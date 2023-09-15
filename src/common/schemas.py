from pydantic import BaseModel, Field

class Message(BaseModel):
    message: str = Field(..., max_length=100)
    key: str = Field(..., max_length=16)
    
class MessageDecrypt(BaseModel):
    message: str
    key: str = Field(..., max_length=16)