from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/api")

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    message: str
    token: str | None = None

@router.post("/login", response_model=LoginResponse)
def login(req: LoginRequest):
    if req.email == "test@example.com" and req.password == "123456":
        return LoginResponse(
            message="Login successful",
            token="mock-token-123"
        )

    raise HTTPException(
        status_code=401,
        detail="Invalid credentials"
    )
