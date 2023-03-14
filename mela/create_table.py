from sqlalchemy import create_engine,Table, Column, Integer, String, MetaData
from mela.models.manuscript import *

DATABASE_URI: str = "postgresql://vagrant:mela@127.0.0.1:5432/mela"

engine = create_engine(DATABASE_URI, echo=True)

Manuscript.metadata.create_all(engine)