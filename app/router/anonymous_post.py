import logging
from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials

import app.schema.anonymous_post as post_schema
from app.dependency import get_current_user

router = APIRouter()

logger = logging.getLogger("gohan_map")


@router.get("/api/anonymous-post", response_model=list[post_schema.AnonymousPost])
async def list_anonymous_post(
    cred: dict[str, Any] = Depends(get_current_user),
) -> list[post_schema.AnonymousPost]:
    logger.debug("request: GET /api/anonymous-post")
    uid: str = cred["uid"]
    return [
        post_schema.AnonymousPost(
            id=1,
            googleMapShopId=uid,
            timelineId=1,
            star=1,
            imageURLList=["http://example.com"],
        )
    ]


@router.post("/api/anonymous-post")
async def create_anonymous_post(post: post_schema.AnonymousPostCreate) -> None:
    logger.debug("request: POST /api/anonymous-post")
