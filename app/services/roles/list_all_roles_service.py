from app.repositories.interfaces.role_repository_interface import IRoleRepository


def execute(role_repository: IRoleRepository):
    roles = role_repository.get_all_roles()
    return roles