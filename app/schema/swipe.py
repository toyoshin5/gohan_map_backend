from pydantic import BaseModel


class SwipePostRequest(BaseModel):
    latitude: float
    longitude: float
    radius: int


class SwipePost(BaseModel):
    id: int
    googleMapShopId: str
    imageURL: str
    star: float
