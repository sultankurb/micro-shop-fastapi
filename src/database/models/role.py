from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, TYPE_CHECKING
from .association_tables import *
from sqlalchemy import String
from src.database import Base
if TYPE_CHECKING:
    from .users import UsersORM


class RolesORM(Base):
    __tablename__ = 'roles'
    name: Mapped[str] = mapped_column(String(length=40), unique=True, nullable=False)
    users: Mapped[List['UsersORM']] = relationship(
        'UsersORM',
        back_populates='role_rel',
        cascade='all, delete, delete-orphan',
        lazy='joined',
    )
