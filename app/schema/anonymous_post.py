from fastapi import UploadFile
from pydantic import BaseModel, Field


class AnonymousPostCreate(BaseModel):
    timelineId: int = Field(description="端末で保存されているタイムラインのID")
    googleMapShopId: str
    star: float
    imageList: list[UploadFile]


class AnonymousPost(BaseModel):
    id: int
    userId: str
    timelineId: int = Field(description="端末で保存されているタイムラインのID")
    googleMapShopId: str
    star: float
    imageURLList: list[str]
    createdAt: str
    updatedAt: str
