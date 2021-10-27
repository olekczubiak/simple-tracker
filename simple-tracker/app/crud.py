from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.elements import True_
from sqlalchemy.sql.sqltypes import Float

from . import models, schemas, security

def get_device_info(db: Session, user_id: int):
    return db.query(models.Device).filter(models.Device.owner_id == user_id).all()

def get_position(db: Session, user_id: int):
    return db.query(models.Position).filter(models.Position.owner_id == user_id).all()

def get_live_position(db: Session, user_id: int):
    return db.query(models.Position).filter(models.Position.owner_id == user_id).all()[-1]

def get_owner_id_by_email(db: Session, email: str):
    return db.query(models.User.id).filter(models.User.email == email).first()[0]

def get_owner_id_by_token(db: Session, my_token: str):
    return db.query(models.User.id).filter(models.User.hashed_password == my_token).first()[0]

def get_last_index_of_id(db: Session) -> int:
    return db.query(models.User.id).order_by(models.User.id.desc()).first()[0]

def create_position(db: Session, item: schemas.PositionSchema, user_id:int):
    db_item = models.Position(
                owner_id=user_id,
                my_date=item.my_date,
                time=item.time,
                latitude=item.latitude,
                longitude=item.longitude
    )
    db.add(db_item)
    try:
        db.commit()
    except SQLAlchemyError as e:
        print(str(e))
        db.session.rollback()
    db.refresh(db_item)
    return db_item

def check_if_last_time_exist(db: Session):
    return db.query(models.Position.time).order_by(models.Position.id.desc()).first()[0]

def check_email_is_in_db(db: Session, email: str):
    return db.query(models.User.email).filter(models.User.email == email).first()

def check_hash_password_is_in_db(db: Session, hash_pass: str):
    return db.query(models.User.hashed_password).filter(models.User.hashed_password == hash_pass).first()

def check_is_user_active(db: Session, email: str) -> bool:
    return db.query(models.User.is_active).filter(models.User.email == email).first()[0]

def check_if_creating_user_exist(db: Session, user_email: str, hash_pass: str) -> bool:
    email = db.query(models.User.email).filter(models.User.email == user_email).all()
    password = db.query(models.User.hashed_password).filter(models.User.hashed_password == hash_pass).all()
    print(len(email))
    print(len(password))
    if len(email) == 1:
        return True
    if len(email) == 0:
        if len(password) == 0:
            return False


def create_user(db: Session, details: schemas.UserSchema):
    db_item = models.User(
                id=get_last_index_of_id(db) + 1,
                email= details.email,
                hashed_password=security.get_password_hash(details.email, details.password),
                is_active = False,
                company = details.company
    )
    db.add(db_item)
    try:
        db.commit()
    except SQLAlchemyError as e:
        print(str(e))
        db.session.rollback()
    db.refresh(db_item)
    return db_item