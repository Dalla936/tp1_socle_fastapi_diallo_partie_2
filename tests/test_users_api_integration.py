import json
from pathlib import Path

from fastapi.testclient import TestClient
import pytest
from app.api.dependencies import get_users_service
from app.factories.users_factory import UsersFactory
from app.main import app
from app.models.user_model import UserModel
from app.models.user_model_create import UserModelCreate
from app.repositories.users_repository_fake import FakeUsersRepository
from app.services.users_service import UsersService


@pytest.fixture
def client(tmp_path: Path):
    """Fixture qui crée un TestClient avec JSON temporaire"""
    # 1. Créer fichier JSON temporaire
    json_file = tmp_path / "users.json"
    json_file.write_text(
        json.dumps({
            "users": [
                {"id": 1, "login": "alice", "age": 20},
                {"id": 2, "login": "bob", "age": 22}
            ]
        }),
        encoding="utf-8"
    )
    
    # 2. Override la dépendance
    def override_users_service() -> UsersService:
        repo = FakeUsersRepository(factory=UsersFactory(), json_path=str(json_file))
        return UsersService(repository=repo)
    
    app.dependency_overrides[get_users_service] = override_users_service
    
    # 3. Fournir client
    yield TestClient(app)
    
    # 4. Cleanup
    app.dependency_overrides.clear()


@pytest.fixture
def payload():
    """Fixture qui fournit un payload valide"""
    return {"login": "charlie", "age": 25}

@pytest.fixture
def user_id():
    """Fixture qui fournit un ID utilisateur valide"""
    return 1


def test_should_list_users_given_existing_users(client: TestClient):
    # Arrange (fait par la fixture)
    # Act
    response = client.get("/users")

    # Assert (1 assertion métier)
    assert len(response.json()) == 2

def test_should_return_users_by_id_given(client: TestClient, user_id: int):
    # Arrange (fait par la fixture)

    # Act
    response = client.get(f"/users/{user_id}")

    # Assert
    assert response.status_code == 200
    assert response.json()["id"] == user_id


def test_should_insert_user_given_valid_payload(client: TestClient, payload: dict):
    # Arrange (fait par la fixture)

    # Act
    response = client.post("/users", json=payload)
    # Assert
    assert response.status_code == 201
    assert response.json()["login"] == payload["login"]
    assert response.json()["age"] == payload["age"]
