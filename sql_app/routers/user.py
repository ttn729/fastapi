

from fastapi import status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils, crud
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=['Users'])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    # hash the user password
    # TODO: maybe move to crud.py

    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = crud.create_user(db, user)
    return new_user

@router.get('/{id}', response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id: {id} does not exist")
    
    return user