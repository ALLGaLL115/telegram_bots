from abc import ABC
from database import Base
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
import logging

logger = logging.getLogger(__name__)


class ISQLAlchemyRepository(ABC):


    async def get():
        raise NotImplemented
    

    async def get_all():
        raise NotImplemented


    async def create():
        raise NotImplemented
    

    async def update():
        raise NotImplemented
    

    async def delete():
        raise NotImplemented
    

class SQLAlchemyRepository(ISQLAlchemyRepository):


    model = None


    def __init__(self, session: AsyncSession):
        self.session = session


    async def get(self, id: int):
        stmt = select(self.model).filter_by(id=id)
        res = await self.session.execute(stmt)
        res = res.scalar_one()
        return res.convert_to_model()


    async def get_all(self, **filters):
        stmt = select(self.model).filter_by(**filters)
        res = await self.session.execute(stmt)
        res = res.scalars().all()
        return [i.convert_to_model() for i in res]


    async def create(self, **data):
        try: 
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await self.session.execute(stmt)
            res = res.scalar_one()
            return res
        except Exception as e:
            logger.error(e)
            raise

    async def update(self, id: int, **data):
        stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model.id)
        res = await self.session.execute(stmt)
        res = res.scalar_one()
        return res


    async def delete(self, id:int):
        stmt = delete(self.model).filter_by(id=id).returning(self.model.id)
        res = await self.session.execute(stmt)
        res = res.scalar_one()
        return res 


    