from sqlalchemy.orm import Session
from fastapi import  APIRouter, Depends, HTTPException, status
from .. import models, token
from . import schemas
from api.database import get_db
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
tags=['Authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query( models.User ).filter( models.User.email == request.username ).first( )


    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"invalid candidate")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")


    # generate a jwt token and return

    access_token = token.create_access_token( data={"sub": user.email} )

    return {"access_token": access_token, "token_type": "bearer"}
    # return user
