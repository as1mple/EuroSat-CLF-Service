from pydantic import BaseModel


class Message(BaseModel):
    message: str


class ResponseModel(BaseModel):
    predict: str
