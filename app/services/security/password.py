from passlib.context import CryptContext

from app.error.business_logic_error import BusinessLogicError, ErrorType

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password) -> str:
    return pwd_context.hash(plain_password)


def compare_passwords(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def check_username_format(username: str) -> bool:
    """
    Returns True if the username provided is valid. \n
    Throws a BusinessLogicError instance if invalid
    """
    if len(username) < 2:
        raise BusinessLogicError(
            "Username must be at least 2 characters long",
            error_type=ErrorType.INVALID_INPUT,
        )
    if not username[0].isupper():
        raise BusinessLogicError(
            "Username must start with a capital letter",
            error_type=ErrorType.INVALID_INPUT,
        )
    if not username[username.find(".") + 1].isupper():
        raise BusinessLogicError(
            "Username must contain a dot and the first letter of the last name must be capitalized",
            error_type=ErrorType.INVALID_INPUT,
        )
    return True


def check_password_strength(password: str) -> bool:
    if len(password) < 10:
        raise BusinessLogicError(
            "Password must be at least 10 characters long",
            error_type=ErrorType.INVALID_INPUT,
        )
    if not any(char.isupper() for char in password):
        raise BusinessLogicError(
            "Password must contain at least one uppercase letter",
            error_type=ErrorType.INVALID_INPUT,
        )
    if not any(char.islower() for char in password):
        raise BusinessLogicError(
            "Password must contain at least one lowercase letter",
            error_type=ErrorType.INVALID_INPUT,
        )
    if not any(char.isdigit() for char in password):
        raise BusinessLogicError(
            "Password must contain at least one number",
            error_type=ErrorType.INVALID_INPUT,
        )
    if not any(char in "!@#$%^&*()-+?_=,<>/;:[]{}" for char in password):
        raise BusinessLogicError(
            "Password must contain at least one special character",
            error_type=ErrorType.INVALID_INPUT,
        )
    return True
