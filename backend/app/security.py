from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from hashlib import sha256

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "4b19a623edda8ca470c6191c0d7a34ff51425f26012ec4ef9c7fc3fe885da923"


def get_password_hash(email: str, password: str):
    return sha256(bytes(f"{email}{password}{SECRET_KEY}", encoding='utf8')).hexdigest()