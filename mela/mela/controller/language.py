from starlite import get, post
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from mela.models.Models import *

@get("/languages")
async def get_languages(async_session: AsyncSession) -> list[Language]:
    """Handler function that returns a text and language"""
    result = await async_session.scalars(select(Language))

    languages = result.all()
    # print (languages)

    return languages

@post("/post_language")
async def post_language(async_session: AsyncSession, data: Language.create_dto()) -> LanguageModel:
    """Handler function that puts language into the database table"""
    language: Language = data.to_model_instance()

    async_session.add(language)
    await async_session.commit()

    return language