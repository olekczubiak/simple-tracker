from fastapi import APIRouter
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from .database import get_db
from . import crud, schemas

router = APIRouter()

@router.get("/api/")
async def api_info():
    return {"message": f"API for the live monitoring and analyzing. Go to /docs for more info. "}

@router.get("/api/live")
async def get_live_poz(db: Session = Depends(get_db)):
    return crud.get_live_position(db)

@router.get("/api/list")
async def get_listed_poz(db: Session = Depends(get_db)):
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
async def device_info(owner_id: int, db: Session = Depends(get_db)):
    db_query = crud.get_device_info(db, owner_id)
    if len(db_query) == 0:
        raise HTTPException(status_code=404, detail="No owner_id found")
    return db_query