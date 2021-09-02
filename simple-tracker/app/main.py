from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

app.simple_db = []


class Position(BaseModel):
    time: str
    cords: str

@app.get("/")
async def root():
    return {"message": f"Check POST METHOD: {app.simple_db}"}

@app.post("/poz")
async def send_poz(poz: Position):
    print(f"Dodanie nowego rekordu {poz}")
    app.simple_db.append(poz)
    return poz

@app.get("/list")
def list_of_poz():
    return app.simple_db