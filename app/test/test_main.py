# tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app
from app.models import UserCreate

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "testuser", "email": "test@example.com"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"