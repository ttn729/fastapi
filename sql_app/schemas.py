from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None = None

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse


    class Config:
        from_attributes = True

class PostResponse(BaseModel):
    Post: Post
    votes: int

class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1)

    class Config:
        from_attributes = True