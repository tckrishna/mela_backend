from starlite import Starlite, get, HTTPException,post, put, Body
from mela.settings import sqlalchemy_plugin

# from mela.controller.manuscript import *
# from mela.controller.sentence import *
from mela.controller.text import *
from mela.controller.language import *
from mela.controller.paragraph import *
from sqlalchemy.orm import Mapped,relationship, selectinload, subqueryload,joinedload, contains_eager
from sqlalchemy import Column, Integer, String, ForeignKey, select
from mela.models.Base import Base, DtoBase
from mela.models.Models import *
# from mela.models.Author import *
# from mela.models.Manuscript import *

# from mela.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

from pydantic import BaseModel

from sqlalchemy.ext.asyncio import AsyncSession

from starlite.status_codes import HTTP_404_NOT_FOUND

# from mela.models.Paragraph import *

# from starlite.plugins.sql_alchemy import SQLAlchemyConfig, SQLAlchemyPlugin
# from starlite import DTOFactory
# from pydantic import BaseSettings

# class AppSettings(BaseSettings):
#     DATABASE_URI: str = "postgresql+asyncpg://vagrant:mela@127.0.0.1:5432/mela"

# settings = AppSettings()
# sqlalchemy_config = SQLAlchemyConfig(connection_string=settings.DATABASE_URI, dependency_key="async_session")
# sqlalchemy_plugin = SQLAlchemyPlugin(config=sqlalchemy_config)

# dto_factory = DTOFactory(plugins=[sqlalchemy_plugin])



engine = create_engine("postgresql://vagrant:mela@127.0.0.1:5432/mela")
Session = sessionmaker(bind=engine)

# class Paragraph(Base):
#     __tablename__ = "paragraph"
#     id: Mapped[int] = Column(Integer, primary_key=True)
#     # one to many relationship
#     # text: Mapped[str] = Column(String)
#     # sentence = relationship("Sentence", back_populates="paragraph",cascade="all, delete, delete-orphan")
#     order: Mapped[int] = Column(Integer)
#     text: Mapped["Text"] = relationship("Text", back_populates="paragraphs", uselist=True)
#     text_id: Mapped[int] = Column(Integer, ForeignKey("text.id"))
    
# class Text(Base):
#     __tablename__ = "text"
#     id: Mapped[int] = Column(Integer, primary_key=True)
#     title: Mapped[str] = Column(String)
#     # author_id: Mapped[int] = Column(Integer, ForeignKey("author.id", ondelete="CASCADE"), nullable=False)
#     # manuscript_id: Mapped[int] =Column(Integer, ForeignKey("manuscript.id", ondelete="CASCADE"),nullable=False)
#     paragraphs: Mapped[list[Paragraph]] = relationship("Paragraph", back_populates="text", uselist=True, lazy='joined')
#     # author = relationship("Author", back_populates="text")
#     # manuscript = relationship("Manuscript", back_populates="text")

# class ParagraphModel(BaseModel):
#     class Config:
#         orm_mode = True

#     id: int
#     order: int

# class TextModel(BaseModel):
#     class Config:
#         orm_mode= True

#     id: int
#     title: str
#     paragraphs: list[ParagraphModel]

# session = Session()
# my_metadata = Base.metadata
# my_metadata.create_all(engine)

# def on_startup() -> None:
#     """Initialize the database."""
#     Base.metadata.create_all(engine)
#     # with Session(engine) as session:
#     #     peter = User(id=1, name="Peter", pets=[Pet(id=1, name="Paul")])
#     #     session.add(peter)
#     #     session.commit()

# @get("/text/{text_id:int}")
# async def get_text(text_id: int, async_session: AsyncSession) -> Text:
#     """Handler function that returns a text and manuscript"""

#     # print ()
#     scalar_result = await async_session.scalars((select(Text).where(Text.id == text_id)).options(subqueryload(Text.paragraphs)))

#     text: Text | None = scalar_result.one_or_none()

#     # print(text)

#     # print(text.manuscript_id)
#     # print(text.title)
#     # print(text.paragraphs[0].sentences[0])

#     # print (TextModel.from_orm(text))

#     if not text:
#         raise HTTPException(detail=f"User with ID {text} not found", status_code=HTTP_404_NOT_FOUND)
    
#     return TextModel.from_orm(text)
    
    # return text

# @get("/get_text/{text_id:int}")
# async def get_text(text_id: int, async_session: AsyncSession) -> Text:
#     """Handler function that returns a text and manuscript"""

#     scalar_result = await async_session.scalars(select(Text). \
#                                             options(joinedload(Text.paragraphs)). \
#                                             where(Text.id == text_id))   


#     text: Text | None = next(scalar_result.unique())

#     result_dict = text.to_dict()

#     result_dict['paragraphs'] = []
#     for i in range(len(text.paragraphs)):
#         serialize_paragraph = text.paragraphs[i].to_dict()
#         serialize_sentence = []
#         for j in range(len(text.paragraphs[i].sentences)):
#             serialize_sentence.append(text.paragraphs[i].sentences[j].to_dict())
#         # print(serialize_sentence)
#         serialize_paragraph['sentences'] = serialize_sentence

#         result_dict['paragraphs'].append(serialize_paragraph)

#     # print(result_dict)

#     if not text:
#         raise HTTPException(detail=f"User with ID {text} not found", status_code=HTTP_404_NOT_FOUND)

#     return result_dict


# @post("/post_text")
# async def create_new_text(async_session: AsyncSession, data: dict = Body()) -> Text:
#     """ 
    

#     """

#     text = data
    
#     paragraphs = text["paragraphs"]

#     upload_text = Text(title = text["title"], author = Author(author=text["author"]), manuscript = Manuscript(title=text["manuscript"]))
#     for paragraph in paragraphs:
#         upload_paragraph = Paragraph(order=paragraph["order"])
#         for sentence in paragraph["sentences"]:
#             upload_paragraph.sentences.append(Sentence(order=sentence["order"],text=sentence["text"], language_id=sentence["language_id"]))
        
#         upload_text.paragraphs.append(upload_paragraph)
        
#     async_session.add(upload_text)

#     await async_session.commit()

#     return text


# @put("/put_text")
# async def edit_text(async_session: AsyncSession, data: dict = Body()) -> Text:
#     """
    

#     """

#     text = data
    
#     paragraphs = text["paragraphs"]


#     upload_text = Text(id=text['id'], title = text["title"], author = Author(author=text["author"]), manuscript = Manuscript(title=text["manuscript"]))
#     for paragraph in paragraphs:
#         upload_paragraph = Paragraph(order=paragraph["order"])
#         for sentence in paragraph["sentences"]:
#             upload_paragraph.sentences.append(Sentence(order=sentence["order"],text=sentence["text"], language_id=sentence["language_id"]))
        
#         upload_text.paragraphs.append(upload_paragraph)
        
#     async_session.add(upload_text)

#     print (upload_text)

#     await async_session.commit()

#     return text


# @get("/texts}")
# async def get_texts(async_session: AsyncSession) -> list[TextModel]:
#     """Handler function that returns a text and manuscript"""

#     # print ()
#     text: list[Text] | None = (await async_session.scalars(select(Text).options(subqueryload(Text.paragraphs)))).all()

#     print (text)

#     # if not text:
#     #     raise HTTPException(detail=f"User with ID {text} not found", status_code=HTTP_404_NOT_FOUND)

#     return list(TextModel.from_orm(text))





@get("/")
def hello_world() -> dict[str, str]:
    """Handler function that returns a greeting dictionary."""
    return {"hello": "world"}

app = Starlite(
    route_handlers=[hello_world, get_text, create_new_text, delete_text, get_paragraph, create_new_paragraph, delete_paragraph, get_languages],
    plugins=[sqlalchemy_plugin],
    debug=True,
)