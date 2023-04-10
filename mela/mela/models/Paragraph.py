# from sqlalchemy.orm import Mapped, relationship
# from sqlalchemy import Column, Integer, String, ForeignKey
# from mela.models.Base import Base, DtoBase, BaseModel
# from mela.models.Sentence import *
# from mela.models.Text import *

# class Paragraph(Base, DtoBase):
#     __tablename__ = "paragraph"
#     id: Mapped[int] = Column(Integer, primary_key=True)
#     text_id: Mapped[int] = Column(Integer, ForeignKey("text.id"))
#     # one to many relationship
#     # text: Mapped[str] = Column(String)
#     # sentence = relationship("Sentence", back_populates="paragraph",cascade="all, delete, delete-orphan")
#     order: Mapped[int] = Column(Integer)
#     text = relationship("Text", back_populates="paragraph")

    # def __repr__(self) -> str:
    #     # return f"Paragraph(id={self.id!r}, text={self.text_id!r}, order={self.order!r})"
    #     return f"Paragraph(id={self.id!r}, order={self.order!r})"

# class Paragraph(Base, DtoBase):
#     __tablename__ = "paragraph"
#     id: Mapped[int] = Column(Integer, primary_key=True)
#     text_id: Mapped[int] = Column(Integer, ForeignKey("text.id"))
#     # one to many relationship
#     # text: Mapped[str] = Column(String)
#     # sentence = relationship("Sentence", back_populates="paragraph",cascade="all, delete, delete-orphan")
#     order: Mapped[int] = Column(Integer)
#     text: Mapped["Text"] = relationship("Text", back_populates="paragraph")

#     def __repr__(self) -> str:
#     # return f"Paragraph(id={self.id!r}, text={self.text_id!r}, order={self.order!r})"
#         return f"Paragraph(id={self.id!r}, order={self.order!r})"


# class Paragraph(Base):
#     __tablename__ = "paragraph"
#     id: Mapped[int] = Column(Integer, primary_key=True)
#     # one to many relationship
#     # text: Mapped[str] = Column(String)
#     sentence = relationship("Sentence", back_populates="paragraph",cascade="all, delete, delete-orphan")
#     order: Mapped[int] = Column(Integer)
#     text: Mapped["Text"] = relationship("Text", back_populates="paragraphs", uselist=True)
#     text_id: Mapped[int] = Column(Integer, ForeignKey("text.id"))

# class ParagraphModel(BaseModel):
#     class Config:
#         orm_mode = True

#     id: int
#     order: int