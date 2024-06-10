from pydantic import BaseModel


class NotificationSchema(BaseModel):
    id: int
    telegram_id: int
    symbol: str
    initial_price: float
    target_price: float


