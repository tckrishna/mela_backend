from sqlalchemy.orm import Mapped,relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from mela.models.Base import Base, DtoBase

class Sentence(Base, DtoBase):
    __tablename__ = "sentence"
    id: Mapped[int] = Column(Integer, primary_key=True)
    title: Mapped[str] = Column(String)
    paragraph_id: Mapped[int] = Column(Integer, ForeignKey("paragraph.id"), nullable=False)
    language_id: Mapped[int] = Column(Integer, ForeignKey("language.id"), nullable=False)
    order: Mapped[int] = Column(Integer)
    text: Mapped[str] = Column(String)

    def __repr__(self) -> str:
        return f"Sentence(id={self.id!r}, text={self.text!r}, order={self.order!r})"