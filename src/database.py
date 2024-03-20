from datetime import datetime
from typing import AsyncGenerator

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String, Boolean, Column, Integer, TIMESTAMP, ForeignKey, MetaData
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, declarative_base

from src.config import DB_USER, DB_HOST, DB_NAME, DB_PASS, DB_PORT

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base = declarative_base()


metadata = MetaData()

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
