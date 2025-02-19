from pydantic import BaseModel, field_validator, Field
from datetime import datetime, timezone
from typing import Optional, List
import re

class Role(BaseModel):
    name: Optional[str] = None



class UserBase(BaseModel):
    phone_number: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[int] = Field(default=...)
    started_at: Optional[datetime] = datetime.now(timezone.utc)


class UserCreateSchemas(UserBase):
    password: Optional[str] = None

    @classmethod
    @field_validator("phone_number")
    def check_number(cls, v):
        params = (r"\(\w{3}\) \w{3}\-\w{4}", r"^\w{3}\-\w{4}$")
        if not re.search(params[0], v):
            return ValueError("not match")
        return v


class UserReadSchemas(UserBase):
    role_rel: Optional['Role'] = None
    orders: Optional[List['']] = None

class UserUpdateSchemas(UserBase):
    pass


class PasswordUpdateSchemas(BaseModel):
    old_password: Optional[str] = None
    new_password: Optional[str] = None
    confirm_password: Optional[str] = None

