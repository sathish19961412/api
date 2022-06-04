from fastapi import APIRouter, Depends, status
from . import schemas
from typing import List
from api.database import get_db
from sqlalchemy.orm import Session
from ..repository import blog
from .. import oauth2

router = APIRouter(
    prefix= "/blog",
    tags=["Blog"]
)


@router.get('', response_model=List[schemas.ShowBlog] )
def all(db: Session = Depends(get_db),current_user: schemas.User = Depends( oauth2.
                                                                            get_current_user )):
    return blog.gell_all( db , current_user )



@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog , db: Session = Depends( oauth2.get_current_user )):
    return blog.create( request , db )


@router.delete('/{id}', status_code=204)
def destroy(id: int , db: Session = Depends( oauth2.get_current_user )):
    return blog.delete( id , db )


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int , request: schemas.Blog , db: Session = Depends( oauth2.get_current_user )):
    return blog.update( id , request , db )


@router.get('/{id}', status_code=200, response_model= schemas.ShowBlog )
def show(id: int , db: Session = Depends( oauth2.get_current_user )):
    return blog.show( id , db )


