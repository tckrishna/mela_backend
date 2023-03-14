from sqlalchemy.orm import declarative_base, Mapped
from sqlalchemy import Column, Integer, String,ForeignKey

Base = declarative_base()

class Translation(Base):
    __tablename__ = "translation"
    id: Mapped[int] = Column(Integer, primary_key=True)
    manuscript_id: Mapped[int] =Column(Integer, ForeignKey("manuscript.id"))
    paragraph: Mapped[int]
    line: Mapped[int]
    text: Mapped[str]
    translation: Mapped[str]

    def __repr__(self) -> str:
        return f"Translation(manuscript_id={self.manuscript_id!r}, paragraph={self.paragraph!r}, line={self.line!r}, text={self.text!r}, translation={self.translation!r})"