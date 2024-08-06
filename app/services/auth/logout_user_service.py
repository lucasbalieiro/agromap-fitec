from app.error.business_logic_error import BusinessLogicError, ErrorType
from app.repositories.interfaces.user_repository_interface import IUserRepository
from app.services.security import sessions, tokens


def execute(payload: str, user_repository: IUserRepository):
    decoded_token = tokens.decode_access_token(payload)
    print(decoded_token)
    if not decoded_token:
        raise BusinessLogicError("Invalid token", error_type=ErrorType.UNAUTHORIZED)
    user_session = user_repository.get_by_session_id(decoded_token["session_id"])

    if not user_session:
        raise BusinessLogicError("Invalid session", error_type=ErrorType.UNAUTHORIZED)

    sessions.clear_user_session_id(user_session.id, user_repository)
