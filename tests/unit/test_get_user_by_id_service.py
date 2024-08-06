import pytest

from app.error.business_logic_error import BusinessLogicError, ErrorType
from app.repositories.interfaces.user_repository_interface import IUserRepository
from app.services.users.get_user_by_id_service import execute


def test_get_user_by_id(mock_user_repository_with_data: IUserRepository):
    user_id = "6ec03620-d39a-4ea9-939e-17535eb2c8ca"
    sut = execute(user_id, mock_user_repository_with_data)
    assert sut.id == user_id


def test_get_inexistent_user(mock_user_repository_with_data: IUserRepository):
    with pytest.raises(BusinessLogicError) as execinfo:
        execute("inexistent_id", mock_user_repository_with_data)

    assert execinfo.value.error_type == ErrorType.NOT_FOUND
    assert execinfo.value.message == "User not found"
