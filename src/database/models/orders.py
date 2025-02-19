from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, TYPE_CHECKING, List
from sqlalchemy import String, Float
from .association_tables import *
from src.database import Base
if TYPE_CHECKING:
    from .users import UsersORM
    from .products import ProductsORM


class OrdersORM(Base):
    __tablename__ = 'orders'
    promo_code: Mapped[Optional[str]] = mapped_column(
        String(length=30), nullable=True
    )
    customer: Mapped['UsersORM'] = relationship(
        'UsersORM',
        back_populates='orders',
        cascade='all, delete',
        lazy='joined',
        secondary='users_orders_association'
    )
    products: Mapped["List[ProductsORM]"] = relationship(
        'ProductsORM',
        back_populates='orders',
        cascade='all, delete',
        lazy='joined',
        secondary='products_orders_association'
    )
    total_price: Mapped[float] = mapped_column(Float)
