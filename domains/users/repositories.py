from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from .models import UserModel


class UserRepository:
    def __init__(self, session: Session):
        self._session = session
