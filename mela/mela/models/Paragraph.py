from sqlalchemy.orm import Mapped
from sqlalchemy import Column, Integer, String, ForeignKey
from mela.models.Base import Base, DtoBase

class Paragraph(Base, DtoBase):
    __tablename__ = "paragraph"
    id: Mapped[int] = Column(Integer, primary_key=True)
    text_id: Mapped[int] = Column(Integer, ForeignKey("text.id"))
    order: Mapped[int] = Column(Integer)

    def __repr__(self) -> str:
        return f"Paragraph(id={self.id!r}, text={self.text_id!r}, order={self.order!r})"