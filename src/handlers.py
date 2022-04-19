import sys
import json

import cv2
import numpy as np
from loguru import logger
from fastapi import APIRouter, File
from fastapi.responses import JSONResponse

from src.modules.inference import Model
from src.modules.data_models import Message, ResponseModel

PATH_TO_MODEL = "resources/model.torch"
PATH_TO_DECODER = "resources/decoder.json"

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
router.model = Model(
    path_to_model=PATH_TO_MODEL, transform=Model.transforms_valid()
)

with open(PATH_TO_DECODER) as jsonFile:
    router.decoder = {int(k): v for k, v in json.load(jsonFile).items()}

DEFAULT_RESPONSES = {500: {"model": Message}}

logger.info("FASTAPI RUN")


@router.get("/api/v1/status", response_model=Message, responses={**DEFAULT_RESPONSES})
def get_satus():
    logger.info("Health check")
    return Message(message="Success")


@router.post("/api/v1/files/", response_model=ResponseModel)
async def predict(file: bytes = File(...)):
    logger.info("Run predict")
    try:
        np_array = np.fromstring(file, np.uint8)
        image = cv2.imdecode(np_array, cv2.COLOR_BGR2RGB)
        logger.info(f"image.shape = {image.shape}")
        logger.info("UPLOAD Success!!!")

        result = router.model(image)
        forecast = router.decoder[result]

        return ResponseModel(predict=forecast)
    except AttributeError:
        mes = "wrong format"
        logger.exception(mes)
        return JSONResponse(status_code=500, content={"message": mes})
