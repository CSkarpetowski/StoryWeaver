import pytest
from fastapi.testclient import TestClient
from src.main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def test_user():
    return {"username": "test", "email": "test@test.com", "password": "test"}


def test_create_user(client, test_user):
    response = client.post("/auth/signup", json=test_user)
    assert response.status_code == 200
    assert response.json() == "Singed up successfully"


def test_login(client, test_user):
    response = client.post("/auth/login", json={"email": test_user["email"], "password": test_user["password"]})
    assert response.status_code == 200
    assert response.json() is not None

def test_user_delete(client, test_user):
    response = client.post(f"/authorized/logout{test_user['email']}")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted"}