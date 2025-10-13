# tests/test_tasks.py
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine
from app import models

# Create a test client
client = TestClient(app)


# Use a fresh database for tests
@pytest.fixture(autouse=True)
def setup_database():
    """Create tables before each test and drop them after."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_create_task():
    response = client.post(
        "/tasks/",
        json={"title": "Test Task", "description": "Test description"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test description"
    assert data["completed"] is False
    assert "id" in data


def test_read_tasks():
    # Create tasks first
    client.post("/tasks/", json={"title": "Task 1"})
    client.post("/tasks/", json={"title": "Task 2"})

    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["title"] == "Task 1"
    assert data[1]["title"] == "Task 2"


def test_read_single_task():
    res = client.post("/tasks/", json={"title": "Single Task"})
    task_id = res.json()["id"]

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == "Single Task"


def test_update_task():
    res = client.post("/tasks/", json={"title": "Old Title"})
    task_id = res.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={"title": "New Title", "completed": True},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New Title"
    assert data["completed"] is True


def test_delete_task():
    res = client.post("/tasks/", json={"title": "To Delete"})
    task_id = res.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200

    # Verify deletion
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404
