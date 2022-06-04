from fastapi import FastAPI , Depends,HTTPException,status
from database import engine , SessionLocal
from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter
from crud import adminlogin as crud_adminlogin
from schemas import adminlogin as schema_adminlogin
from models import adminlogin as model_adminlogin
from fastapi import  FastAPI, Depends, HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from database import engine , SessionLocal
from sqlalchemy.orm import Session
from endpoint import token_a
from crud import hashing as hassed_password

router = APIRouter()

model_adminlogin.Base.metadata.create_all( engine )


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users/", response_model=List[schema_adminlogin.User],tags=["Users"])
def get_question(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud_adminlogin.get_users(db,skip=skip, limit=limit)
    return users

@router.post("/users/", response_model=schema_adminlogin.User,tags=["Users"])
def create_user(user: schema_adminlogin.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_adminlogin.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_adminlogin.create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=schema_adminlogin.User,tags=["Users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_adminlogin.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post('/login',tags=["Users"])
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(model_adminlogin.User).filter(model_adminlogin.User.email == request.username).first()



    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"invalid candidate")
    if not hassed_password.Hash.verify(user.hashed_password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")


    # generate a jwt token and return

    access_token =token_a.create_access_token( data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}
    # return user
