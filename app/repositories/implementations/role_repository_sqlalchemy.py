import uuid

from sqlalchemy.orm import Session

from app.models.role import Role
from app.repositories.interfaces.role_repository_interface import IRoleRepository


class RoleRepositorySQLAlchemy(IRoleRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, id: uuid):
        return self.db.query(Role).filter(Role.id == id).first()

    def get_all_roles(self) -> list[Role]:
        return self.db.query(Role).all()
