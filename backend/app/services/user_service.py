from sqlalchemy.orm import Session
from crud.user import create_user, get_user
from schemas.user import UserCreate

def register_user(db: Session, user_data: UserCreate):
    existing_user = get_user(db, user_data.user_id)
    if existing_user:
        raise ValueError("이미 존재하는 id입니다.")

    return create_user(db, user_data)
