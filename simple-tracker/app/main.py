from fastapi import FastAPI, HTTPException, status
from .schemas import Position

app = FastAPI()

app.simple_db = []

@app.get("/")
async def root():
    return {"message": f"API for the live monitoring and analyzing"}

@app.get("/live/")
async def root():
    return {"message": f"Live poz is {app.simple_db[-1]}"}

@app.post("/add/", status_code=status.HTTP_201_CREATED)
async def send_poz(poz: Position):
    if poz in app.simple_db:
        raise HTTPException(status_code=409, detail="Conflict")
    else:
        app.simple_db.append(poz)
    return poz

@app.get("/info/")
async def device_info():
    return {"message": "Pobiera z bazy danych informacje o urządeniu"}

@app.get("/list/")
def list_of_poz():
    return app.simple_db