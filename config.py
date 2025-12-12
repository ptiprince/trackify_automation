# Global configuration for Trackify Automation

class Config:
    # Base URL for UI (your HTML mock)
    BASE_URL = "http://127.0.0.1:5500"

    # Base URL for API (used ONLY for relative paths inside TestClient)
    # No external server, no http://127.0.0.1:8000
    API_BASE_URL = "/api"

    # Browser settings
    HEADLESS = False
    SLOW_MO = 300  # Slow motion for debugging

    # Default credentials for tests
    VALID_EMAIL = "test@example.com"
    VALID_PASSWORD = "123456"

    INVALID_EMAIL = "wrong@example.com"
    INVALID_PASSWORD = "wrongpass"

    # Timeouts (milliseconds for UI, seconds for API client)
    DEFAULT_TIMEOUT = 2000
    API_DEFAULT_TIMEOUT = 5


