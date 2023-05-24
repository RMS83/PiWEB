import atexit

import uuid
from typing import Type

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, create_engine, func
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy_utils import EmailType, UUIDType
from config import PG_DSN

from datetime import datetime


engine = create_engine(PG_DSN)
Base = declarative_base()


class Ads(Base):

    __tablename__ = "ads"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30), unique=True, nullable=False)
    description = Column(String(120), nullable=False)
    creation_time = Column(DateTime(), default=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    user = relationship("User", back_populates='adss')

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(EmailType, unique=True, index=True)
    password = Column(String(60), nullable=False)
    registration_time = Column(Date, server_default=func.now())
    adss = relationship("Ads", back_populates='user', cascade="all, delete-orphan")


class Token(Base):

    __tablename__ = "tokens"

    id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("User", lazy="joined")



Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

atexit.register(lambda: engine.dispose())

ORM_MODEL_CLS = Type[User] | Type[Token]
ORM_MODEL = User | Token
ORM_MODEL_ADS = Type[User] | Type[Ads]
ORM_MODEL_A = User | Ads