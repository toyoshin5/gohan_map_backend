from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.schema.swipe as swipe_schema
from app.db import get_db
from app.dependency import get_current_user
from app.types.fireabase import UserInfo
from app.utils.logger import get_logger

router = APIRouter()

logger = get_logger()


@router.get("/api/swipe/anonymous-post", response_model=list[swipe_schema.SwipePost])
async def list_anonymous_post(
    q: swipe_schema.SwipePostRequest = Depends(),
    db: Session = Depends(get_db),
    cred: UserInfo = Depends(get_current_user),
) -> list[swipe_schema.SwipePost]:
    logger.debug("request: GET /api/swipe/anonymous-post")
    uid = cred["uid"]

    return []
