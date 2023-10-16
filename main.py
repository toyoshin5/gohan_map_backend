import firebase_admin
from fastapi import FastAPI
from firebase_admin import credentials

from app.db import get_db
from app.router import anonymous_post
from app.utils.logger import init_logger

## 初期化 ##
init_logger()
firebase_admin.initialize_app(credentials.Certificate("./firebaseAdminKey.json"))

app = FastAPI()

app.include_router(anonymous_post.router)
