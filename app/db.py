# # app/db.py
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import sessionmaker
#
# DATABASE_URL = "postgresql+asyncpg://mashiro:%40gG8503280@localhost:5432/blockchainapp"
#
#
# engine = create_async_engine(DATABASE_URL, echo=True)
#
# async_session = sessionmaker(
#     engine, expire_on_commit=False, class_=AsyncSession
# )

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
import asyncio

# 👇 這裡引入你自己的 User 模型
from .models import Base, User

# Supabase 資料庫連線字串（@ 要換成 %40）
DATABASE_URL = "postgresql+asyncpg://postgres.iannnonmxjftdurkpdxx:%40gG8503280@aws-0-ap-northeast-1.pooler.supabase.com:5432/postgres"

# 建立 async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# async session factory
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# 建立資料表
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("✅ Tables created!")

# 新增使用者
async def create_user(email: str, password: str):
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(User).where(User.email == email))
            user = result.scalar_one_or_none()
            if user:
                user.password = password  # 更新現有記錄
                print(f"✅ User updated: {email}")
            else:
                user = User(email=email, password=password)
                session.add(user)
                print(f"✅ User created: {email}")
        await session.commit()
# 取得所有使用者
async def get_users():
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        for u in users:
            print(f"User: {u.email}, Password: {u.password}")

# main 測試區
if __name__ == "__main__":
    async def main():
        await create_tables()
        # 新增測試帳號
        await create_user("test@example.com", "mypassword123")
        # 查詢全部使用者
        await get_users()

    asyncio.run(main())

