from app.error.business_logic_error import (
    BusinessLogicError,
    ErrorType
)
from app.repositories.interfaces.user_repository_interface import IUserRepository
from app.schemas.auth import AuthRequest, AuthResponse
from app.services.security.password import compare_passwords
from app.services.security.tokens import create_access_token


def execute(payload: AuthRequest, user_repository: IUserRepository) -> AuthResponse:
    user = user_repository.get_by_email(payload.username)

    if not user:
        raise BusinessLogicError(
            "Invalid Credentials", error_type=ErrorType.UNAUTHORIZED
        )
    valid_password = compare_passwords(payload.password, user.password)
    if not valid_password:
        raise BusinessLogicError(
            "Invalid Credentials",
            error_type=ErrorType.UNAUTHORIZED,
        )

    token = create_access_token(
        {"sub": user.name, "role": user.role.name}
    )
    
    return AuthResponse(access_token=token)
