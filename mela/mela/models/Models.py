from sqlalchemy.orm import declarative_base
from mela.settings import dto_factory
from pydantic import BaseModel
from sqlalchemy.orm import Mapped,relationship
from sqlalchemy import Column, Integer, String, ForeignKey, inspect, UniqueConstraint

Base = declarative_base()

class DtoBase():
    def to_dict(self):
        # return {field.name:getattr(self, field.name) for field in self.__table__.c}
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
    
    @classmethod
    def create_dto(cls):
        # print(f"Create{cls.__name__}DTO", cls.__name__)
        return dto_factory(f"Create{cls.__name__}DTO", cls, exclude=["id"])


class Language(Base, DtoBase):
    __tablename__ = "language"
    id: Mapped[int] = Column(Integer, primary_key=True)
    iso_code: Mapped[str] = Column(String)
    language: Mapped[str] = Column(String, unique=True)

    def __repr__(self) -> str:
        return f"Language(id={self.id!r}, language={self.language!r})"


class Author(Base, DtoBase):
    __tablename__ = "author"
    id: Mapped[int] = Column(Integer, primary_key=True)
    author: Mapped[str] = Column(String, unique=True)

    def __repr__(self) -> str:
        return f"Author(id={self.id!r}, text={self.author!r})"

class Manuscript(Base, DtoBase):
    __tablename__ = "manuscript"
    id: Mapped[int] = Column(Integer, primary_key=True)
    title: Mapped[str] = Column(String, unique=True)

    def __repr__(self) -> str:
        return f"Manuscript(id={self.id!r}, title={self.title!r})"

class Translation(Base,DtoBase):
    __tablename__ = "translation"
    id: Mapped[int] = Column(Integer, primary_key=True)
    sentence_id: Mapped[int] =Column(Integer, ForeignKey("sentence.id", ondelete="CASCADE"))
    sentence: Mapped["Sentence"] = relationship("Sentence", back_populates="translations")
    language_id: Mapped[int] = Column(Integer, ForeignKey("language.id", ondelete="CASCADE"), nullable=False)
    language:Mapped[Language] = relationship("Language",uselist=False)
    text: Mapped[str] = Column(String)

class Sentence(Base, DtoBase):
    __tablename__ = "sentence"
    __table_args__ = (UniqueConstraint("order", "paragraph_id"),)

    id: Mapped[int] = Column(Integer, primary_key=True)
    paragraph_id: Mapped[int] = Column(Integer, ForeignKey("paragraph.id", ondelete="CASCADE"), nullable=False)
    # many to one relationship
    paragraph: Mapped["Paragraph"] = relationship("Paragraph", back_populates="sentences")
    order: Mapped[int] = Column(Integer)
    text: Mapped[str] = Column(String)
    language_id: Mapped[int] = Column(Integer, ForeignKey("language.id", ondelete="CASCADE"), nullable=False)
    language:Mapped[Language] = relationship("Language", uselist=False)
    # one to one relationship
    translations: Mapped[list[Translation]] = relationship("Translation", back_populates="sentence", uselist=True, cascade="all, delete", passive_deletes=True)


class Paragraph(Base, DtoBase):
    __tablename__ = "paragraph"
    __table_args__ = (UniqueConstraint("order", "text_id"),)
    
    id: Mapped[int] = Column(Integer, primary_key=True)
    # one to many relationship
    # text: Mapped[str] = Column(String)
    text_id: Mapped[int] = Column(Integer, ForeignKey("text.id", ondelete="CASCADE"))
    text: Mapped["Text"] = relationship("Text", back_populates="paragraphs")
    sentences: Mapped[list[Sentence]] = relationship("Sentence", back_populates="paragraph", uselist=True, lazy='joined', innerjoin=True, cascade="all, delete", passive_deletes=True)
    order: Mapped[int] = Column(Integer)
    
    
class Text(Base, DtoBase):
    __tablename__ = "text"
    id: Mapped[int] = Column(Integer, primary_key=True)
    title: Mapped[str] = Column(String)
    author_id: Mapped[int] = Column(Integer, ForeignKey("author.id"), nullable=False)
    manuscript_id: Mapped[int] =Column(Integer, ForeignKey("manuscript.id"),nullable=False)
    paragraphs: Mapped[list[Paragraph]] = relationship("Paragraph", back_populates="text", uselist=True, lazy='joined', innerjoin=True, cascade="all, delete", passive_deletes=True)
    author: Mapped[Author] = relationship("Author",uselist=False, lazy='joined')
    manuscript:Mapped[Manuscript] = relationship("Manuscript",uselist=False,lazy='joined')


class ManuscriptModel(BaseModel,DtoBase):
    class Config:
        orm_mode = True

    id: int
    title: str

class AuthorModel(BaseModel,DtoBase):
    class Config:
        orm_mode = True

    id: int
    author: str

class LanguageModel(BaseModel,DtoBase):
    class Config:
        orm_mode = True

    id: int
    Language: str

class TranslationModel(BaseModel,DtoBase):
    class Config:
        orm_mode = True

    id: int
    text: str

class SentenceModel(BaseModel,DtoBase):
    class Config:
        orm_mode = True

    id: int
    order: int
    text : str
    language_id : int
    paragraph_id : int
    translations: list[TranslationModel]

class ParagraphModel(BaseModel,DtoBase):
    class Config:
        orm_mode = True

    id: int
    order: int
    text_id : int
    sentences: list[SentenceModel]

class TextModel(BaseModel,DtoBase):
    class Config:
        orm_mode= True

    id: int
    title: str
    author_id: int
    manuscript_id: int
    paragraphs: list[ParagraphModel]
