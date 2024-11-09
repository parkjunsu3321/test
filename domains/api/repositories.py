from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status


class APIRepository:
    def __init__(self, session: Session):
        self._session = session
