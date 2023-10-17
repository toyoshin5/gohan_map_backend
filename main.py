import firebase_admin
from fastapi import FastAPI
from firebase_admin import credentials

from app.db import get_db
from app.router import anonymous_post

## 初期化 ##
firebase_admin.initialize_app(credentials.Certificate("./firebaseAdminKey.json"))

app = FastAPI()

app.include_router(anonymous_post.router)
