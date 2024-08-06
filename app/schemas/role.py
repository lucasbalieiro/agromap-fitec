from uuid import UUID

from pydantic import BaseModel


class ShowRole(BaseModel):
    id: UUID
    name: str
