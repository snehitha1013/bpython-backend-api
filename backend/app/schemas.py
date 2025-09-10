from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    # pydantic v2: enable from_attributes so ORM models convert to schema
    model_config = {"from_attributes": True}
