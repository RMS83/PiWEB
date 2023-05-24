import re
from typing import Any, Dict, Optional, Type

from config import PASSWORD_LENGTH
from errors import ApiException
from pydantic import BaseModel, EmailStr, ValidationError, validator

PASSWORD_REGEX = re.compile(
    "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-])*.{{{password_length},}}$".format(
        password_length=PASSWORD_LENGTH
    )
)


class CreateUserSchema(BaseModel):

    email: EmailStr
    password: str

    @validator("password")
    def strong_password(cls, value: str):
        if not PASSWORD_REGEX.match(value):
            raise ValueError("password is to easy")
        return value

# class Register(BaseModel):
#
#     email: EmailStr
#     password: str
#
#     @validator("password")
#     def strong_password(cls, value: str):
#         if not PASSWORD_REGEX.match(value):
#             raise ValueError("password is to easy")
#         return value


class PatchUser(BaseModel):

    email: Optional[EmailStr]
    password: Optional[str]

class CreateAdsSchema(BaseModel):

    title: str
    description: str

class PatchAds(BaseModel):

    title: Optional[str]
    description: Optional[str]


SCHEMA_TYPE = Type[CreateUserSchema] | Type[PatchUser] | Type[CreateAdsSchema] | Type[PatchAds]


def validate(schema: SCHEMA_TYPE, data: Dict[str, Any], exclude_none: bool = True) -> dict:
    try:
        validated = schema(**data).dict(exclude_none=exclude_none)
    except ValidationError as er:
        raise ApiException(400, er.errors())
    return validated