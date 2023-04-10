# from sqlalchemy.orm import Mapped,relationship
# from sqlalchemy import Column, Integer, String, ForeignKey
# from mela.models.Base import Base, DtoBase
# from mela.models.Paragraph import *
# from mela.models.Language import *
# # from mela.models.Translation import *

# class Sentence(Base, DtoBase):
#     __tablename__ = "sentence"
#     id: Mapped[int] = Column(Integer, primary_key=True)
#     # paragraph_id: Mapped[int] = Column(Integer, ForeignKey("paragraph.id"), nullable=False)
#     # many to one relationship
#     # paragraph = relationship("Paragraph", back_populates="sentence")
#     # language_id: Mapped[int] = Column(Integer, ForeignKey("language.id"), nullable=False)
#     order: Mapped[int] = Column(Integer)
#     text: Mapped[str] = Column(String)
#     # one to one relationship
#     # translation = relationship("Translation", back_populates="sentence", uselist=False)

#     # def __init__(self,language,order,text):
#     #     self.language = language
#     #     self.order = order
#     #     self.text = text


#     def __repr__(self) -> str:
#         return f"Sentence(id={self.id!r}, text={self.text!r}, order={self.order!r})"