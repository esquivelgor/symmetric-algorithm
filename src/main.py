from fastapi import FastAPI

from src.routes import (
    encrypt
)

app = FastAPI(title="Symmetric Encryption API", version="0.0.1")

app.include_router(encrypt.router)

@app.get("/")
async def read_root():
    return {"Hello": "Welcome to Symmetric Encryption API, explore the docs at /docs."}
