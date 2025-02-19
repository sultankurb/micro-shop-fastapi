from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class UsersReviewsAssociationORM(Base):
    __tablename__ = 'reviews_users_association'
    __table_args__ = (
        UniqueConstraint(
            'users_pk',
            'reviews_pk',
            name='idx_unique_users_reviews_relation'
        ),
    )
    users_pk: Mapped[int] = mapped_column(
        ForeignKey(
            column='users.pk',
            ondelete='CASCADE',
            onupdate='CASCADE',
        ),
    )
    reviews_pk: Mapped[int] = mapped_column(
        ForeignKey(
            column='reviews.pk',
            ondelete='CASCADE',
            onupdate='CASCADE',
        ),
    )
