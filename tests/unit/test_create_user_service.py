import uuid

from app.error.business_logic_error import BusinessLogicError, ErrorType
from app.repositories import dependencies
from app.schemas.user import CreateUser
from app.services.security.password import compare_passwords
from app.services.users import create_user_service


def test_user_create_sevice_successfully(
    user_repository_mock=dependencies.get_user_repository_mock(),
    role_repository_mock=dependencies.get_role_repository_mock(),
):
    pwd = "123456!Ab0"
    payload = CreateUser(
        name="Test.User",
        email="test@test.com",
        password=pwd,
        role_id=uuid.UUID("789aca5d-c689-4f28-9f1f-1a71daf7248e"),
    )

    created_user = create_user_service.execute(
        payload,
        role_repository_mock,
        user_repository_mock,
    )

    assert created_user.name == payload.name
    assert created_user.email == payload.email
    assert created_user.role_id == payload.role_id
    assert created_user.id is not None
    assert compare_passwords(pwd, created_user.password) is True


def test_create_user_existent_email(
    mock_user_repository_with_data,
    role_repository_mock=dependencies.get_role_repository_mock(),
):
    payload = CreateUser(
        name="Test.User",
        email="user@agromap.com.br",
        password="123456!Ab0",
        role_id="789aca5d-c689-4f28-9f1f-1a71daf7248e",
    )
    try:
        create_user_service.execute(
            payload,
            role_repository_mock,
            mock_user_repository_with_data,
        )
    except Exception as e:
        assert isinstance(e, BusinessLogicError)
        assert e.error_type == ErrorType.DUPLICATED_ITEM
        assert e.message == "User already exists with this email"


def test_create_user_unexistent_role(
    mock_user_repository_with_data,
    role_repository_mock=dependencies.get_role_repository_mock(),
):
    payload = CreateUser(
        name="Test.User",
        email="user@test.com",
        password="123456!Ab0",
        role_id="789aca5d-c689-4f28-9f1f-1a71daf7248a",
    )

    try:
        create_user_service.execute(
            payload,
            role_repository_mock,
            mock_user_repository_with_data,
        )
    except Exception as e:
        assert isinstance(e, BusinessLogicError)
        assert e.error_type == ErrorType.INVALID_INPUT
        assert e.message == "Role does not exist"
