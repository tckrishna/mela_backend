from sqlalchemy.orm import Mapped
from sqlalchemy import Column, Integer, String, ForeignKey
from mela.models.Base import Base, DtoBase

class Author(Base, DtoBase):
    __tablename__ = "author"
    id: Mapped[int] = Column(Integer, primary_key=True)
    author: Mapped[str] = Column(String)

    def __repr__(self) -> str:
        return f"Author(id={self.id!r}, text={self.author!r})"