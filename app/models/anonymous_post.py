from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.orm import relationship

from app.db import Base


class AnonymousPost(Base):
    """
    匿名投稿モデル
    """

    __tablename__ = "anonymous_post"
    __table_args__ = {"comment": "Swipe UIに使用する匿名投稿用のテーブル"}

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    userId = Column("user_id", Integer)
    timelineId = Column("timeline_id", Integer)
    googleMapShopId = Column("google_map_shop_id", String(200))
    star = Column("star", Numeric(2, 1))
    anonymousPostImages = relationship("anonymous_post_image")

    createdAt = Column("created_at", DateTime, default=datetime.now(), nullable=False)
    updatedAt = Column(
        "updated_at",
        DateTime,
        default=datetime.now(),
        onupdate=datetime.now(),
        nullable=False,
    )
