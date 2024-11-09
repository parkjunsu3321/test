from typing import Optional
from .config import DefaultConfig,get_config

from sqlalchemy.engine import Engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import Session, sessionmaker

Base = declarative_base()
db_engine: Optional[Engine] = None
db_session: Optional[Session] = None
DBSessionLocal: Optional[sessionmaker] = None


def init_db(config: DefaultConfig) -> None:
    global db_engine, DBSessionLocal, db_session

    postgres_endpoint = config.postgresql_endpoint
    postgres_port = config.postgresql_port
    postgres_table = config.postgresql_table
    postgres_user = config.postgresql_user
    postgres_password = config.postgresql_password

    db_url = (
        "postgresql://"
        + f"{postgres_user}:{postgres_password}"
        + f"@{postgres_endpoint}:{postgres_port}/{postgres_table}"
    )

    db_engine = create_engine(db_url)
    DBSessionLocal = sessionmaker(autoflush=False, bind=db_engine)


def provide_session():
    if DBSessionLocal is None:
        raise ImportError("You need to call init_db before this function")

    db_session = DBSessionLocal()

    try:
        yield db_session
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        raise e
    finally:
        db_session.close()