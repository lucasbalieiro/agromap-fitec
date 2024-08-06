import uuid

from app.repositories.interfaces.user_repository_interface import IUserRepository


def set_user_session_id(user_id: uuid.UUID, user_repository: IUserRepository):
    session_id = uuid.uuid4()
    user_repository.set_session_id(user_id, session_id)
    return session_id


def clear_user_session_id(user_id: uuid.UUID, user_repository: IUserRepository):
    user_repository.clear_session_id(user_id)
