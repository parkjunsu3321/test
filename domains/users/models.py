from sqlalchemy import Column, DateTime, String, Integer, func


from dependencies.database import Base


class User(Base):
    __tablename__ = "users"

    serial_number = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    id = Column(String(50), unique=True, nullable=False)
    nickname = Column(String(30))
    password = Column(String(255), nullable=False)
    birth_date = Column(DateTime)