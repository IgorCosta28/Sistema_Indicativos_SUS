from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

DATA_BASE_URL = 'sqlite+aiosqlite:///src/db/database.db'

engine = create_async_engine(
    DATA_BASE_URL,
    echo=True
)

SessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False
)

