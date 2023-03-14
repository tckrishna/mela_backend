from starlite import get, post
from mela.controller.database import dto_factory
from sqlalchemy import select
from mela.models.manuscript import Manuscript
from sqlalchemy.ext.asyncio import AsyncSession

CreateManuscriptDTO = dto_factory("CreateManuscriptDTO", Manuscript, exclude=["id"])

@get("/manuscripts")
async def get_manuscripts(async_session: AsyncSession) -> list[Manuscript]:
    """Handler function that returns a text and manuscript"""

    return list(await async_session.scalars(select(Manuscript)))

@post("/post_manuscript")
async def post_manuscript(async_session: AsyncSession, data: CreateManuscriptDTO) -> Manuscript:
    """Handler function that puts manuscript into the database table"""
    manuscript: Manuscript = data.to_model_instance()

    async_session.add(manuscript)
    await async_session.commit()

    return manuscript