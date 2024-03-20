from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_users import FastAPIUsers
from redis import asyncio as aioredis

from src.auth.base_config import auth_backend
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate
from src.auth.models import User

from src.operations.router import router as router_operation
from src.tasks.router import router as router_task
import sys
import os

sys.path.append(os.path.join(sys.path[0], 'src'))

'''
run app:

uvicorn src.main:app --reload
'''
app = FastAPI(
    title="Trading App"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_operation)
app.include_router(router_task)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost", prefix="fastapi-cache-trading-app")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
