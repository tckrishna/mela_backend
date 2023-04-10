# from sqlalchemy.orm import Mapped, relationship
# from sqlalchemy import Column, Integer, String, ForeignKey
# from mela.models.Base import Base, DtoBase
# from mela.models.Text import *

# class Author(Base, DtoBase):
#     __tablename__ = "author"
#     id: Mapped[int] = Column(Integer, primary_key=True)
#     author: Mapped[str] = Column(String)
#     # text = relationship("Text", back_populates="author", cascade="all, delete, delete-orphan")

#     def __repr__(self) -> str:
#         return f"Author(id={self.id!r}, text={self.author!r})"