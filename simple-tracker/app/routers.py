from fastapi import APIRouter
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from .database import get_db
from . import crud, schemas

router = APIRouter()


# @router.get("/")
# async def root():
#     return {"message": f"Go to /api to get api, go to /docs to see docs"}


@router.get("/api/")
async def api_info():
    return {"message": f"API for the live monitoring and analyzing. Go to /docs for more info. "}

@router.get("/api/live")
async def get_live_poz(db: Session = Depends(get_db)):
    return crud.get_live_position(db)

@router.get("/api/list/")
async def get_listed_poz(db: Session = Depends(get_db)):
    return crud.get_position(db)

@router.post("/api/add/",  response_model=schemas.PositionSchema)
async def send_poz(item: schemas.PositionSchema, db: Session = Depends(get_db)):
    if not crud.check_user_id_exist(db, item.owner_id):
        raise HTTPException(status_code=409, detail="No owner_id in db")
    return crud.create_position(db=db, item=item)

# @router.get("/api/deive/")
# async def device_info():
#     return {"message": "Pobiera z bazy danych informacje o urządeniu"}