from sqlalchemy import select, insert, delete, update
from src.database import async_session_factory, Base
from .base_repo import BaseRepo


class SQLAlchemyRepository(BaseRepo):
    model: Base = None

    async def select_all(self, limit: int):
        async with async_session_factory() as session:
            stmt = select(self.model).limit(limit=limit)
            result = await session.execute(stmt)
            return result.scalars().all()

    async def select_one(self, filters: dict):
        async with async_session_factory() as session:
            stmt = select(self.model).filter_by(**filters)
            result = await session.execute(stmt)
            return result.scalar()

    async def insert_one(self, data: dict) -> bool:
        async with async_session_factory() as session:
            stmt = insert(self.model).values(**data).returning(self.model.pk)
            result = await session.execute(stmt)
            await session.commit()
            if result is not None:
                return True
            return False

    async def delete_one(self, pk: int):
        async with async_session_factory() as session:
            stmt = delete(self.model).filter_by(pk=pk)
            await session.execute(stmt)
            await session.commit()

    async def update_one(self, pk: int, data: dict) -> bool:
        async with async_session_factory() as session:
            stmt = update(self.model).filter_by(pk=pk).values(**data).returning(self.model.pk)
            result = await session.execute(stmt)
            await session.commit()
            if result is not None:
                return True
            return False

    async def insert_many(self, data: list[dict]):
        async with async_session_factory() as session:
            await session.execute(
                insert(self.model),
                data
            )
