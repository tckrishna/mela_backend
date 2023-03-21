from starlite.plugins.sql_alchemy import SQLAlchemyConfig, SQLAlchemyPlugin
from starlite import DTOFactory
from pydantic import BaseSettings

class AppSettings(BaseSettings):
    DATABASE_URI: str = "postgresql+asyncpg://vagrant:mela@127.0.0.1:5432/mela"

settings = AppSettings()
sqlalchemy_config = SQLAlchemyConfig(connection_string=settings.DATABASE_URI, dependency_key="async_session")
sqlalchemy_plugin = SQLAlchemyPlugin(config=sqlalchemy_config)

dto_factory = DTOFactory(plugins=[sqlalchemy_plugin])