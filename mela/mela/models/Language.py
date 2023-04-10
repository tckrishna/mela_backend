# from sqlalchemy.orm import Mapped
# from sqlalchemy import Column, Integer, String, ForeignKey
# from mela.models.Base import Base, DtoBase

# class Language(Base, DtoBase):
#     __tablename__ = "language"
#     id: Mapped[int] = Column(Integer, primary_key=True)
#     iso_code: Mapped[str] = Column(String)
#     language: Mapped[str] = Column(String)

#     def __repr__(self) -> str:
#         return f"Language(id={self.id!r}, language={self.language!r})"