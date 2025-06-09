import pytest
from sqlalchemy import delete, select

from app.db import async_session  # 你定義的 session factory
from app.models import User


# 建立 pytest fixture，避免跨 event loop 問題
@pytest.fixture
async def db_session():
    async with async_session() as session:
        yield session
        await session.rollback()  # 確保資料不殘留


@pytest.mark.asyncio
async def test_create_and_partial_delete_users(db_session):
    users_data = [
        {"email": "user1@example.com", "password": "pw1"},
        {"email": "user2@example.com", "password": "pw2"},
        {"email": "user3@example.com", "password": "pw3"},
    ]

    users_to_delete = ["user1@example.com", "user3@example.com"]
    users_to_keep = ["user2@example.com"]

    # 清空資料表
    await db_session.execute(delete(User))

    # 插入多筆資料
    for data in users_data:
        user = User(email=data["email"], password=data["password"])
        db_session.add(user)

    await db_session.commit()

    # 確認資料都有寫入
    for data in users_data:
        result = await db_session.execute(select(User).where(User.email == data["email"]))
        user = result.scalar_one_or_none()
        assert user is not None
        assert user.email == data["email"]

    # 刪除部分使用者
    await db_session.execute(delete(User).where(User.email.in_(users_to_delete)))
    await db_session.commit()

    # 驗證刪除與保留狀況
    for email in users_to_delete:
        result = await db_session.execute(select(User).where(User.email == email))
        user = result.scalar_one_or_none()
        assert user is None, f"{email} should have been deleted"

    for email in users_to_keep:
        result = await db_session.execute(select(User).where(User.email == email))
        user = result.scalar_one_or_none()
        assert user is not None, f"{email} should still exist"
        assert user.email == email
