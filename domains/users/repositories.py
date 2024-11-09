from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from .models import UserModel, ShowingsModel
from dependencies.auth import hash_password
from domains.users.dto import User


class UserRepository:
    def __init__(self, session: Session):
        self._session = session

    def find_id(self, user_id: str):
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()

    def add_user(self, user_data: User):
        db_user = UserModel(
            id=user_data.id,
            name=user_data.name,
            nickname=user_data.nickname,
            password=hash_password(user_data.password),
            birth_date=user_data.birth_date
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def get_seat(self, type:str):
        showings = self.db.query(ShowingsModel).filter(ShowingsModel.theater_name == type).first()
        return showings