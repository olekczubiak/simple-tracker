from pydantic import BaseModel
from datetime import date

from typing import Optional

from uuid import UUID

class UserSchema(BaseModel):
    id: int
    email: str
    password: str
    is_active: bool
    company: Optional[str]

    class Config:
        orm_mode = True

class DeviceSchema(BaseModel):
    id: int
    device_name: str
    gps_name: str
    owner_id: int
    description: Optional[str]

    class Config:
        orm_mode = True

class PositionSchema(BaseModel):
    # id: UUID
    owner_id: int
    my_date: Optional[date]
    time: str
    longitude: float
    latitude: float

    class Config:
        orm_mode = True

'''
Making OAuth2 with Password (and hashing), Bearer with JWT tokens
'''
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
