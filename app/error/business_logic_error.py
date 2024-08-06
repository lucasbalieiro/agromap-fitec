from enum import Enum
from typing import Union

from pydantic import BaseModel

class ErrorType(Enum):
    UNKNOWN_ERROR = 500
    DUPLICATED_ITEM = 409
    INVALID_INPUT = 422
    UNAUTHORIZED = 401
    CONFLICT = 409
    NOT_FOUND = 404
    CONTENT_TOO_LARGE = 413


class BaseError(BaseModel):
    message: Union[str, dict]
    type_error: ErrorType
    status_code: int = 500

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.status_code = kwargs["type_error"].value


class BusinessLogicError(Exception):
    def __init__(self, message: str, error_type: ErrorType):
        super().__init__(message)
        self.error_type = error_type
        self.message = message


def handle_exception(e: Exception) -> BaseError:
    if isinstance(e, BusinessLogicError):
        return BaseError(message=e.message, type_error=e.error_type)

    return BaseError(
        message="Internal Server Error", type_error=ErrorType.UNKNOWN_ERROR
    )
