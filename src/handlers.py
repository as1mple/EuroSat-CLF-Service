import sys

from fastapi import APIRouter
from loguru import logger

from src.modules.data_models import Message

logger.configure(
    handlers=[
        {"sink": sys.stderr, "level": "DEBUG"},
        dict(
            sink="logs/debug.log",
            format="{time} {level} {message}",
            level="DEBUG",
            rotation="1 weeks",
        ),
    ]
)
router = APIRouter()
logger.info("FASTAPI RUN")

DEFAULT_RESPONSES = {500: {"model": Message}}


@router.get("/api/v1/status", response_model=Message, responses={**DEFAULT_RESPONSES})
def get_satus():
    logger.info("Health check")
    return Message(message="Success")
