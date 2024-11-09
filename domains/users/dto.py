from typing  import Optional
from datetime import date
from pydantic import BaseModel

class User(BaseModel):
    serial_number: Optional[int] = None
    id: str
    name: str
    nickname: str
    password: str
    birth_date: date

class LoginUser(BaseModel):
    id: str
    password: str

class Movie(BaseModel):
    movie_id: Optional[int] = None
    movie_name: str
    release_date: date
    audience_count: int

class Showings(BaseModel):
    serial_number: Optional[int] = None
    theater_name: str
    seat_number: str
    show_time: str
    movie_info: Movie