import requests
from dataclasses import dataclass
from typing import Any, Dict, Optional

from config import Config


@dataclass
class ApiResponse:
    status_code: int
    json: Optional[Dict[str, Any]]
    raw: Any


class ApiClient:
    """
    Base HTTP client for Trackify API.
    Initially used for Auth module, but can be extended for other API modules.
    """

    def __init__(
        self,
        base_url: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> None:
        # If Config.API_BASE_URL exists, use it. Otherwise fallback to UI BASE_URL.
        self.base_url = (base_url or getattr(Config, "API_BASE_URL", Config.BASE_URL)).rstrip("/")
        # Default timeout for HTTP requests (seconds).
        self.timeout = timeout or getattr(Config, "API_DEFAULT_TIMEOUT", 5)

    def _url(self, path: str) -> str:
        """Build full endpoint URL."""
        return f"{self.base_url}/{path.lstrip('/')}"

    def _wrap_response(self, resp: requests.Response) -> ApiResponse:
        """Normalize all responses into a single unified structure."""
        try:
            body = resp.json()
        except ValueError:
            body = None

        return ApiResponse(
            status_code=resp.status_code,
            json=body,
            raw=resp,
        )

    def get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ApiResponse:
        resp = requests.get(
            self._url(path),
            params=params,
            headers=headers,
            timeout=self.timeout,
        )
        return self._wrap_response(resp)

    def post(
        self,
        path: str,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> ApiResponse:
        resp = requests.post(
            self._url(path),
            json=json,
            headers=headers,
            timeout=self.timeout,
        )
        return self._wrap_response(resp)
