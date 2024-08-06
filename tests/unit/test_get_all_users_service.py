from app.repositories.interfaces.user_repository_interface import IUserRepository
from app.services.users import list_user_service


def test_get_all_users(mock_user_repository_with_data: IUserRepository):
    users = list_user_service.execute(mock_user_repository_with_data)
    assert type(users) is list
    assert len(users) == 2
