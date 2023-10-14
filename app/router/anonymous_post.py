import logging

from fastapi import APIRouter

router = APIRouter()

logger = logging.getLogger("gohan_map")


@router.get("/api/anonymous-post")
async def list_anonymous_post() -> None:
    logger.debug("request: GET /api/anonymous-post")


@router.post("/api/anonymous-post")
async def create_anonymous_post() -> None:
    logger.debug("request: POST /api/anonymous-post")
