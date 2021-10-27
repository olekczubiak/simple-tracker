from sqlalchemy.orm import Session

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.elements import True_
from sqlalchemy.sql.expression import desc

from . import models, schemas

def get_device_info(db: Session, my_owner_id: int):
    return db.query(models.Device).filter(models.Device.owner_id == my_owner_id).all()

def get_position(db: Session):
    return db.query(models.Position).all()

def get_live_position(db: Session):
    return db.query(models.Position).all()[-1]

def get_owner_id_by_email(db: Session, email: str):
    return db.query(models.User.id).filter(models.User.email == email).first()[0]

def create_position(db: Session, item: schemas.PositionSchema):
    db_item = models.Position(**item.dict())
    db.add(db_item)
    try:
        db.commit()
    except SQLAlchemyError as e:
        print(str(e))
        db.session.rollback()
    db.refresh(db_item)
    return db_item

def check_user_id_exist(db: Session, my_owner_id: int):
    return db.query(models.User.id).filter(models.User.id == my_owner_id).first()

def check_if_last_time_exist(db: Session):
    return db.query(models.Position.time).order_by(models.Position.id.desc()).first()[0]

def check_email_is_in_db(db: Session, email: str):
    return db.query(models.User.email).filter(models.User.email == email).first()

def check_hash_password_is_in_db(db: Session, hash_pass: str):
    return db.query(models.User.hashed_password).filter(models.User.hashed_password == hash_pass).first()

def check_is_user_active(db: Session, email: str) -> bool:
    return db.query(models.User.is_active).filter(models.User.email == email).first()[0]
