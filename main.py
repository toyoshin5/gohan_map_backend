from fastapi import FastAPI

from app.db import get_db
from app.router import anonymous_post
from app.utils.logger import init_logger

# 初期化
init_logger()

app = FastAPI()
session = get_db()

app.include_router(anonymous_post.router)
