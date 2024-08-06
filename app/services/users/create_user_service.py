from app.error.business_logic_error import BusinessLogicError, ErrorType
from app.models.user import User
from app.repositories.interfaces.role_repository_interface import IRoleRepository
from app.repositories.interfaces.user_repository_interface import IUserRepository
from app.schemas.user import CreateUser
from app.services.security.password import (
    check_password_strength,
    hash_password,
)


def execute(
    payload: CreateUser,
    role_repository: IRoleRepository,
    user_repository: IUserRepository,
) -> User:
    email_already_taken = user_repository.get_by_email(payload.email)
    if email_already_taken:
        raise BusinessLogicError(
            "User already exists with this email", error_type=ErrorType.DUPLICATED_ITEM
        )

    role_exists = role_repository.get_by_id(payload.role_id)
    if not role_exists:
        raise BusinessLogicError(
            "Role does not exist", error_type=ErrorType.INVALID_INPUT
        )
    check_password_strength(payload.password)
    payload.password = hash_password(payload.password)

    user = user_repository.insert(payload)
    return user
