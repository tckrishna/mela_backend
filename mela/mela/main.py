from starlite import Starlite, get
from mela.settings import sqlalchemy_plugin

from mela.controller.manuscript import *

# from starlite.plugins.sql_alchemy import SQLAlchemyConfig, SQLAlchemyPlugin
# from starlite import DTOFactory
# from pydantic import BaseSettings

# class AppSettings(BaseSettings):
#     DATABASE_URI: str = "postgresql+asyncpg://vagrant:mela@127.0.0.1:5432/mela"

# settings = AppSettings()
# sqlalchemy_config = SQLAlchemyConfig(connection_string=settings.DATABASE_URI, dependency_key="async_session")
# sqlalchemy_plugin = SQLAlchemyPlugin(config=sqlalchemy_config)

# dto_factory = DTOFactory(plugins=[sqlalchemy_plugin])



@get("/")
def hello_world() -> dict[str, str]:
    """Handler function that returns a greeting dictionary."""
    return {"hello": "world"}

app = Starlite(
    route_handlers=[hello_world, get_manuscripts, post_manuscript],
    plugins=[sqlalchemy_plugin],
    debug=True,
)