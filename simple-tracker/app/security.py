from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from hashlib import sha256
from . import config

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_password_hash(email: str, password: str):
    return sha256(bytes(f"{email}{password}{config.settings.secret_key}", encoding='utf8')).hexdigest()