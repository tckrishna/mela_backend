# from sqlalchemy.orm import Mapped, relationship
# from sqlalchemy import Column, Integer, ForeignKey, String
# from mela.models.Base import Base, DtoBase

# class Translation(Base,DtoBase):
#     __tablename__ = "translation"
#     id: Mapped[int] = Column(Integer, primary_key=True)
#     sentence_id: Mapped[int] =Column(Integer, ForeignKey("sentence.id", ondelete="CASCADE"))
#     # sentence = relationship("Sentence", back_populates="translation", uselist=False)
#     language_id: Mapped[int] = Column(Integer, ForeignKey("language.id", ondelete="CASCADE"), nullable=False)
#     text: Mapped[str] = Column(String)

#     def __repr__(self) -> str:
#         return f"Translation(id={self.id!r}, sentence_id={self.sentence_id!r}, language={self.language_id!r}, text={self.text!r})"