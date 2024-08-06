from fastapi import APIRouter, Depends, HTTPException, status

from app.error.business_logic_error import handle_exception
from app.repositories import dependencies
from app.repositories.interfaces.role_repository_interface import IRoleRepository
from app.schemas.role import ShowRole
from app.services.auth.auth_bearer import JWTBearer
from app.services.roles import list_all_roles_service

router = APIRouter(
    prefix="/roles",
    tags=["roles"],
    dependencies=[Depends(JWTBearer())],
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


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[ShowRole],
    summary="List all roles",
)
def list_roles(
    role_repository: IRoleRepository = Depends(dependencies.get_role_repository),
):
    try:
        roles = list_all_roles_service.execute(role_repository)
        return roles
    except Exception as e:
        error = handle_exception(e)
        raise HTTPException(status_code=error.status_code, detail=error.message)
