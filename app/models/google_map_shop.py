from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base


class GoogleMapShop(Base):
    """
    GoogleMapの店情報を保存するテーブル
    """

    __tablename__ = "google_map_shop"
    __table_args__ = {"comment": "GoogleMapのshopIdに対応した情報を、APIを叩く回数を減らすために保存する。"}

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    googleMapShopId = Column(
        "google_map_shop_id", String(200), nullable=False, unique=True
    )
    latitude = Column(
        "latitude",
        Float(),
        nullable=False,
    )
    longitude = Column(
        "longitude",
        Float(),
        nullable=False,
    )
    anonymousPost = relationship("AnonymousPost")

    createdAt = Column("created_at", DateTime, default=datetime.now(), nullable=False)
    updatedAt = Column(
        "updated_at",
        DateTime,
        default=datetime.now(),
        onupdate=datetime.now(),
        nullable=False,
    )
