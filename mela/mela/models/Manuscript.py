from sqlalchemy.orm import declarative_base, Mapped
from sqlalchemy import Column, Integer, String
from mela.models.Base import Base, DtoBase

class Manuscript(Base, DtoBase):
    __tablename__ = "manuscript"
    id: Mapped[int] = Column(Integer, primary_key=True)
    title: Mapped[str] = Column(String)
    author: Mapped[str] = Column(String)

    def __repr__(self) -> str:
        return f"Manuscript(id={self.id!r}, title={self.title!r}, author={self.author!r})"