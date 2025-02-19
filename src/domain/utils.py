from .repositories.roles import RolesRepository


async def create_roles(repository: RolesRepository = RolesRepository()) -> None:
    await repository.insert_many(
        data=[
            {"name": "user"},
            {"name": "admin"},
            {"name": "staff"},
        ]
    )
