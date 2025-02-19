from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from dotenv import load_dotenv
import os


load_dotenv()

async_db_url = os.getenv("DATABASE_URL")
if async_db_url is None:
    async_db_url = 'sqlite+aiosqlite:///test.db'

async_engine = create_async_engine(url=async_db_url)
async_session_factory = async_sessionmaker(async_engine, class_=AsyncSession)
