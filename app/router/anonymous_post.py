import logging
from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials
from firebase_admin.auth import UserInfo
from sqlalchemy.orm import Session

import app.schema.anonymous_post as post_schema
from app.crud import anonymous_post
from app.db import get_db
from app.dependency import get_current_user

router = APIRouter()

logger = logging.getLogger("gohan_map")


@router.get("/api/anonymous-post", response_model=list[post_schema.AnonymousPost])
async def list_anonymous_post(
    db: Session = Depends(get_db),
    cred: UserInfo = Depends(get_current_user),
) -> list[post_schema.AnonymousPost]:
    logger.debug("request: GET /api/anonymous-post")
    uid: str = cred["uid"]

    posts = anonymous_post.fetch_anonymous_post_by_uid(db, uid)

    return [
        post_schema.AnonymousPost(
            id=1,
            userId=uid,
            googleMapShopId=uid,
            timelineId=1,
            star=1,
            imageURLList=["http://example.com"],
            createdAt="",
            updatedAt="",
        )
    ]


@router.post("/api/anonymous-post")
async def create_anonymous_post(post: post_schema.AnonymousPostCreate) -> None:
    logger.debug("request: POST /api/anonymous-post")
