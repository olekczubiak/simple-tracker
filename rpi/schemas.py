from pydantic import BaseModel

class Data(BaseModel):
    time: str
    longitude: str
    latitude: str

class Device(BaseModel):
    id: int
    name: str = "Raspberry PI 3B+"
    gps_name: str = "NEO 6M"
    owner: str = "Olek"
    description: str = "Default description"

def my_dict(data, time, lat, lng):
    return {"owner_id":0,"my_date":data ,"time":time,"longitude":lng,"latitude":lat}

