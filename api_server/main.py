from fastapi import FastAPI
from .auth import router as auth_router

app = FastAPI()

# Register Auth module routes
app.include_router(auth_router)



