from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

app.simple_db = []

class Position(BaseModel):
    time: str
    longitude: str
    latitude: str

@app.get("/")
async def root():
    return {"message": f"API for the live monitoring and analyzing"}

@app.get("/live")
async def root():
    LIVE_POZ = "0000:0000:00000"
    return {"message": f"Live poz is {app.simple_db[-1]}"}

@app.post("/add")
async def send_poz(poz: Position):
    print(f"Dodanie nowego rekordu {poz}")
    app.simple_db.append(poz)
    return poz

@app.get("/list")
def list_of_poz():
    return app.simple_db