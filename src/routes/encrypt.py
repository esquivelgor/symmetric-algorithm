from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from src.algorithms.encrypt import encrypt_message
from src.common.schemas import Message
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.post("/encrypt", response_model = dict, tags=["encrypt"])
async def encrypt(body: Message = Body()):
    
    binary_array_result, base64_result  = encrypt_message(plain_text=body.message, key=body.key)
    
    response = {
        "binary_encrypted": binary_array_result,
        "base64_encrypted": base64_result
    }

    return JSONResponse(
        content = jsonable_encoder(response),
        status_code = status.HTTP_200_OK
    )