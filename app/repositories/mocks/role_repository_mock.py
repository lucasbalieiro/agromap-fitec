import uuid

from app.models.role import Role
from app.repositories.interfaces.role_repository_interface import IRoleRepository

_initial_roles = [
    Role(id=uuid.UUID("789aca5d-c689-4f28-9f1f-1a71daf7248e"), name="Administrator"),
    Role(id=uuid.UUID("48675261-8b91-4b55-8ac4-bb407f5774d7"), name="Operator")
]


class RoleRepositoryMock(IRoleRepository):
    def __init__(self):
        self.db = _initial_roles

    def get_by_id(self, id: uuid.UUID):
        for role in self.db:
            if role.id == id:
                return role
        return None

    def get_all_roles(self) -> list[Role]:
        return self.db
