from sqlalchemy.orm import Session
from fastapi import status, HTTPException

from . import models, schemas

def get_post(db: Session, id: int):
    return db.query(models.Post).filter(models.Post.id == id).first()

def get_posts(db: Session):
    return db.query(models.Post).all()

def create_post(db: Session, post: schemas.Post):
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def update_post(db: Session, id: int, updated_post: schemas.Post):
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
    
    post_query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()

    return post_query.first()

def delete_post(db: Session, id: int):
    post_query = db.query(models.Post).filter(models.Post.id == id)

    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
    
    post_query.delete(synchronize_session=False)
    db.commit()

def create_user(db: Session, user: schemas.UserCreate):
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user