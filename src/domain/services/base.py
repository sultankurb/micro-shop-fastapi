from src.domain.repositories import BaseRepo
from fastapi import HTTPException, status
from pydantic import BaseModel


class BaseService:
    def __init__(self, repo: BaseRepo):
        self.repository = repo

    async def send_all(self, limit: int = 100):
        result = await self.repository.select_all(limit=limit)
        return result

    async def send_one_by_pk(self, pk: int):
        result = await self.repository.select_one(filters={"pk": pk})
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
        return result

    async def send_one_by_custom_filter(self, filters: dict):
        result = await self.repository.select_one(filters=filters)
        if result is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
        return result

    async def add_new_one(self, request: BaseModel):
        data = request.model_dump(exclude_unset=True)
        result: bool = await self.repository.insert_one(data)
        if result:
            return {"Message": f"Item with data: {data}\n was added successfully"}
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to add data please try again"
        )

    async def delete_one(self, pk: int):
        check = await self.send_one_by_pk(pk=pk)
        if check is not None:
            await self.repository.delete_one(pk)
            return {"Message": f"Item with pk: {pk} was deleted successfully"}
        return check

    async def edit_one(self, request: BaseModel, pk: int):
        data = request.model_dump(exclude_unset=True)
        await self.repository.update_one(pk, data)
        return await self.send_one_by_pk(pk=pk)


