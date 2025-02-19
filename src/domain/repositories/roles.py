from .sqlalchemy_repository import SQLAlchemyRepository
from src.database.models import RolesORM


class RolesRepository(SQLAlchemyRepository):
    model = RolesORM


