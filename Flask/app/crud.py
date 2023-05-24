import psycopg2
from sqlalchemy import select

from errors import ApiException
from model import ORM_MODEL, ORM_MODEL_CLS, ORM_MODEL_ADS, ORM_MODEL_A
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


def get_user(session: Session, model_cls: ORM_MODEL_CLS, item_id: int | str) -> ORM_MODEL:
    user = session.query(model_cls).get(item_id)
    if user is None:
        raise ApiException(404, f"{model_cls.__name__.lower()} not found")
    return user


def create_user(session: Session, model_cls: ORM_MODEL_CLS, commit: bool = True, **params) -> ORM_MODEL:
    new_user = model_cls(**params)
    session.add(new_user)
    if commit:
        try:
            session.commit()
        except IntegrityError as er:
            if isinstance(er.orig, psycopg2.errors.UniqueViolation):
                raise ApiException(409, f"such {model_cls.__name__.lower()} already exists")
    return new_user


def patch_user(session: Session, item: ORM_MODEL, commit: bool = True, **params) -> ORM_MODEL:
    for field, value in params.items():
        setattr(item, field, value)
    session.add(item)
    if commit:
        try:
            session.commit()
        except IntegrityError as er:
            if isinstance(er.orig, psycopg2.errors.UniqueViolation):
                raise ApiException(409, f"attr already exists")
    return item


def delete_user(session: Session, item: ORM_MODEL, commit: bool = True):
    session.delete(item)
    if commit:
        session.commit()



def get_token(session: Session, model_cls: ORM_MODEL_CLS, item_id: int | str) -> ORM_MODEL:
    query = select(model_cls).where(model_cls.user_id==item_id)
    token = session.scalars(query).first()
    if token is None:
        raise ApiException(404, f"{model_cls.__name__.lower()} not found")
    return token



def get_ads(session: Session, model_cls: ORM_MODEL_ADS, item_id: int | str) -> ORM_MODEL_A:
    ads = session.query(model_cls).get(item_id)
    if ads is None:
        raise ApiException(404, f"{model_cls.__name__.lower()} not found")
    return ads


def create_ads(session: Session, model_cls: ORM_MODEL_ADS, commit: bool = True, **params) -> ORM_MODEL_A:
    new_ads = model_cls(**params)
    session.add(new_ads)
    if commit:
        try:
            session.commit()
        except IntegrityError as er:
            if isinstance(er.orig, psycopg2.errors.UniqueViolation):
                raise ApiException(409, f"such {model_cls.__name__.lower()} already exists")
    return new_ads


def patch_ads(session: Session, item: ORM_MODEL_A, commit: bool = True, **params) -> ORM_MODEL_A:
    for field, value in params.items():
        setattr(item, field, value)
    session.add(item)
    if commit:
        try:
            session.commit()
        except IntegrityError as er:
            if isinstance(er.orig, psycopg2.errors.UniqueViolation):
                raise ApiException(409, f"attr already exists")
    return item


def delete_ads(session: Session, item: ORM_MODEL_A, commit: bool = True):
    session.delete(item)
    if commit:
        session.commit()