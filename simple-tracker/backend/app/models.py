from sqlalchemy import Integer, String, Boolean, Column, ForeignKey, Date, Float
from sqlalchemy.sql.schema import Column
# from sqlalchemy.sql.sqltypes import Date, DateTime, Float
from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    company = Column(String)


class Device(Base):
    __tablename__ = 'device'

    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String)
    gps_name = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    description = Column(String, index=True)

class Position(Base):
    __tablename__ = 'position'

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    my_date = Column(Date)
    time = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
