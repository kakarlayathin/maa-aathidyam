from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.main import app
import pytest

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_client():
    response = client.post(
        "/api/clients/",
        json={"name": "Test Client", "email": "test@example.com"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Client"
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_create_project():
    # First create a client
    client_resp = client.post(
        "/api/clients/",
        json={"name": "Test Client", "email": "test@example.com"},
    )
    client_id = client_resp.json()["id"]

    response = client.post(
        "/api/projects/",
        json={"name": "Test Project", "description": "A test project", "client_id": client_id},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Project"
    assert data["client_id"] == client_id

def test_create_task():
    # First create a client and project
    client_resp = client.post(
        "/api/clients/",
        json={"name": "Test Client", "email": "test@example.com"},
    )
    client_id = client_resp.json()["id"]
    
    project_resp = client.post(
        "/api/projects/",
        json={"name": "Test Project", "client_id": client_id},
    )
    project_id = project_resp.json()["id"]

    response = client.post(
        "/api/tasks/",
        json={"title": "Test Task", "description": "A test task", "project_id": project_id},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["project_id"] == project_id
    assert data["status"] == "backlog"
