from sqlalchemy.orm import declarative_base, Mapped
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Manuscript(Base):
    __tablename__ = "test_manuscript"
    id: Mapped[int] = Column(Integer, primary_key=True)
    title: Mapped[str] = Column(String)
    author: Mapped[str] = Column(String)

    def __repr__(self) -> str:
        return f"Manuscript(id={self.id!r}, title={self.title!r}, author={self.author!r})"