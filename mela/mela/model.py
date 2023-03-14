from typing import List
from typing import Optional
# from sqlalchemy import ForeignKey
# from sqlalchemy import String
from sqlalchemy.orm import declarative_base, Mapped
from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy.orm import relationship

Base = declarative_base()

# class Manuscript(Base):
#     __tablename__ = "manuscript"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str]
#     author: Mapped[Optional[str]]

#     def __repr__(self) -> str:
#         return f"Manuscript(id={self.id!r}, title={self.title!r}, author={self.author!r})"
class Manuscript(Base):
    __tablename__ = "manuscript"
    id: Mapped[int] = Column(Integer, primary_key=True)
    title: Mapped[str] = Column(String)
    author: Mapped[str] = Column(String)

    def __repr__(self) -> str:
        return f"Manuscript(id={self.id!r}, title={self.title!r}, author={self.author!r})"

# class Translation(Base):
#     __tablename__ = "translation"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     manuscript_id: Mapped[int] = mapped_column(ForeignKey("manuscript.id"))
#     paragraph: Mapped[int]
#     line: Mapped[int]
#     text: Mapped[str]
#     translation: Mapped[str]

#     def __repr__(self) -> str:
#         return f"Translation(manuscript_id={self.manuscript_id!r}, paragraph={self.paragraph!r}, line={self.line!r}, text={self.text!r}, translation={self.translation!r})"