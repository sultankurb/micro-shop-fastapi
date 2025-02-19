from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import BigInteger


class Base(DeclarativeBase, AsyncAttrs):
    __abstract__ = True
    pk: Mapped[int] = mapped_column(BigInteger, primary_key=True)
