from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Float, Text
from typing import TYPE_CHECKING, List
from .association_tables import *
from src.database import Base
if TYPE_CHECKING:
    from .orders import OrdersORM
    from .reviews import ReviewsORM


class ProductsORM(Base):
    __tablename__ = 'products'
    name: Mapped[str] = mapped_column(String(length=300))
    description: Mapped[str] = mapped_column(Text(length=560))
    price: Mapped[float] = mapped_column(Float)
    orders: Mapped["List[OrdersORM]"] = relationship(
        "OrdersORM",
        secondary='products_orders_association',
        back_populates='products',
        lazy='joined',
        cascade='all, delete',
    )
    reviews: Mapped["List[ReviewsORM]"] = relationship(
        "ReviewsORM",
        secondary='reviews_users_association',
        back_populates='products',
        lazy='joined',
        cascade='all, delete',
    )
