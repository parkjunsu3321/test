from typing  import Optional
from datetime import date
from pydantic import BaseModel, Json

class User(BaseModel):
    serial_number: Optional[int] = None
    id: str
    name: str
    nickname: str
    password: str
    birth_date: str

class LoginUser(BaseModel):
    id: str
    password: str

class Movie(BaseModel):
    movie_id: Optional[int] = None
    movie_name: str
    release_date: date
    audience_count: int

class MovieAddDTO(BaseModel):
    movie_info:Movie

class InputDTO(BaseModel):
    m_payload:Json
    theater_name:str
    show_time:str

class BookingDTO(BaseModel):
    theater_name:str
    show_time:str
    seat_number:list[int]