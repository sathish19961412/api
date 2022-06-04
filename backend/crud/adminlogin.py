from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from schemas import adminlogin as schema_adminlogin
from models import adminlogin as model_adminlogin
from .hashing import Hash as hash


def create_user(db: Session, user: schema_adminlogin.UserCreate):
    # fake_hashed_password = user.password + "notreallyhashed"

    db_user = model_adminlogin.User(email=user.email, hashed_password=hash.bcrypt(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):

    return db.query(model_adminlogin.User).filter(model_adminlogin.User.email == email).first()

def get_user(db: Session, user_id: int):

    return db.query(model_adminlogin.User).filter(model_adminlogin.User.user_id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):

    return db.query(model_adminlogin.User).offset(skip).limit(limit).all()
