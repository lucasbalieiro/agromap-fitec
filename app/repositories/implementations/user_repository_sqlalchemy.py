from uuid import UUID

from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.interfaces.user_repository_interface import IUserRepository
from app.schemas.user import CreateUser


class UserRepositorySQLAlchemy(IUserRepository):
    def __init__(self, db: Session):
        self.db = db

    def insert(self, payload: CreateUser):
        user = User()
        user.name = payload.name
        user.email = payload.email
        user.password = payload.password
        user.role_id = payload.role_id
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def get_by_name(self, name: str) -> User:
        return self.db.query(User).join(User.role).filter(User.name == name).first()

    def get_users(self) -> list[User]:
        users = self.db.query(User).join(User.role).all()
        return users

    def get_by_id(self, user_id: UUID) -> User:
        return self.db.query(User).filter(User.id == user_id).first()