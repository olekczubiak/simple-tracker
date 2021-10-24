from typing import List

from sqlalchemy.sql.functions import user
from fastapi import FastAPI, HTTPException, status, Depends
# from .schemas import PositionSchema, UserSchema, DeviceSchema
from sqlalchemy.orm import Session
from .database import get_db
# from .models import Position, User, Device
from . import crud, models, schemas


app = FastAPI()

app.simple_db = []

# @app.get("/")
# async def root():
#     return {"message": f"Go to /api to get api, go to /docs to see docs"}


# @app.get("/api/")
# async def root():
#     return {"message": f"API for the live monitoring and analyzing"}

@app.get("/api/list/")
async def get_listed_poz(db: Session = Depends(get_db)):
    return crud.get_position(db)

# @app.post("/api/add/", status_code=status.HTTP_201_CREATED)
# async def send_poz(details: schemas.PositionSchema, db: Session = Depends(get_db)):
#     to_create = Position(
#         id = details.id,
#         owner_id = details.owner_id,
#         my_date=details.my_date,
#         time=details.time,
#         longitude=details.longitude,
#         latitude=details.latitude
#     )
#     db.add(to_create)
#     db.commit()
#     print("debug")
#     return {
#         "success": True,
#         "created_id": to_create.id
#     }

@app.post("/api/add/",  response_model=schemas.PositionSchema)
async def send_poz(item: schemas.PositionSchema, db: Session = Depends(get_db)):
    return crud.create_position(db=db, item=item)


    # if details in app.simple_db:
    #     raise HTTPException(status_code=409, detail="Conflict")
    # else:
    #     app.simple_db.append(details)
    # return details

# @app.get("/api/info/")
# async def device_info():
#     return {"message": "Pobiera z bazy danych informacje o urządeniu"}

# @app.get("/api/list/")
# def list_of_poz():
#     return app.simple_db