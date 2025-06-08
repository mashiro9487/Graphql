# tests/test_db.py
import pytest
import pytest_asyncio
from sqlalchemy import delete, select

from app.db import engine, async_session
from app.models import Base, User


@pytest_asyncio.fixture(scope="module")
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.mark.asyncio
async def test_create_multi_user():
    users_data = [
        {"email": "user1@example.com", "password": "pw1"},
        {"email": "user2@example.com", "password": "pw2"},
        {"email": "user3@example.com", "password": "pw3"},
    ]

    # 清空資料表
    async with async_session() as session:
        await session.execute(delete(User))
        await session.commit()

    # 插入多筆資料
    async with async_session() as session:
        async with session.begin():
            for data in users_data:
                user = User(email=data["email"], password=data["password"])
                session.add(user)

    # 驗證資料是否正確寫入
    async with async_session() as session:
        for data in users_data:
            result = await session.execute(
                select(User).where(User.email == data["email"])
            )
            user = result.scalar_one_or_none()
            assert user is not None
            assert user.email == data["email"]
            assert user.password == data["password"]
