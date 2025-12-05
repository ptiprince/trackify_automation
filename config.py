# Global configuration for Trackify Automation

class Config:
    # Base URL for the web application
    BASE_URL = "http://127.0.0.1:5500"

    # Browser settings
    HEADLESS = False     # Run browser with UI (True = headless)
    SLOW_MO = 300        # Slow motion for debugging

    # Default credentials for tests
    VALID_EMAIL = "test@example.com"
    VALID_PASSWORD = "123456"

    INVALID_EMAIL = "wrong@example.com"
    INVALID_PASSWORD = "wrongpass"

    # Timeouts
    DEFAULT_TIMEOUT = 2000  # milliseconds
