from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
from . import schemas, crud
from pydantic import BaseModel
from typing import Optional
from passlib.context import CryptContext
from sqlalchemy.orm import Session, session
from hashlib import sha256

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_password_hash(email: str, password: str):
    return sha256(bytes(f"{email}{password}{SECRET_KEY}", encoding='utf8')).hexdigest()