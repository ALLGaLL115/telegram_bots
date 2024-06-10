from database import Base
from sqlalchemy.orm import Mapped, mapped_column

from notifications.schemas import NotificationSchema



class Notifications(Base):
    __tablename__="notifications"
    id: Mapped[int] = mapped_column(primary_key= True)
    telegram_id: Mapped[int] = mapped_column(nullable=False)
    symbol: Mapped[str] = mapped_column(nullable=False)
    initial_price: Mapped[float] = mapped_column(nullable=False)
    target_price: Mapped[float] = mapped_column(nullable=False)

    def convert_to_model(self):
        return NotificationSchema(
            id = self.id,
            telegram_id = self.telegram_id,
            symbol = self.symbol,
            initial_price = self.initial_price,
            target_price = self.target_price,
        )
