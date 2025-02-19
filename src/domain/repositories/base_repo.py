from abc import ABC, abstractmethod

class BaseRepo(ABC):

    @abstractmethod
    async def select_all(self, limit: int):
        raise NotImplementedError

    @abstractmethod
    async def select_one(self, filters: dict):
        raise NotImplementedError

    @abstractmethod
    async def insert_one(self, data: dict) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, pk: int):
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, pk: int, data: dict) -> bool:
        raise NotImplementedError
