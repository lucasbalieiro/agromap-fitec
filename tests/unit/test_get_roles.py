from app.repositories.interfaces.role_repository_interface import IRoleRepository
from app.services.roles import list_all_roles_service


def test_get_all_roles(mock_role_repository_with_data: IRoleRepository):
    roles = list_all_roles_service.execute(mock_role_repository_with_data)

    assert type(roles) is list
    assert len(roles) == 2
