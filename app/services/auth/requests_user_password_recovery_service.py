from app.error.business_logic_error import BusinessLogicError, ErrorType
from app.repositories.interfaces.user_repository_interface import IUserRepository
from app.services.security.password import check_username_format


def execute(payload: str, user_repository: IUserRepository) -> None:
    check_username_format(payload)

    user_exists = user_repository.get_by_name(payload)
    if not user_exists:
        raise BusinessLogicError("The user does not exists", ErrorType.NOT_FOUND)

    user_repository.set_user_recovery_status(user_exists.id, True)
