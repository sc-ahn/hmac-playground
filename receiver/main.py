from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from common.helper import hmac
from common.schema import MessageForValidation

app = FastAPI()

@app.get("/", include_in_schema=False)
async def root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "Receiver APP",
        }
    )

@app.post("/verify")
async def verify(body: MessageForValidation):
    if hmac.verify(body.message, body.digest):
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "OK",
            }
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": "NG",
            }
        )
