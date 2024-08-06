from uuid import UUID

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status

from app.error.business_logic_error import handle_exception
from app.repositories import dependencies
from app.repositories.interfaces.role_repository_interface import IRoleRepository
from app.repositories.interfaces.user_repository_interface import IUserRepository
from app.schemas.user import CreateUser, ShowUser       
from app.services.auth.auth_bearer import JWTBearer
from app.services.users import (
    create_user_service,
    get_user_by_id_service,
    list_user_service
)

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={
        404: {
            "description": "Not found",
            "content": {"application/json": {"example": {"detail": "Not found"}}},
        },
        409: {
            "description": "Conflict",
            "content": {"application/json": {"example": {"detail": "Conflict"}}},
        },
        500: {
            "description": "Internal Server Error",
            "content": {
                "application/json": {"example": {"detail": "Internal Server Error"}}
            },
        },
        403: {
            "description": "Forbidden",
            "content": {"application/json": {"example": {"detail": "Forbidden"}}},
        },
    },
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ShowUser,
    summary="Create a new user",
)
async def create_user(
    payload: CreateUser,
    role_repository: IRoleRepository = Depends(dependencies.get_role_repository),
    user_repository: IUserRepository = Depends(dependencies.get_user_repository),
):
    try:
        created_user = create_user_service.execute(
            payload,
            role_repository,
            user_repository,
        )
        return created_user

    except Exception as e:
        error = handle_exception(e)
        raise HTTPException(status_code=error.status_code, detail=error.message)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[ShowUser],
    summary="List ALL users",
    dependencies=[Depends(JWTBearer())]
)
def list_users(
    user_repository: IUserRepository = Depends(dependencies.get_user_repository),
):
    try:
        users = list_user_service.execute(
            user_repository,
        )

        return users
    except Exception as e:
        error = handle_exception(e)
        raise HTTPException(status_code=error.status_code, detail=error.message)


@router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=ShowUser,
    summary="Get specific user by id",
    dependencies=[Depends(JWTBearer())]
)
def get_user_by_id(
    user_id: UUID,
    user_respository: IUserRepository = Depends(dependencies.get_user_repository),
):
    try:
        user = get_user_by_id_service.execute(user_id, user_respository)
        return user
    except Exception as e:
        error = handle_exception(e)
        raise HTTPException(status_code=error.status_code, detail=error.message)

