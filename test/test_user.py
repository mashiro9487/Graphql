# test_users.py
import pytest
from sqlalchemy import select, delete

from app.db import async_session
from app.models import User  # 請替換成你實際的 User model 定義


@pytest.fixture
async def clean_db():
    async with async_session() as session:
        await session.execute(delete(User))
        await session.commit()


@pytest.mark.asyncio
async def test_create_user(clean_db):
    async with async_session() as session:
        new_user = User(email="test@example.com", password="hashed_pw")
        session.add(new_user)
        await session.commit()

        # 驗證是否成功寫入
        result = await session.execute(select(User).where(User.email == "test@example.com"))
        user = result.scalar_one()
        assert user.email == "test@example.com"


@pytest.mark.asyncio
async def test_read_user(clean_db):
    # 測試前需要自行創建一個 user
    async with async_session() as session:
        new_user = User(email="test2@example.com", password="hashed_pw")
        session.add(new_user)
        await session.commit()

    async with async_session() as session:
        result = await session.execute(select(User).where(User.email == "test2@example.com"))
        user = result.scalar_one_or_none()
        assert user is not None

# @pytest.mark.asyncio
# async def test_create_multi_user():
#     users_data = [
#         {"email": "user1@example.com", "password": "pw1"},
#         {"email": "user2@example.com", "password": "pw2"},
#         {"email": "user3@example.com", "password": "pw3"},
#     ]
#
#     # 清空資料表
#     async with async_session() as session:
#         await session.execute(delete(User))
#         await session.commit()
#
#     # 插入多筆資料
#     async with async_session() as session:
#         async with session.begin():
#             for data in users_data:
#                 user = User(email=data["email"], password=data["password"])
#                 session.add(user)
#
#     # 驗證資料是否正確寫入
#     async with async_session() as session:
#         for data in users_data:
#             result = await session.execute(
#                 select(User).where(User.email == data["email"])
#             )
#             user = result.scalar_one_or_none()
#             assert user is not None
#             assert user.email == data["email"]
#             assert user.password == data["password"]
#
# @pytest.mark.asyncio
# async def test_create_and_partial_delete_users(db_session):
#     users_data = [
#         {"email": "user1@example.com", "password": "pw1"},
#         {"email": "user2@example.com", "password": "pw2"},
#         {"email": "user3@example.com", "password": "pw3"},
#     ]
#
#     users_to_delete = ["user1@example.com", "user3@example.com"]
#     users_to_keep = ["user2@example.com"]
#
#     # 清空資料表
#     await db_session.execute(delete(User))
#
#     # 插入多筆資料
#     for data in users_data:
#         user = User(email=data["email"], password=data["password"])
#         db_session.add(user)
#
#     await db_session.commit()
#
#     # 確認資料都有寫入
#     for data in users_data:
#         result = await db_session.execute(select(User).where(User.email == data["email"]))
#         user = result.scalar_one_or_none()
#         assert user is not None
#         assert user.email == data["email"]
#
#     # 刪除部分使用者
#     await db_session.execute(delete(User).where(User.email.in_(users_to_delete)))
#     await db_session.commit()
#
#     # 驗證刪除與保留狀況
#     for email in users_to_delete:
#         result = await db_session.execute(select(User).where(User.email == email))
#         user = result.scalar_one_or_none()
#         assert user is None, f"{email} should have been deleted"
#
#     for email in users_to_keep:
#         result = await db_session.execute(select(User).where(User.email == email))
#         user = result.scalar_one_or_none()
#         assert user is not None, f"{email} should still exist"
#         assert user.email == email
