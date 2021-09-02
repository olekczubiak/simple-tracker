from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/")
def get_poz() -> dict:
    return {"message":"test metody GET udany"}

@router.post("/")
def post_poz() -> dict:
    return {"message":"test metody POST udany"}