from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, TIMESTAMP, text, ForeignKey
from datetime import datetime, timezone
from .association_tables import *
from typing import TYPE_CHECKING
from src.database import Base
if TYPE_CHECKING:
    from .shop import ShopORM
    from .orders import OrdersORM
    from .role import RolesORM


class UsersORM(Base):
    __tablename__ = 'users'
    phone: Mapped[str] = mapped_column(String(length=150), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(length=50), nullable=False)
    first_name: Mapped[str] = mapped_column(String(length=60), nullable=False)
    last_name: Mapped[str] = mapped_column(String(length=60), nullable=False)
    role: Mapped[int] = mapped_column(
        ForeignKey(column='roles.pk', onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
    role_rel: Mapped["RolesORM"] = relationship(
        "RolesORM",
        back_populates="users",
        cascade="all, delete",
        lazy='joined'
    )
    started_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
        onupdate=datetime.now(timezone.utc),
        server_default=text("TIMEZONE('utc', now())"),
    )
    shop: Mapped['ShopORM'] = relationship(
        'ShopORM',
        back_populates='owner',
        lazy='joined',
        cascade='all, delete',
        secondary='users_shop_association'
    )
    orders: Mapped['OrdersORM'] = relationship(
        'OrdersORM',
        back_populates='customer',
        lazy='joined',
        cascade='all, delete',
        secondary="users_orders_association",
    )
