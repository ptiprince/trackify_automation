from fastapi.testclient import TestClient
from api_server.main import app

client = TestClient(app)


def reset_users_state() -> None:
    # Reset mock DB on the server side
    resp = client.post("/api/users/reset")
    assert resp.status_code == 200


def test_list_users():
    # Ensure clean state
    reset_users_state()

    resp = client.get("/api/users/")
    assert resp.status_code == 200

    data = resp.json()
    assert isinstance(data, list)
    assert len(data) == 1

    user = data[0]
    assert user["email"] == "test@example.com"
    assert user["full_name"] == "Test User"
    assert "id" in user


def test_create_user():
    # Ensure clean state
    reset_users_state()

    payload = {
        "email": "auto_user@example.com",
        "password": "123456",
        "full_name": "Auto User",
    }

    resp = client.post("/api/users/", json=payload)
    assert resp.status_code == 200

    data = resp.json()
    assert data["email"] == "auto_user@example.com"
    assert data["full_name"] == "Auto User"
    assert "id" in data
    assert data["id"] == 2  # after reset there is exactly one default user
