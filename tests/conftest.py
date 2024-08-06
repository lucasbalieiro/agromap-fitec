from fastapi.testclient import TestClient
from pytest import fixture

from app.main import create_application
from app.models.role import Role
from app.models.user import User
from app.repositories.dependencies import (
    get_role_repository_mock,
    get_user_repository_mock,
)


@fixture(scope="module")
def test_app():
    app = create_application()
    with TestClient(app) as test_client:
        yield test_client

@fixture
def mock_user_repository_with_data(mock_user_repository=get_user_repository_mock()):
    admin_role = Role(
        id="789aca5d-c689-4f28-9f1f-1a71daf7248e",
        name="Administrator",
    )
    user = User(
        id="6ec03620-d39a-4ea9-939e-17535eb2c8ca",
        name="AgroMap User",
        email="user@agromap.com.br",
        password="$2b$12$YArdpXkgp3itGQda/cvVXeTxBQfOC5cIkOsiZjB4bIuh7iAyaMiR.",  # 1234567890!Ab
        role=admin_role,
    )
    user2 = User(
        id="d8c42e9b-098b-47ac-b888-9ed377ae5376",
        name="AgroMap User Dup",
        email="user_dup@agromap.com.br",
        password="$2b$12$YArdpXkgp3itGQda/cvVXeTxBQfOC5cIkOsiZjB4bIuh7iAyaMiR.",  # 1234567890!Ab
        role=admin_role,
    )
    mock_user_repository.db.append(user)
    mock_user_repository.db.append(user2)
    yield mock_user_repository
    mock_user_repository.db.clear()


@fixture
def mock_role_repository_with_data(mock_role_repository=get_role_repository_mock()):
    yield mock_role_repository