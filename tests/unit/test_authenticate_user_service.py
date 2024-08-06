from app.error.business_logic_error import (
    BusinessLogicError,
    ErrorType,
)
from app.repositories.interfaces.user_repository_interface import IUserRepository
from app.schemas.auth import AuthRequest
from app.services.auth import authenticate_user_service


def test_user_authentication_successfully(
    mock_user_repository_with_data: IUserRepository,
):
    payload = AuthRequest(username="user@agromap.com.br", password="1234567890!Ab")
    sut = authenticate_user_service.execute(payload, mock_user_repository_with_data)
    assert sut is not None
    assert sut.access_token is not None
    assert sut.access_token != ""
    assert len(sut.access_token.split(".")) == 3
    assert sut.token_type == "Bearer"


def test_user_authentication_invalid_user(
    mock_user_repository_with_data: IUserRepository,
):
    payload = AuthRequest(username="invaliduser", password="1234567890!Ab")
    try:
        authenticate_user_service.execute(payload, mock_user_repository_with_data)
    except Exception as e:
        assert isinstance(e, BusinessLogicError)
        assert e.error_type == ErrorType.UNAUTHORIZED
        assert e.message == "Invalid Credentials"



def test_user_authetication_with_invalid_password(
    mock_user_repository_with_data: IUserRepository,
):
    payload = AuthRequest(username="user@agromap.com.br", password="123456")
    try:
        authenticate_user_service.execute(payload, mock_user_repository_with_data)
    except Exception as e:
        assert isinstance(e, BusinessLogicError)
        assert e.error_type == ErrorType.UNAUTHORIZED
        assert e.message == "Invalid Credentials"
