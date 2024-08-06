from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.services.security.tokens import decode_access_token


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if not credentials.scheme == "Bearer":
            raise HTTPException(
                status_code=403, detail="Invalid authentication scheme."
            )

        if credentials.credentials.startswith("INTERNAL"):
            valid_token = self.verify_internal_token(credentials.credentials)
            if not valid_token:
                raise HTTPException(
                    status_code=403, detail="Invalid or expired internal token."
                )
            return credentials.credentials

        if not self.verify_jwt(credentials.credentials):
            raise HTTPException(status_code=403, detail="Invalid or expired token.")
        return credentials.credentials

    def verify_jwt(self, jwtoken: str) -> bool:
        try:
            payload = decode_access_token(jwtoken)
            if payload:
                return True
            return False
        except Exception:
            return False