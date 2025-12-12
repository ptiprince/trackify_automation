from fastapi.testclient import TestClient
from api_server.main import app


class AuthAPI:
    """
    Auth API wrapper for tests.
    Uses internal FastAPI TestClient — no external server required.
    """

    def __init__(self):
        # Internal in-memory FastAPI test client
        self.client = TestClient(app)

    def login(self, email: str, password: str):
        payload = {
            "email": email,
            "password": password,
        }
        # Direct call to FastAPI /api/login route
        return self.client.post("/api/login", json=payload)
