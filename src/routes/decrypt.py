from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from src.algorithms.decrypt import decrypt_message
from src.common.schemas import MessageDecrypt
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.post("/decrypt", response_model = dict, tags=["decrypt"])
async def decrypt(body: MessageDecrypt = Body()):
    
    decrypted_in_binary_ascii, decrypted_plain_text  = decrypt_message(encrypted_message=body.message, key=body.key)
    
    response = {
        "decrypted_in_binary_ascii": decrypted_in_binary_ascii,
        "decrypted_plain_text": decrypted_plain_text
    }

    return JSONResponse(
        content = jsonable_encoder(response),
        status_code = status.HTTP_200_OK
    )