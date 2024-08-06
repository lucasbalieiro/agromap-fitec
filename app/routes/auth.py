from fastapi import APIRouter, Depends, HTTPException, Request, status

from app.error.business_logic_error import handle_exception
from app.repositories.dependencies import get_user_repository
from app.schemas.auth import AuthRequest, AuthResponse
from app.services.auth import (
    authenticate_user_service
)

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={
        404: {
            "description": "Not found",
            "content": {"application/json": {"example": {"detail": "Not found"}}},
        },
        401: {
            "description": "Unauthorized",
            "content": {"application/json": {"example": {"detail": "Unauthorized"}}},
        },
        500: {
            "description": "Internal Server Error",
            "content": {
                "application/json": {"example": {"detail": "Internal Server Error"}}
            },
        },
        409: {
            "description": "Conflict",
            "content": {"application/json": {"example": {"detail": "Conflict"}}},
        },
    },
)


@router.post(
    "/login",
    summary="Login",
    status_code=status.HTTP_200_OK,
    response_model=AuthResponse,
)
async def login(
    payload: AuthRequest,
    user_repository=Depends(get_user_repository),
):
    try:
        token = authenticate_user_service.execute(
            payload,
            user_repository,
        )
        return token
    except Exception as e:
        error = handle_exception(e)
        raise HTTPException(status_code=error.status_code, detail=error.message)
