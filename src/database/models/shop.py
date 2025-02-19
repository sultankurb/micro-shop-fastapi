from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text
from .association_tables import *
from typing import TYPE_CHECKING
from src.database import Base
if TYPE_CHECKING:
    from .users import UsersORM


class ShopORM(Base):
    __tablename__ = 'shop'
    name: Mapped[str] = mapped_column(String(length=300), unique=True)
    description: Mapped[str] = mapped_column(Text(length=560))
    owner: Mapped["UsersORM"] = relationship(
        "UsersORM",
        back_populates="shop",
        lazy='joined',
        cascade='all, delete',
        secondary='users_shop_association'
    )
