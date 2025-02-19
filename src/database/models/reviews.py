from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, Integer
from .association_tables import *
from typing import TYPE_CHECKING
from src.database import Base
if TYPE_CHECKING:
    from .users import UsersORM


class ReviewsORM(Base):
    __tablename__ = 'reviews'
    review_text: Mapped[str] = mapped_column(Text(length=360))
    review_mark: Mapped[int] = mapped_column(Integer)
    user: Mapped["UsersORM"] = relationship(
        "UsersORM",
        back_populates="reviews",
        cascade="all, delete",
        lazy='joined',
        secondary='reviews_users_association'
    )