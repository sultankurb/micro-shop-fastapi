from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class UserShopAssociationORM(Base):
    __tablename__ = 'users_shop_association'
    __table_args__ = (
        UniqueConstraint(
            'users_pk',
            'shop_pk',
            name='idx_unique_users_shop_relation'
        ),
    )
    users_pk: Mapped[int] = mapped_column(
        ForeignKey(
            column='users.pk',
            ondelete='CASCADE',
            onupdate='CASCADE',
        ),
    )
    shop_pk: Mapped[int] = mapped_column(
        ForeignKey(
            column='shop.pk',
            ondelete='CASCADE',
            onupdate='CASCADE',
        ),
    )
