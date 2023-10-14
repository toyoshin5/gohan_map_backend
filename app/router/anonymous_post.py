import logging

from fastapi import APIRouter

import app.schema.anonymous_post as post_schema

router = APIRouter()

logger = logging.getLogger("gohan_map")


@router.get("/api/anonymous-post", response_model=list[post_schema.AnonymousPost])
async def list_anonymous_post() -> list[post_schema.AnonymousPost]:
    logger.debug("request: GET /api/anonymous-post")
    return [
        post_schema.AnonymousPost(
            id=1,
            googleMapShopId="1",
            timelineId=1,
            star=1,
            imageURLList=["http://example.com"],
        )
    ]


@router.post("/api/anonymous-post")
async def create_anonymous_post(post: post_schema.AnonymousPostCreate) -> None:
    logger.debug("request: POST /api/anonymous-post")
