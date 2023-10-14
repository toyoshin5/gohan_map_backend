from sqlalchemy import Column, Integer, String

from app.db import Base


class AnonymousPost(Base):
    """
    匿名投稿モデル
    """

    __tablename__ = "anonymous_post"
    __table_args__ = {"comment": "Swipe UIに使用する匿名投稿用のテーブル"}

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    userId = Column("user_id", String(200))
