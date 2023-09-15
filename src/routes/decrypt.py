from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from src.algorithms.decrypt import decrypt_message
from src.common.schemas import MessageDecrypt

router = APIRouter()


@router.post("/decrypt", response_model = dict, tags=["decrypt"])
async def decrypt(body: MessageDecrypt = Body()):
    
    decrypted_message = decrypt_message(encrypted_message=body.message, key=body.key)
    
    response = {
        "decrypted_message": decrypted_message
    }

    return JSONResponse(
        content = response,
        status_code = status.HTTP_200_OK
    )