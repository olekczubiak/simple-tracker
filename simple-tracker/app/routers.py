from fastapi import APIRouter
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from .database import get_db
from . import crud, schemas
from . import security as sec

router = APIRouter()

@router.get("/api/")
async def api_info():
    return {"message": f"API for the live monitoring and analyzing. Go to /docs for more info. "}

@router.get("/api/live")
async def get_live_poz(
                            db: Session = Depends(get_db), 
                            auth = Depends(sec.oauth2_scheme)):
    return crud.get_live_position(db)

@router.get("/api/list")
async def get_listed_poz(
                            db: Session = Depends(get_db), 
                            auth = Depends(sec.oauth2_scheme)):
    return crud.get_position(db)

@router.post("/api/add",  response_model=schemas.PositionSchema)
async def send_poz(item: schemas.PositionSchema, db: Session = Depends(get_db)):
    if not crud.check_user_id_exist(db, item.owner_id):
        raise HTTPException(status_code=404, detail="No owner_id found")
    if crud.check_if_last_time_exist(db) == item.time:
        raise HTTPException(status_code=409, detail="Conflict")
    else:
        return crud.create_position(db=db, item=item)

@router.get("/api/device/{owner_id}")
async def device_info(
                        owner_id: int, 
                        db: Session = Depends(get_db),
                        auth = Depends(sec.oauth2_scheme)):
    db_query = crud.get_device_info(db, owner_id)
    if len(db_query) == 0:
        raise HTTPException(status_code=404, detail="No owner_id found")
    return db_query

'''
Making OAuth2 with Password (and hashing), Bearer with JWT tokens
'''

from . import models


@router.post("/token")
async def login(
                        db: Session = Depends(get_db), 
                        form_data: sec.OAuth2PasswordRequestForm = Depends()):
    check_email = crud.check_email_is_in_db(db, form_data.username)
    if check_email == None:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    check_credentials = crud.check_hash_password_is_in_db(db, sec.get_password_hash(form_data.username, form_data.password))
    if check_credentials == None:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": form_data.username, "token_type": "bearer"}


@router.get("/test")
async def read_users_me(auth = Depends(sec.oauth2_scheme)):
    return {"message": "success"}