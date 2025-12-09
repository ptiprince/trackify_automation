from api.auth_api import AuthAPI
from config import Config


def test_login_api_valid():
    client = AuthAPI()

    resp = client.login(
        email=Config.VALID_EMAIL,
        password=Config.VALID_PASSWORD,
    )

    assert resp.status_code == 200
    assert resp.json is not None
