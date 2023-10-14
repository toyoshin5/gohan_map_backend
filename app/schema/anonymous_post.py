from fastapi import UploadFile
from pydantic import BaseModel, Field


class AnonymousPostCreate(BaseModel):
    timelineId: int = Field(description="端末で保存されているタイムラインのID")
    googleMapShopId: str
    star: int
    imageList: list[UploadFile]


class AnonymousPost(BaseModel):
    id: int
    timelineId: int = Field(description="端末で保存されているタイムラインのID")
    googleMapShopId: str
    star: int
    imageURLList: list[str]
