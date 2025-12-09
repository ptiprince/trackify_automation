from typing import Optional, Dict, Any

from api.api_client import ApiClient
from config import Config


class AuthAPI(ApiClient):
    """
    High-level wrapper for Auth endpoints.
    Provides login() method for tests.
    """

    def __init__(self):
        # Uses API base URL if defined, otherwise falls back to Config defaults
        super().__init__(base_url=Config.API_BASE_URL)

    def login(self, email: str, password: str):
        payload = {
            "email": email,
            "password": password
        }
        return self.post("/login", json=payload)
