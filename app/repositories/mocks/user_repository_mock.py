import uuid
from uuid import UUID

from app.models.user import User
from app.repositories.interfaces.user_repository_interface import IUserRepository
from app.schemas.user import CreateUser


class UserRepositoryMock(IUserRepository):
    def __init__(self):
        self.db: list[User] = []

    def get_by_email(self, email: str) -> User:
        for user in self.db:
            if user.email == email:
                return user
        return None

    def insert(self, payload: CreateUser) -> User:
        new_user = User(
            id=uuid.uuid4(),
            name=payload.name,
            email=payload.email,
            password=payload.password,
            department_id=payload.department_id,
            role_id=payload.role_id,
            status=True,
        )
        self.db.append(new_user)
        return new_user

    def get_by_name(self, name: str) -> User:
        for user in self.db:
            if user.name == name:
                return user
        return None

    def get_users(self) -> list[User]:
        return self.db

    def get_by_id(self, user_id: UUID) -> User:
        for user in self.db:
            if user.id == str(user_id):
                return user
        return None