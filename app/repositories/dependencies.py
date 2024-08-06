from fastapi import Depends
from sqlalchemy.orm import Session

from app.config.database import get_db

from app.repositories.implementations.role_repository_sqlalchemy import (
    RoleRepositorySQLAlchemy,
)

from app.repositories.mocks.role_repository_mock import RoleRepositoryMock

def get_role_repository(db: Session = Depends(get_db)):
    return RoleRepositorySQLAlchemy(db)

def get_role_repository_mock():
    return RoleRepositoryMock()
