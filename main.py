from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from src.router.main_router import api_v1
from src.domain import create_roles
from fastapi import FastAPI
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_roles()
    yield


app = FastAPI(
    lifespan=lifespan,
    version="0.0.1",
    title='Simple shop API',
    description='Simple shop API On FastAPI',
)
app.include_router(api_v1)


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='0.0.0.0', port=8000, reload=True)
