from pydantic import BaseModel


class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "Bearer"


class AuthRequest(BaseModel):
    username: str
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "user@agromap.com.br",
                    "password": "1234567890!Ab",
                }
            ]
        }
    }
