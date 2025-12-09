from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, constr

router = APIRouter(prefix="/api/users")


# Request model
class CreateUserRequest(BaseModel):
    email: EmailStr
    password: constr(min_length=1)
    full_name: constr(min_length=1)


# Response model
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str


# Mock DB (mutable list kept in memory)
mock_users_db = [
    {"id": 1, "email": "test@example.com", "full_name": "Test User"},
]


def reset_mock_db():
    # Reset DB in-place so server restart is not required
    mock_users_db[:] = [
        {"id": 1, "email": "test@example.com", "full_name": "Test User"},
    ]
    return mock_users_db


@router.post("/reset")
def reset_users():
    reset_mock_db()
    return {"status": "ok"}


@router.get("/", response_model=list[UserResponse])
def list_users():
    return mock_users_db


@router.post("/", response_model=UserResponse)
def create_user(req: CreateUserRequest):
    # Duplicate email check
    for user in mock_users_db:
        if user["email"] == req.email:
            raise HTTPException(status_code=409, detail="User already exists")

    new_user = {
        "id": len(mock_users_db) + 1,
        "email": req.email,
        "full_name": req.full_name,
    }

    mock_users_db.append(new_user)
    return new_user
