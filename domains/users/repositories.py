from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from .models import UserModel, ShowingsModel, MovieModel
from dependencies.auth import hash_password
from domains.users.dto import User, Movie, InputDTO, BookingDTO


class UserRepository:
    def __init__(self, session: Session):
        self.db = session

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
    
    def get_seat(self):
        showings = self.db.query(ShowingsModel).all()
        return showings
    
    def movie_add(self, movie_info:Movie):
        db_mv = MovieModel(
            movie_id=movie_info.movie_id,
            movie_name = movie_info.movie_name,
            release_date = movie_info.release_date,
            audience_count = movie_info.audience_count
        )
        if self.db.query(MovieModel).filter(MovieModel.movie_id != movie_info.movie_id):
            self.db.add(db_mv)
            self.db.commit()
            self.db.refresh(db_mv)
        return db_mv

    def update_showing(self, payload:InputDTO):
        db_sw:ShowingsModel = self.db.query(ShowingsModel).filter(ShowingsModel.theater_name == payload.theater_name, ShowingsModel.show_time == payload.show_time).first()
        db_sw.movie_info = payload.m_payload
        db_sw.state = True
        self.db.commit()
        self.db.refresh(db_sw)
        return db_sw
    
    def booking_showings(self, payload:BookingDTO):
        db_sw:ShowingsModel = self.db.query(ShowingsModel.theater_name == payload.theater_name, ShowingsModel.show_time == payload.show_time)
        db_sw.seat_numbers = payload.seat_number
        self.db.commit()
        self.db.refresh(db_sw)
        return db_sw