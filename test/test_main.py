from fastapi.testclient import TestClient
from src.main import api

client = TestClient(api)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Book Management System"}

def test_add_book():
    response = client.post("/book", json={
        "id": 1,
        "name": "Book 1",
        "description": "A test book",
        "isAvailable": True
    })
    assert response.status_code == 200
    assert response.json()[0]["name"] == "Book 1"

def test_get_books():
    response = client.get("/book")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_update_book():
    response = client.put("/book/1", json={
        "id": 1,
        "name": "Book 1 Updated",
        "description": "Updated description",
        "isAvailable": False
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Book 1 Updated"

def test_delete_book():
    response = client.delete("/book/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Book 1 Updated"
