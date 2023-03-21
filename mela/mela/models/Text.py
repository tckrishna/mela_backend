from sqlalchemy.orm import Mapped,relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from mela.models.Base import Base, DtoBase

class Text(Base, DtoBase):
    __tablename__ = "text"
    id: Mapped[int] = Column(Integer, primary_key=True)
    title: Mapped[str] = Column(String)
    author_id: Mapped[int] = Column(Integer, ForeignKey("author.id"), nullable=False)
    manuscript_id: Mapped[int] =Column(Integer, ForeignKey("manuscript.id"),nullable=False)

    def __repr__(self) -> str:
        return f"Text(id={self.id!r}, title={self.title!r})"