from sqlalchemy.orm import declarative_base
from mela.settings import dto_factory

Base = declarative_base()

class DtoBase():
    @classmethod
    def create_dto(cls):
        # print(f"Create{cls.__name__}DTO", cls.__name__)
        return dto_factory(f"Create{cls.__name__}DTO", cls, exclude=["id"])
