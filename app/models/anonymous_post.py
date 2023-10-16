from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Relationship, relationship

from app.db import Base
from app.models.anonymous_post_image import AnonymousPostImage


class AnonymousPost(Base):
    """
    匿名投稿モデル
    """

    __tablename__ = "anonymous_post"
    __table_args__ = {"comment": "Swipe UIに使用する匿名投稿用のテーブル"}

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    userId = Column("user_id", String(200), nullable=False)
    timelineId = Column("timeline_id", Integer, nullable=False)
    googleMapShopId = Column(
        "google_map_shop_id",
        String(200),
        ForeignKey(
            "google_map_shop.google_map_shop_id", onupdate="CASCADE", ondelete="CASCADE"
        ),
        nullable=False,
    )
    star = Column(
        "star",
        Float(),
        nullable=False,
    )
    anonymousPostImages: Relationship[AnonymousPostImage] = relationship(
        "AnonymousPostImage"
    )

    createdAt = Column("created_at", DateTime, default=datetime.now(), nullable=False)
    updatedAt = Column(
        "updated_at",
        DateTime,
        default=datetime.now(),
        onupdate=datetime.now(),
        nullable=False,
    )
