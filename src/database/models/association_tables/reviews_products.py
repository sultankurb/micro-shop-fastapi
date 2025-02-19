from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class ReviewsProductsAssociationORM(Base):
    __tablename__ = 'reviews_products_association'
    __table_args__ = (
        UniqueConstraint(
            'products_pk',
            'reviews_pk',
            name='idx_unique_products_reviews_relation'
        ),
    )
    products_pk: Mapped[int] = mapped_column(
        ForeignKey(
            column='products.pk',
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
