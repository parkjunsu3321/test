from sqlalchemy import Column, Date, String, Integer, func, ForeignKey
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

    movie_id = Column(Integer, primary_key=True)  # 영화 고유 ID (SERIAL)
    movie_name = Column(String(255), nullable=False)  # 영화 제목
    release_date = Column(Date, nullable=False)  # 개봉일
    audience_count = Column(Integer, nullable=False)  # 관객 수


class ShowingsModel(Base):
    __tablename__ = "showings"
    serial_number = Column(Integer, primary_key=True, index=True)
    theater_name = Column(String(255), nullable=False)
    seat_number = Column(String, nullable=False)
    show_time = Column(String(255), nullable=False)
    movie_id = Column(Integer, ForeignKey('movies.movie_id'))  # 외래 키, 중복된 movie_id 제거
    movie = relationship("MovieModel", backref="showings")  # Movie 테이블과의 관계 설정
