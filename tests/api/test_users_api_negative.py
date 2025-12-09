from fastapi.testclient import TestClient
from api_server.main import app

client = TestClient(app)


def reset_users_state() -> None:
    # Reset mock DB on the server side
    resp = client.post("/api/users/reset")
    assert resp.status_code == 200


def test_create_user_duplicate_email():
    # Start from clean state
    reset_users_state()

    payload = {
        "email": "dup@example.com",
        "password": "123456",
        "full_name": "Dup User",
    }

    # First create is ok
    resp1 = client.post("/api/users/", json=payload)
    assert resp1.status_code == 200

    # Second create with same email must fail with 409
    resp2 = client.post("/api/users/", json=payload)
    assert resp2.status_code == 409
    assert resp2.json()["detail"] == "User already exists"


def test_create_user_invalid_payload():
    # Start from clean state
    reset_users_state()

    # Empty fields violate pydantic validators
    payload = {
        "email": "not-an-email",
        "password": "",
        "full_name": "",
    }

    resp = client.post("/api/users/", json=payload)
    assert resp.status_code == 422

