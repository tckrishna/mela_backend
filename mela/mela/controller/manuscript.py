from starlite import get, post
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from mela.models.Manuscript import Manuscript, ManuscriptModel

@get("/manuscripts")
async def get_manuscripts(async_session: AsyncSession) -> list[ManuscriptModel]:
    """Handler function that returns a text and manuscript"""
    result = await async_session.scalars(select(Manuscript))

    manuscripts = result.all()
    print (manuscripts)

    return manuscripts

@post("/post_manuscript")
async def post_manuscript(async_session: AsyncSession, data: Manuscript.create_dto()) -> ManuscriptModel:
    """Handler function that puts manuscript into the database table"""
    manuscript: Manuscript = data.to_model_instance()

    async_session.add(manuscript)
    await async_session.commit()

    return manuscript
