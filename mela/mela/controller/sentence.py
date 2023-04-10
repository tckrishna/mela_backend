from starlite import get, post
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# from mela.models.Sentence import Sentence

# @get("/sentences")
# async def get_sentence(async_session: AsyncSession) -> list[Sentence]:
#     """Handler function that returns a text and manuscript"""

#     return list(await async_session.scalars(select(Sentence)))

# @post("/post_sentence")
# async def post_sentence(async_session: AsyncSession, data: Sentence.create_dto()) -> Sentence:
#     """Handler function that puts sentence into the database table"""
#     sentence: Sentence = data.to_model_instance()

#     async_session.add(sentence)
#     await async_session.commit()

#     return sentence
