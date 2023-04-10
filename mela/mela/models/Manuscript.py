# from sqlalchemy.orm import declarative_base, Mapped, relationship
# from sqlalchemy import Column, Integer, String
# from mela.models.Base import Base, DtoBase
# # from mela.models.Text import Text
# from pydantic import BaseModel

# class Manuscript(Base, DtoBase):
#     __tablename__ = "manuscript"
#     id: Mapped[int] = Column(Integer, primary_key=True)
#     title: Mapped[str] = Column(String)
#     author: Mapped[str] = Column(String)
#     # text: Mapped[Text] = relationship("Text", back_populates="manuscript", cascade="all, delete, delete-orphan")

#     def __repr__(self) -> str:
#         return f"Manuscript(id={self.id!r}, title={self.title!r}, author={self.author!r})"

# class ManuscriptModel(BaseModel):
#     id: int
#     title: str
#     author: str