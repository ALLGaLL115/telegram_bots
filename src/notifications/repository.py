from notifications.models import Notifications
from utils.repository import SQLAlchemyRepository


class NotificationsRepository(SQLAlchemyRepository):
    model : Notifications

