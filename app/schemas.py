from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

class AIAnalyzeRequest(BaseModel):
    text: str


class AIAnalyzeResponse(BaseModel):
    summary: str
    keywords: list[str]
    sentiment: str
