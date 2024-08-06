from uuid import UUID

from app.error.business_logic_error import BusinessLogicError, ErrorType
from app.repositories.interfaces.user_repository_interface import IUserRepository


def execute(user_id: UUID, user_repository: IUserRepository):
    user = user_repository.get_by_id(user_id)

    if not user:
        raise BusinessLogicError("User not found", error_type=ErrorType.NOT_FOUND)

    return user
