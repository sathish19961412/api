from pydantic import BaseModel
from typing import List, Union,Optional


class UserBase(BaseModel):
    email: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):

    password: str


class User(UserBase):
    user_id: int
  #  applied_job: Optional[JobBase]  # = []

    class Config:
        orm_mode = True