from sqlalchemy import Column, Date, String, Integer,ARRAY, Boolean, JSON
from sqlalchemy.orm import relationship

from dependencies.database import Base


class UserModel(Base):
    __tablename__ = "users"

    serial_number = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    id = Column(String(255), unique=True, nullable=False)
    nickname = Column(String(255))
    password = Column(String(255), nullable=False)
    birth_date = Column(String(255))

    
class MovieModel(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True, index=True)  # 영화 고유 ID (SERIAL)
    movie_name = Column(String(255), nullable=False)  # 영화 제목
    release_date = Column(Date, nullable=False)  # 개봉일
    audience_count = Column(Integer, nullable=False)  # 관객 수


class ShowingsModel(Base):
    __tablename__ = "showings"

    id = Column(Integer, primary_key=True, index=True)  # id로 변경
    movie_info = Column(JSON, nullable=True)  # movie_info를 JSON 형식으로 변경
    theater_name = Column(String(50), nullable=False)
    seat_numbers = Column(ARRAY(Integer), nullable=False)  # seat_numbers를 integer 배열로 수정
    show_time = Column(String, nullable=False)
    state = Column(Boolean, nullable=False)  # state 컬럼 추가