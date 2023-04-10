from starlite import Starlite,HTTPException, Body
from starlite.handlers import get, post, patch, delete, put
from starlite.status_codes import HTTP_404_NOT_FOUND
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from mela.models.Models import *


@get("/get_paragraph/{text_id:int}")
async def get_paragraph(text_id: int, async_session: AsyncSession) -> Text:
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


@post("/post_paragraph")
async def create_new_paragraph(async_session: AsyncSession, data: dict = Body()) -> Text:
    """ 
    

    """

    text = data
    paragraphs = text["paragraphs"]
    
    current_text = async_session.execute(select(Text).where(Text.id == text["id"])).unique().scalar_one()

    for paragraph in paragraphs:
        if paragraph.get("id") is None:
            upload_paragraph = Paragraph(order=paragraph["order"])
            for sentence in paragraph["sentences"]:
                upload_paragraph.sentences.append(Sentence(order=sentence["order"],text=sentence["text"], language_id=sentence["language_id"]))
        
            current_text.paragraphs.append(upload_paragraph)

    await async_session.commit()

    return text

@put("/reorder_paragraphs/{text_id:int}")
async def reorder_paragraphs(async_session: AsyncSession, text_id:int, data: dict = Body()) -> None:
    """
    
    
    """
    text = data
    paragraphs = text["paragraphs"]
    
    current_text = async_session.execute(select(Text).where(Text.id == text_id)).unique().scalar_one()

    ### first put the values to NULL 

    for i in range(len(current_text.paragraphs)):
        current_text.paragraphs[i].order = None

    await async_session.commit()

    ### Then update with the new order

    for paragraph in paragraphs:
        for i in range(len(current_text.paragraphs)):
            if current_text.paragraphs[i].id == paragraph["id"]:
                current_text.paragraphs[i].order = paragraph["order"]

    await async_session.commit()
    
    return None

@delete("/delete_paragraph/{paragraph_id:int}")
async def delete_paragraph(paragraph_id: int, async_session: AsyncSession) -> None:

    async_session.execute(delete(Paragraph).where(Paragraph.id == paragraph_id))

    await async_session.commit()

    return None