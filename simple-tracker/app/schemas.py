from sqlalchemy.sql.sqltypes import Date
from pydantic import BaseModel
from datetime import date

from uuid import UUID

class UserSchema(BaseModel):
    id: int
    email: str
    password: str
    is_active: bool
    company: str

    class Config:
        orm_mode = True

class DeviceSchema(BaseModel):
    id: int
    device_name: str
    gps_name: str
    owner_id: int
    description: str

    class Config:
        orm_mode = True



class PositionSchema(BaseModel):
    # id: UUID
    owner_id: int
    my_date: date
    time: str
    longitude: float
    latitude: float

    class Config:
        orm_mode = True