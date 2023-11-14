from pydantic import BaseModel


class Message(BaseModel):
    message: str


class MessageForValidation(Message):
    digest: str
