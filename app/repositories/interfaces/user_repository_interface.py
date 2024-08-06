from abc import ABC, abstractmethod
from uuid import UUID

from app.models.user import User
from app.schemas.user import CreateUser


class IUserRepository(ABC):
    @abstractmethod
    def insert(self, payload: CreateUser) -> User:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> User:
        pass

    @abstractmethod
    def get_users(self) -> list[User]:
        pass

    @abstractmethod
    def get_by_id(self, user_id: UUID) -> User:
        pass