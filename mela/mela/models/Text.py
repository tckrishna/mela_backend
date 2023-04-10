from sqlalchemy.orm import Mapped,relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from mela.models.Base import Base, DtoBase
from mela.models.Author import *
from mela.models.Manuscript import *
from mela.models.Paragraph import *

# class Text(Base, DtoBase):
#     __tablename__ = "text"
#     id: Mapped[int] = Column(Integer, primary_key=True)
#     title: Mapped[str] = Column(String)
#     author_id: Mapped[int] = Column(Integer, ForeignKey("author.id", ondelete="CASCADE"), nullable=False)
#     manuscript_id: Mapped[int] =Column(Integer, ForeignKey("manuscript.id", ondelete="CASCADE"),nullable=False)
#     paragraph = relationship("Paragraph", back_populates="text", cascade="all, delete, delete-orphan")
#     author = relationship("Author", back_populates="text")
#     manuscript = relationship("Manuscript", back_populates="text")

#     def __repr__(self) -> str:
#         return f"Text(Title={self.title!r}, author_id={self.author_id!r})"

# class Text(Base, DtoBase):
#     __tablename__ = "text"
#     id: Mapped[int] = Column(Integer, primary_key=True)
#     title: Mapped[str] = Column(String)
#     author_id: Mapped[int] = Column(Integer, ForeignKey("author.id", ondelete="CASCADE"), nullable=False)
#     manuscript_id: Mapped[int] =Column(Integer, ForeignKey("manuscript.id", ondelete="CASCADE"),nullable=False)
#     paragraphs: Mapped[list[Paragraph]] = relationship("Paragraph", back_populates="text", uselist=True, lazy='joined')
#     author = relationship("Author", back_populates="text", lazy='joined')
#     manuscript = relationship("Manuscript", back_populates="text", lazy='joined')

#     def __repr__(self) -> str:
#         return f"Text(Title={self.title!r}, author_id={self.author_id!r})"

# class TextModel(BaseModel):
#     class Config:
#         orm_mode= True

#     id: int
#     title: str
#     paragraphs: list[ParagraphModel]