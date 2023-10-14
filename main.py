import logging

from fastapi import FastAPI

from app.utils.logger import init_logger

# 初期化
init_logger()

logger = logging.getLogger("gohan_map")
app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    logger.debug("request: /")
    return {"Hello": "World"}
