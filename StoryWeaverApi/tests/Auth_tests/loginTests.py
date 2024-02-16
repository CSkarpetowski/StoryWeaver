import pytest
from fastapi.testclient import TestClient

from src.auth.models import User
from src.main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def test_user():
    return User(username="TestUser", email="test@test.com", password="test")


def test_create_user(client, test_user):
    response = client.post("/auth/signup", json=test_user.dict())
    assert response.status_code == 201
    assert response.json() == "Singed up successfully"


def test_login_with_incorrect_password(client, test_user):
    response = client.post("/auth/login", data={"username": test_user.username, "password": "wrong_password"})
    assert response.status_code == 401
    assert "detail" in response.json()
    assert response.json()["detail"] == "Invalid username or password"


def test_login_with_non_existent_username(client):
    response = client.post("/auth/login", data={"username": "non_existent_username", "password": "test"})
    assert response.status_code == 401
    assert "detail" in response.json()
    assert response.json()["detail"] == "Invalid username or password"


def test_login_with_correct_credentials(client, test_user):
    response = client.post("/auth/login", data={"username": test_user.username, "password": test_user.password})
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_delete_account(client, test_user):
    # Login
    response = client.post("/auth/login", data={"username": test_user.username, "password": test_user.password})
    assert response.status_code == 200
    assert response.json() is not None

    # Get the token from the login response
    token = response.json().get('access_token')

    # Delete account
    headers = {'Authorization': f'Bearer {token}'}
    response = client.delete(f"/authorized/delete-account/{test_user.email}", headers=headers)
    assert response.status_code == 204

    # Try to log in again
    response = client.post("/auth/login", data={"username": test_user.username, "password": test_user.password})
    assert response.status_code != 200
