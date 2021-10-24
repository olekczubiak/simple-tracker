from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user

from sqlalchemy.exc import SQLAlchemyError

from . import models, schemas

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

def get_position(db: Session):
    return db.query(models.Position).all()
