from sqlalchemy import and_, delete
from notifications.models import Notifications
from notifications.schemas import NotificationSchema
from utils.repository import SQLAlchemyRepository


class NotificationsRepository(SQLAlchemyRepository):
    model = Notifications

    async def get_and_delete_suitable_notifications(self, data: dict):
        mailing: NotificationSchema = []
        for k, v in data['data'].keys():
            stmt = delete(self.model).where(
                and_(
                    self.model.c.symbol == k,
                    (
                        (self.model.c.initial_price < v) & (v <= self.model.c.initial_price) |
                        (self.model.c.initial_price > v) & (v >= self.model.c.initial_price)
                    )
                )
            )   

            res = await self.session.execute(stmt)
            res = [i.convert_to_model for i in res.scalars().all()]
            mailing.extend(res)
            
        return mailing