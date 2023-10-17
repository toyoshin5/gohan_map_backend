from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.schema.anonymous_post as post_schema
from app.crud import anonymous_post
from app.db import get_db
from app.dependency import get_current_user
from app.types.fireabase import UserInfo
from app.utils.logger import get_logger

router = APIRouter()

logger = get_logger()


@router.get("/api/anonymous-post", response_model=list[post_schema.AnonymousPost])
async def list_anonymous_post(
    db: Session = Depends(get_db),
    cred: UserInfo = Depends(get_current_user),
) -> list[post_schema.AnonymousPost]:
    logger.debug("request: GET /api/anonymous-post")
    uid = cred["uid"]

    postModelList = anonymous_post.fetch_anonymous_post_by_uid(db, uid)
    postSchemaList: list[post_schema.AnonymousPost] = list(
        map(lambda x: post_schema.AnonymousPost.from_model(x), postModelList)
    )

    return postSchemaList


@router.post("/api/anonymous-post")
async def create_anonymous_post(post: post_schema.AnonymousPostCreate) -> None:
    logger.debug("request: POST /api/anonymous-post")
