from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://127.0.0.1:8000",
    "null"
]

from src.routes import (
    encrypt, decrypt
)

app = FastAPI(title="Symmetric Encryption API", version="0.0.1")

app.include_router(encrypt.router)
app.include_router(decrypt.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods= ["*"],
    allow_headers= ["*"],
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to Symmetric Encryption API, explore the docs at /docs."}
            
# @app.get("/")
# async def read_root():
#     return {"Hello": "Welcome to Symmetric Encryption API, explore the docs at /docs."}
