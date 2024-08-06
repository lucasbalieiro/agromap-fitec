from pydantic import UUID4, BaseModel, EmailStr
from app.schemas.role import ShowRole


class BaseUser(BaseModel):
    name: str
    email: EmailStr


class CreateUser(BaseUser):
    password: str
    role_id: UUID4

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "AgroMap User",
                    "email": "user@agromap.com.br",
                    "password": "1234567890!Ab",
                    "role_id": "789aca5d-c689-4f28-9f1f-1a71daf7248e"
                }
            ]
        }
    }


class ShowUser(BaseUser):
    id: UUID4
    role: ShowRole

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "880d84b4-3276-4d7f-9d79-20a71301b2d0",
                    "name": "AgroMap User",
                    "email": "user@agromap.com.br",
                }
            ]
        },
        "from_attributes": True,
    }
