from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from src.algorithms.encrypt import encrypt_message
from src.schemas.encrypt import MessageEncrypt

router = APIRouter()


@router.post("/encrypt", response_model = dict, tags=["encrypt"])
async def login(body: MessageEncrypt = Body()):
    
    encrypted_message = encrypt_message(plain_text=body.message, key=body.key)
    
    response = {
        "message": encrypted_message
    }

    return JSONResponse(
        content = response,
        status_code = status.HTTP_200_OK
    )