from fastapi import FastAPI
from common.helper import hmac
from common.schema import MessageForValidation

app = FastAPI()

@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Receiver APP"}

@app.post("/verify")
async def verify(body: MessageForValidation):
    if hmac.verify(body.message, body.digest):
        return {"message": "OK"}
    else:
        return {"message": "NG"}
