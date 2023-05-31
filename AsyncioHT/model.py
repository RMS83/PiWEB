import asyncio

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, declarative_base
from config import PG_DSN



engine = create_async_engine(PG_DSN, echo=False)

class Base(DeclarativeBase): pass

class People(Base):

    __tablename__ = 'people'

    id = Column(Integer, primary_key=True, autoincrement=True)
    birth_year = Column(String)
    eye_color = Column(String)
    films = Column(String)
    gender = Column(String)
    hair_color = Column(String)
    height = Column(String)
    homeworld = Column(String)
    mass = Column(String)
    name = Column(String)
    skin_color = Column(String)
    species = Column(String)
    starships = Column(String)
    vehicles = Column(String)


Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# async def disp():
#     await engine.dispose()
#
# async def init_models(eng: AsyncSession):
#     async with eng.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#
#     await engine.dispose()
#
#
# asyncio.run(init_models(engine))
