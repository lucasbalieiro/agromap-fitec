import uuid
from abc import ABC, abstractmethod

from app.models.role import Role


class IRoleRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: uuid):
        pass

    @abstractmethod
    def get_all_roles(self) -> list[Role]:
        pass
