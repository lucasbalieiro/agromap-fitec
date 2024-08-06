from datetime import datetime, timedelta

from jose import ExpiredSignatureError, jwt

from app.config.environment import get_settings
from app.error.business_logic_error import BusinessLogicError, ErrorType


def create_access_token(payload: dict):
    settings = get_settings()
    to_encode = payload.copy()
    to_encode.update(
        {
            "exp": datetime.utcnow()
            + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES),
        }
    )
    encoded_jwt = jwt.encode(
        to_encode,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )
    return encoded_jwt


def decode_access_token(token: str):

    try:
        settings = get_settings()
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM],
        )
        return payload
    except ExpiredSignatureError:
        raise BusinessLogicError(
            "Invalid session token", error_type=ErrorType.UNAUTHORIZED
        )
