from sqlalchemy.ext.asyncio import create_async_engine

asyncio_engine = create_async_engine(
    "postgresql+psycopg://postgres:postgres@0.0.0.0:5432/postgres"
)

"""SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
"""