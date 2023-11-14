from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from aiohttp import ClientSession
from common.helper import hmac, inject_timestamp
from common.schema import Message, MessageForValidation

app = FastAPI()

@app.get("/", include_in_schema=False)
async def root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "Hello World",
        },
    )

@app.post("/generate")
async def generate(body: Message):
    message = inject_timestamp(body.message)
    digest = hmac.generate(message)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "digest": digest,
            "message": message,
        },
    )

@app.post("/verify")
async def verify(body: MessageForValidation):
    async with ClientSession() as session:
        async with session.post(
            "http://hmac-receiver:8000/verify",
            json={
                "message": body.message,
                "digest": body.digest,
            }
        ) as resp:
            return await resp.json()
