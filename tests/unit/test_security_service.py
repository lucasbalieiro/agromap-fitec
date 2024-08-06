import pytest

from app.error.business_logic_error import BusinessLogicError, ErrorType
from app.services.security.password import (
    check_password_strength,
    check_username_format,
    compare_passwords,
    hash_password,
)


def test_hash_password():
    hashed_password = hash_password("testpassword")
    assert hashed_password is not None
    assert len(hashed_password) > 0


def test_compare_passwords():
    plain_password = "testpassword"
    hashed_password = hash_password(plain_password)
    assert compare_passwords(plain_password, hashed_password) is True


def test_check_username_format():
    assert check_username_format("John.Doe") is True

    with pytest.raises(BusinessLogicError) as excinfo:
        check_username_format("A")
    assert excinfo.value.error_type == ErrorType.INVALID_INPUT

    with pytest.raises(BusinessLogicError) as excinfo:
        check_username_format("john.Doe")
    assert excinfo.value.error_type == ErrorType.INVALID_INPUT

    with pytest.raises(BusinessLogicError) as excinfo:
        check_username_format("John.doe")
    assert excinfo.value.error_type == ErrorType.INVALID_INPUT


def test_check_password_strength():
    assert check_password_strength("TestP@ssw0rd") is True

    with pytest.raises(BusinessLogicError) as excinfo:
        check_password_strength("Short1$")
    assert excinfo.value.error_type == ErrorType.INVALID_INPUT

    with pytest.raises(BusinessLogicError) as excinfo:
        check_password_strength("nopassword1$")
    assert excinfo.value.error_type == ErrorType.INVALID_INPUT

    with pytest.raises(BusinessLogicError) as excinfo:
        check_password_strength("NOPASSWORD1$")
    assert excinfo.value.error_type == ErrorType.INVALID_INPUT

    with pytest.raises(BusinessLogicError) as excinfo:
        check_password_strength("Password$withoutnumber")
    assert excinfo.value.error_type == ErrorType.INVALID_INPUT

    with pytest.raises(BusinessLogicError) as excinfo:
        check_password_strength("Password1234")
    assert excinfo.value.error_type == ErrorType.INVALID_INPUT
