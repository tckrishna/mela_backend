# from mela.models.Manuscript import *
# from mela.models.Author import *
# from mela.controller.manuscript import *
# from mela.models.Language import *
# from mela.models.Text import *
# from mela.models.Paragraph import *
# from mela.models.Sentence import *
# from mela.models.Translation import *

# from mela.models.Base import Base
from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import sessionmaker
import json

from mela.models.Models import *

# class Paragraph(Base, DtoBase):
#     __tablename__ = "paragraph"
#     id: Mapped[int] = Column(Integer, primary_key=True)
#     text_id: Mapped[int] = Column(Integer, ForeignKey("text.id"))
#     # one to many relationship
#     # text: Mapped[str] = Column(String)
#     # sentence = relationship("Sentence", back_populates="paragraph",cascade="all, delete, delete-orphan")
#     order: Mapped[int] = Column(Integer)
#     text: Mapped["Text"] = relationship("Text", back_populates="paragraph")
    
# class Text(Base, DtoBase):
#     __tablename__ = "text"
#     id: Mapped[int] = Column(Integer, primary_key=True)
#     title: Mapped[str] = Column(String)
#     # author_id: Mapped[int] = Column(Integer, ForeignKey("author.id", ondelete="CASCADE"), nullable=False)
#     # manuscript_id: Mapped[int] =Column(Integer, ForeignKey("manuscript.id", ondelete="CASCADE"),nullable=False)
#     paragraphs: Mapped[list[Paragraph]] = relationship("Paragraph", back_populates="text", cascade="all, delete, delete-orphan")
#     # author = relationship("Author", back_populates="text")
#     # manuscript = relationship("Manuscript", back_populates="text")

# class ParagraphModel(BaseModel):
#     class Config:
#         orm_mode = True

#     id: int
#     order: str

# class TextModel(BaseModel):
#     class Config:
#         orm_mode= True

#     id: int
#     title: str
#     paragraphs: list[ParagraphModel]


engine = create_engine("postgresql://vagrant:mela@127.0.0.1:5432/mela")
Session = sessionmaker(bind=engine)

my_metadata = Base.metadata

session = Session()
# my_metadata.create_all(engine)

# engine = create_engine("postgresql://vagrant:mela@127.0.0.1:5432/mela")
# Session = sessionmaker(bind=engine)

# my_metadata = Base.Base.metadata

# session = Session()
# my_metadata.create_all(engine)


# inside of a "create the database" script, first create
# tables:

# first_upload = Language(iso_code="639-1", language="english")
# session.add(first_upload)
# first_upload = Text(title="")
# first_upload = Paragraph(text="the first book",order=1)
# session.add(first_upload)
# first_upload = Sentence(paragraph_id=1, order=1, text="This is my first sentence")
# session.add(first_upload)

# session.commit()
# # then, load the Alembic configuration and generate the
# # version table, "stamping" it with the most recent rev:
# from alembic.config import Config
# from alembic import command
# alembic_cfg = Config("/home/vagrant/src/mela/alembic.ini")
# command.stamp(alembic_cfg, "head")

# data = '{"id": 1, "title":"first upload ","author":"author_test1", "manuscript": "ghentcdh", "paragraphs" :[{"id":1, "order": 1,"sentences":[{"order": 1, "text": "First sentence is correctly uploaded with first paragraph", "language_id": 1},{"order": 2, "text": "Second sentence is also uploaded with first paragraph", "language_id":1}]},{"id": 2, "order": 2,"sentences":[{"order": 1, "text": "First sentence is correctly uploaded second paragraph", "language_id": 1},{"order": 2, "text": "Second sentence is also uploaded paragraph", "language_id":1}]}]}'

data = '{"id": 1, "title":"first upload ","author":"author_test1", "manuscript": "ghentcdh", "paragraphs" :[{"id":5, "order": 2,"sentences":[{"order": 1, "text": "First sentence is correctly uploaded with third paragraph", "language_id": 1},{"order": 2, "text": "Second sentence is also uploaded with third paragraph", "language_id":1}]},{"id":1, "order": 3,"sentences":[{"order": 1, "text": "First sentence is correctly uploaded with first paragraph", "language_id": 1},{"order": 2, "text": "Second sentence is also uploaded with first paragraph", "language_id":1}]},{"id": 2, "order":1,"sentences":[{"order": 1, "text": "First sentence is correctly uploaded second paragraph", "language_id": 1},{"order": 2, "text": "Second sentence is also uploaded paragraph", "language_id":1}]}]}'


# session.add(Language(language="english", iso_code="asdafff"))
# session.commit()

def add_text(session, text_object):
    """
    json structure: {
        {
            author:
            manuscript:
            paragraphs :
            [
                0:{
                    order:
                    sentences:[
                        {
                            order:
                            text :
                            language :
                            translations : [
                                {

                                }
                            ]
                        }
                    ]
                }
            ]

        }
    }
    """
    text = json.loads(text_object)
    paragraphs = text["paragraphs"]

    # session.add(Language(language="english", iso_code="asdafff"))
    # session.commit()
    upload_text = Text(title = text["title"], author = Author(author=text["author"]), manuscript = Manuscript(title=text["manuscript"]))
    # upload_text = Text(title = text["title"])
    session.add(upload_text)
    for paragraph in paragraphs:
        upload_paragraph = Paragraph(order=paragraph["order"])
        for sentence in paragraph["sentences"]:
            upload_paragraph.sentences.append(Sentence(order=sentence["order"],text=sentence["text"], language_id=sentence["language_id"]))
        
        upload_text.paragraphs.append(upload_paragraph)
        
    session.add(upload_text)

    session.commit()

def put_text(session, text_object):

    """
    """

    text = json.loads(text_object)
    paragraphs = text["paragraphs"]

    current_text = session.execute(select(Text).where(Text.id == text["id"])).unique().scalar_one()

    ### Check if new paragraph is added 
    if len(paragraphs) == len(current_text.paragraphs):
        ### no new paragraph is added
        for paragraph in paragraphs:
            for i in range(len(current_text.paragraphs)):
                if current_text.paragraphs[i].id == paragraph["id"]:
                    if len(paragraph.sentences) == len(current_text.paragraphs[i].sentences):
                        ### no new paragraph is added
                        for sentence in current_text.paragraphs[i].sentences:
                            for j in range(len(current_text.paragraphs[i].sentences)):
                                if current_text.paragraphs[i].sentences[j].id == sentence["id"]:
                                    current_text.paragraphs[i].sentences[j].order = sentence["order"]
                                    current_text.paragraphs[i].sentences[j].text = sentence["text"]

      
    #     upload_text.paragraphs.append(upload_paragraph)
        
    # session.add(upload_text)

    session.commit()

def delete_text(session, delete_id):
    """


    """

    session.execute(delete(Text).where(Text.id == delete_id))

    session.commit()    


def add_paragraph(session, text_object):
    """
    """

    text = json.loads(text_object)
    paragraphs = text["paragraphs"]

    # session.add(Language(language="english", iso_code="asdafff"))
    # session.commit()
    current_text = session.execute(select(Text).where(Text.id == text["id"])).unique().scalar_one()

    for paragraph in paragraphs:
        if paragraph.get("id") is None:
            upload_paragraph = Paragraph(order=paragraph["order"])
            for sentence in paragraph["sentences"]:
                upload_paragraph.sentences.append(Sentence(order=sentence["order"],text=sentence["text"], language_id=sentence["language_id"]))
        
            current_text.paragraphs.append(upload_paragraph)
        
    # # session.add(upload_text)

    session.commit()

def reorder_paragraphs(session, text_object, text_id):
    """
    """
    text = json.loads(text_object)
    paragraphs = text["paragraphs"]

    current_text = session.execute(select(Text).where(Text.id == text_id)).unique().scalar_one()

    ### first put the values to NULL 

    for i in range(len(current_text.paragraphs)):
        current_text.paragraphs[i].order = None

    session.commit()

    ### Then update with the new order

    for paragraph in paragraphs:
        for i in range(len(current_text.paragraphs)):
            if current_text.paragraphs[i].id == paragraph["id"]:
                current_text.paragraphs[i].order = paragraph["order"]

    session.commit()

    return []

def delete_paragraph(session, delete_id):
    """
    """
    session.execute(delete(Paragraph).where(Paragraph.id == delete_id))

    # ## re-order
    # current_text = session.execute(select(Text).where(Text.id == text["id"])).unique().scalar_one()

    session.commit()



def reorder_sentence(session, paragraph_object):
    """

    """
    paragraph = json.loads(paragraph_object)
    sentences = paragraph["sentences"]

    current_paragraph= session.execute(select(Paragraph).where(Paragraph.id == paragraph["id"])).unique().scalar_one()

    ### first put the values to NULL 

    for i in range(len(current_paragraph.sentences)):
        current_paragraph.sentences[i].order = None

    session.commit()

    ### Then update with the new order

    for sentence in sentences:
        for i in range(len(current_paragraph.sentences)):
            if current_paragraph.sentences[i].id == sentence["id"]:
                current_paragraph.sentences[i].order = sentence["order"]

    # ### no new paragraph is added
    # for paragraph in paragraphs:
    #     for i in range(len(current_text.paragraphs)):
    #         if current_text.paragraphs[i].id == paragraph["id"]:
    #             for sentence in current_text.paragraphs[i].sentences:
    #                 for j in range(len(current_text.paragraphs[i].sentences)):
    #                     if current_text.paragraphs[i].sentences[j].id == sentence["id"]:
    #                         current_text.paragraphs[i].sentences[j].order = sentence["order"]
    #                         current_text.paragraphs[i].sentences[j].text = sentence["text"]


    session.commit()


def delete_sentence(session, delete_id):
    """
    """

    session.execute(delete(Sentence).where(Sentence.id == delete_id))
    session.commit()

def add_translation(session, text_object, paragraph_id):
    text = json.loads(text_object)

    paragraph = next(paragraph for paragraph in text["paragraphs"] if paragraph["id"] == paragraph_id) 
    current_paragraph= session.execute(select(Paragraph).where(Paragraph.id == paragraph["id"])).unique().scalar_one()
    
    ## Adding new translation (expects only new elements to be added in the object)

    for sentence in paragraph["sentences"]:
        for i in range(len(current_paragraph)):
            if (sentence["id"] == current_paragraph.id):
                sentence[i].translation.append(Translation(language_id = sentence[i]["translation"][0]["language_id"], text = sentence[i]["translation"][0]["text"]))


# add_text(session,data)
# add_paragraph(session,data)
reorder_paragraphs(session,data)
# delete_paragraph(session,data,4)


