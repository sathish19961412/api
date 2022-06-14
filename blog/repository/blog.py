from sqlalchemy.orm import Session
from .. import models
from ..routers import schemas
from fastapi import HTTPException, status

def gell_all(db: Session):
    blogs = db.query( models.Blog ).all( )
    return blogs

def create(request: schemas.Blog , db: Session):
    new_blog = models.Blog( title=request.title , body=request.body , user_id=1 )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id: int, db: Session):
    blog = db.query( models.Blog ).filter( models.Blog.id == id )

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id , request: schemas.Blog , db:Session):
    blog = db.query( models.Blog ).filter( models.Blog.id == id )

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.update(request)
    return "updated"

def show(id, db:Session):
    blog = db.query( models.Blog ).filter( models.Blog.id == id ).first( )

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    return blog








