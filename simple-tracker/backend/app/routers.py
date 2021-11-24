from typing import Optional
from fastapi import APIRouter
from fastapi import HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .database import get_db
from datetime import date
from . import crud, schemas
from . import security as sec

router = APIRouter()

@router.get("/api/")
async def api_info():
    return {"message": f"API for the live monitoring and analyzing. Go to /docs for more info. "}

@router.get("/api/live")
async def get_live_poz(
                            db: Session = Depends(get_db), 
                            token: str =  Depends(sec.oauth2_scheme)):
    user_id = crud.get_owner_id_by_token(db, my_token=token)
    return crud.get_live_position(db, user_id)

@router.get("/api/list")
async def get_listed_poz(
                            db: Session = Depends(get_db), 
                            token: str =  Depends(sec.oauth2_scheme)):
    user_id = crud.get_owner_id_by_token(db, my_token=token)
    return crud.get_position(db, user_id)


@router.get("/api/list/day")
async def get_day_listed(
                            day: Optional[date],
                            db: Session = Depends(get_db),
                            token: str =  Depends(sec.oauth2_scheme)):
    user_id = crud.get_owner_id_by_token(db, my_token=token)
    return crud.get_list_poz_by_day(db, user_id=user_id, my_day=day)

@router.get("/api/list/monthly")
async def get_all_events_in_month(  
                            month: Optional[int],
                            db: Session = Depends(get_db),
                            token: str =  Depends(sec.oauth2_scheme)):
    user_id = crud.get_owner_id_by_token(db, my_token=token)
    return crud.get_list_of_events_in_month(db, user_id, month)

@router.get("/api/device")
async def device_info(
                        db: Session = Depends(get_db),
                        token: str =  Depends(sec.oauth2_scheme)):
    user_id = crud.get_owner_id_by_token(db, my_token=token)
    db_query = crud.get_device_info(db, user_id)
    if len(db_query) == 0:
        raise HTTPException(status_code=404, detail="No owner_id found")
    return db_query

@router.post("/api/add",  response_model=schemas.PositionSchema)
async def send_poz(
                            item: schemas.PositionSchema, 
                            db: Session = Depends(get_db),
                            token: str =  Depends(sec.oauth2_scheme)):
    if crud.check_if_last_time_exist(db) == item.time:
        raise HTTPException(status_code=409, detail="Conflict")
    else:
        user_id = crud.get_owner_id_by_token(db, my_token=token)
        return crud.create_position(db=db, item=item, user_id=user_id)

@router.post("/api/add/more",  response_model=schemas.PositionSchema)
async def send_poz(
                            item: schemas.PositionList, 
                            db: Session = Depends(get_db),
                            token: str =  Depends(sec.oauth2_scheme)
                            ):
        for single_record in item.my_list:
            # if crud.check_if_last_time_exist(db) == single_record.time:
            #     raise HTTPException(status_code=409, detail="Conflict")
            # else:
            user_id = crud.get_owner_id_by_token(db, my_token=token)
            crud.create_position(db=db, item=single_record, user_id=user_id)
        return JSONResponse(status_code=200, content={"message": "Adding success"})

@router.post("/token")
async def login(
                        db: Session = Depends(get_db), 
                        form_data: sec.OAuth2PasswordRequestForm = Depends()
                        ):
    check_email = crud.check_email_is_in_db(db, form_data.username)
    owner_id = crud.get_owner_id_by_email(db, email=form_data.username)
    if check_email == None:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    check_credentials = crud.check_hash_password_is_in_db(db, sec.get_password_hash(form_data.username, form_data.password))
    if check_credentials == None:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    is_active = crud.check_is_user_active(db, email=form_data.username)
    if is_active == False:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token = check_credentials[0]
    return {"access_token": access_token, "token_type": "bearer", "owner_id": owner_id}


@router.post("/user/create")
async def create_user(user: schemas.UserSchema,db: Session = Depends(get_db)):
    user_exist = crud.check_if_creating_user_exist(db, user.email, sec.get_password_hash(user.email, user.password))
    if user_exist == True:
        raise HTTPException(status_code=409, detail="Confilct")
    return crud.create_user(db, details=user, hash_password=sec.get_password_hash(user.email, user.password))


@router.get("/token/test")
async def test_token(token: str = Depends(sec.oauth2_scheme)):
    return {"the_token": token}

@router.get("/token/test/user-id")
async def test_root(db: Session = Depends(get_db),
                    token: str =  Depends(sec.oauth2_scheme)):
    user_id = crud.get_owner_id_by_token(db, my_token=token)
    return user_id

