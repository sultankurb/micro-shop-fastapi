from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class UsersOrdersAssociationORM(Base):
    __tablename__ = 'users_orders_association'
    __table_args__ = (
        UniqueConstraint(
            'user_pk',
            'orders_pk',
            name='idx_unique_users_orders_relation'
        ),
    )
    user_pk: Mapped[int] = mapped_column(
        ForeignKey(
            column='users.pk',
            ondelete='CASCADE',
            onupdate='CASCADE',
        ),
    )
    orders_pk: Mapped[int] = mapped_column(
        ForeignKey(
            column='orders.pk',
            ondelete='CASCADE',
            onupdate='CASCADE',
        ),
    )
