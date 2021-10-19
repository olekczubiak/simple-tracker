from pydantic import BaseModel

class Position(BaseModel):
    time: str
    longitude: str
    latitude: str