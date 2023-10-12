from fastapi import FastAPI
import logging

from app.utils.logger import init_logger

# 初期化
init_logger()

logger = logging.getLogger("gohan_map")
app = FastAPI()


@app.get("/")
def read_root():
    logger.debug("request: /")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    logger.debug(f"request: /items/{item_id}")
    return {"item_id": item_id, "q": q}
