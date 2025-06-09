import asyncio

import pytest
from sqlalchemy.ext.asyncio import create_async_engine


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def engine():
    engine = create_async_engine(
        "postgresql+asyncpg://mashiro:%40gG8503280@localhost:5432/blockchainapp",
        pool_size=5,
        max_overflow=10,
        echo=True
    )
    yield engine
    await engine.dispose()


@pytest.fixture
async def async_session(engine):
    async with engine.begin() as conn:
        yield conn
