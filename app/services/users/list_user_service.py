from app.models.user import User
from app.repositories.interfaces.user_repository_interface import IUserRepository


def execute(
    user_repository: IUserRepository,
) -> list[User]:
    users = user_repository.get_users()
    return users
