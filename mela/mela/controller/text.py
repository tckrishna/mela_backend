from starlite import Starlite,HTTPException, Body
from starlite.handlers import get, post, patch, delete, put
from starlite.status_codes import HTTP_404_NOT_FOUND
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from mela.models.Models import *
# from mela.models.Text import Text

# @get("/text")
# async def get_texts(async_session: AsyncSession) -> list[Text]:
#     """Handler function that returns a text and manuscript"""

#     print (list(await async_session.scalars(select(Text))))

#     return []

# @post("/post_manuscript")
# async def post_manuscript(async_session: AsyncSession, data: Manuscript.create_dto()) -> Manuscript:
#     """Handler function that puts manuscript into the database table"""
#     manuscript: Manuscript = data.to_model_instance()

#     async_session.add(manuscript)
#     await async_session.commit()

#     return manuscript

@get("/get_text/{text_id:int}")
async def get_text(text_id: int, async_session: AsyncSession) -> Text:
    """Handler function that returns a text and manuscript"""

    scalar_result = await async_session.scalars(select(Text). \
                                            options(joinedload(Text.paragraphs)). \
                                            where(Text.id == text_id))   


    text: Text | None = next(scalar_result.unique())

    result_dict = text.to_dict()

    result_dict['paragraphs'] = []
    for i in range(len(text.paragraphs)):
        serialize_paragraph = text.paragraphs[i].to_dict()
        serialize_sentence = []
        for j in range(len(text.paragraphs[i].sentences)):
            serialize_sentence.append(text.paragraphs[i].sentences[j].to_dict())
        # print(serialize_sentence)
        serialize_paragraph['sentences'] = serialize_sentence

        result_dict['paragraphs'].append(serialize_paragraph)

    # print(result_dict)

    if not text:
        raise HTTPException(detail=f"User with ID {text} not found", status_code=HTTP_404_NOT_FOUND)

    return result_dict


@post("/post_text")
async def create_new_text(async_session: AsyncSession, data: dict = Body()) -> Text:
    """ 
    

    """

    text = data
    paragraphs = text["paragraphs"]

    upload_text = Text(title = text["title"], author = Author(author=text["author"]), manuscript = Manuscript(title=text["manuscript"]))
    
    for paragraph in paragraphs:
        upload_paragraph = Paragraph(order=paragraph["order"])
        for sentence in paragraph["sentences"]:
            upload_paragraph.sentences.append(Sentence(order=sentence["order"],text=sentence["text"], language_id=sentence["language_id"]))
        
        upload_text.paragraphs.append(upload_paragraph)
        
    async_session.add(upload_text)

    await async_session.commit()

    return text

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

@delete("/delete_text/{text_id:int}")
async def delete_text(text_id: int, async_session: AsyncSession) -> None:

    async_session.execute(delete(Text).where(Text.id == text_id))

    await async_session.commit()
