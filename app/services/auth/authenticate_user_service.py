from app.error.business_logic_error import (
    BusinessLogicError,
    ErrorType,
    LoginAttemptsExceeded,
)
from app.repositories.interfaces.user_repository_interface import IUserRepository
from app.schemas.auth import AuthRequest, AuthResponse
from app.services.security.password import compare_passwords
from app.services.security.sessions import clear_user_session_id, set_user_session_id
from app.services.security.tokens import create_access_token


def execute(payload: AuthRequest, user_repository: IUserRepository) -> AuthResponse:
    user = user_repository.get_by_name(payload.username)

    if not user:
        raise BusinessLogicError(
            "Invalid Credentials", error_type=ErrorType.UNAUTHORIZED
        )
    if not user.status:
        raise BusinessLogicError("User is inactive", error_type=ErrorType.UNAUTHORIZED)

    valid_password = compare_passwords(payload.password, user.password)
    if not valid_password:
        user = user_repository.set_login_attempts(user.id, user.login_attempts + 1)
        if user.login_attempts > 3:
            user_repository.set_user_status(user.id, False)
            user_repository.set_login_attempts(user.id, 0)
            raise BusinessLogicError(
                "Too many login attempts. User is now inactive",
                error_type=ErrorType.UNAUTHORIZED,
            )

        raise LoginAttemptsExceeded(
            "Invalid Credentials",
            error_type=ErrorType.UNAUTHORIZED,
            login_attempts=user.login_attempts,
        )

    if user.session_id:
        clear_user_session_id(user.id, user_repository)
        raise BusinessLogicError(
            "User already logged in. The concurrent session will be closed.",
            error_type=ErrorType.CONFLICT,
        )

    session_id = set_user_session_id(user.id, user_repository)
    token = create_access_token(
        {"sub": user.name, "role": user.role.name, "session_id": str(session_id)}
    )
    user_repository.set_login_attempts(user.id, 0)
    return AuthResponse(access_token=token)
