from typing import cast

from pydantic import BaseSettings
from sqlalchemy import text, select
# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession


from starlite import Starlite, State, get
from starlite.plugins.sql_alchemy import SQLAlchemyConfig, SQLAlchemyPlugin

from model import *

class AppSettings(BaseSettings):
    DATABASE_URI: str = "postgresql+asyncpg://vagrant:mela@127.0.0.1:5432/mela"


settings = AppSettings()
sqlalchemy_config = SQLAlchemyConfig(connection_string=settings.DATABASE_URI, dependency_key="async_session")
sqlalchemy_plugin = SQLAlchemyPlugin(config=sqlalchemy_config)

@get("/")
def hello_world() -> dict[str, str]:
    """Handler function that returns a greeting dictionary."""
    return {"hello": "world"}

@get("/test_mela")
async def get_manuscript(async_session: AsyncSession) -> list[Manuscript]:
    """Handler function that returns a text and manuscript"""
    
    # # engine = create_engine("postgresql+asyncpg://vagrant:mela@locahost:5432/mela")
    # # conn_string = "host='localhost' dbname='mela' user='vagrant' password='mela'"
    # session = Session(state.engine)

    # stmt = select(Translation).where(and_(Translation.manuscript_id==1, Translation.paragraph==1, Translation.line==2))

    # for translation in session.scalars(stmt):
    #     print(translation)

    # # return text

    # session = Session(state.engine.begin())

    return list(await async_session.scalars(select(Manuscript)))

    # async with state.engine.begin() as conn:
    #     results = (await conn.execute(select(Manuscript))).all()
    #     print(results)



        # return (await conn.execute(text("select * from manuscript"))).all()
            # print(result)


# app = Starlite(route_handlers=[hello_world])


# def get_db_connection(state: State) -> AsyncEngine:
#     """Returns the db engine.

#     If it doesn't exist, creates it and saves it in on the application state object
#     """
#     if not getattr(state, "engine", None):
#         state.engine = create_async_engine(settings.DATABASE_URI)
#     return cast("AsyncEngine", state.engine)


# async def close_db_connection(state: State) -> None:
#     """Closes the db connection stored in the application State object."""
#     if getattr(state, "engine", None):
#         await cast("AsyncEngine", state.engine).dispose()


app = Starlite(
    route_handlers=[hello_world,get_manuscript],
    # on_startup=[get_db_connection],
    # on_shutdown=[close_db_connection],
    plugins=[sqlalchemy_plugin]
)

# conn_string = "host='localhost' dbname='mela' user='vagrant' password='mela'"
# # use connect function to establish the connection
# conn = psycopg2.connect(conn_string)
