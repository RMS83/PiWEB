import time
import uuid

from flask import request

from app import get_bcrypt
from config import TOKEN_TTL
from errors import ApiException
from model import Token

bcrypt = get_bcrypt()


def hash_password(password: str):
    password = password.encode()
    hashed = bcrypt.generate_password_hash(password)
    return hashed.decode()


def check_password(password_hash: str, password: str) -> bool:
    password_hash = password_hash.encode()
    password = bcrypt.check_password_hash(password_hash)
    return password.encode()


def check_auth(session) -> Token:
    try:
        token = uuid.UUID(request.headers.get("Authorization"))
    except (ValueError, TypeError):
        raise ApiException(403, "incorrect token")

    token = session.query(Token).get(token)

    if token is None:
        raise ApiException(403, "incorrect token")
    if time.time() - token.created_at.timestamp() > TOKEN_TTL:
        raise ApiException(403, "incorrect token")

    return token
