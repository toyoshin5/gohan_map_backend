from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 接続先DBの設定
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

Engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=Engine)


def get_db():
    return SessionLocal()
