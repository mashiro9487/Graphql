import asyncio

from app.db import engine
from app.models import Base


async def init():
    # 這行會列出目前 Base 中註冊的所有資料表名稱
    print("已註冊的資料表：", Base.metadata.tables.keys())

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# 為了單獨執行檔案測試時用（例如 python -m app.init_db）
if __name__ == "__main__":
    asyncio.run(init())
