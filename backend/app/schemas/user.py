from pydantic import BaseModel

class UserCreate(BaseModel):
    user_id: str
    password: str

class UserResponse(BaseModel):
    id: int
    user_id: str

    class Config:
        orm_mode = True
