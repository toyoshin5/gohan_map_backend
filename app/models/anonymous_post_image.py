from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from app.db import Base


class AnonymousPost(Base):
    """
    匿名投稿の画像モデル
    """

    __tablename__ = "anonymous_post_image"
    __table_args__ = {"comment": "Swipe UIに使用する匿名投稿用の画像パスを保存するテーブル"}

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    anonymousPostId = Column(
        "anonymous_post_id",
        Integer,
        ForeignKey("anonymous_post.id", onupdate="CASCADE", ondelete="CASCADE"),
    )
    fileName = Column("file_name", String(200))

    createdAt = Column("created_at", DateTime, default=datetime.now(), nullable=False)
    updatedAt = Column(
        "updated_at",
        DateTime,
        default=datetime.now(),
        onupdate=datetime.now(),
        nullable=False,
    )
