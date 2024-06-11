import asyncio
import json
import logging
from typing import List

import aiohttp
from pydantic import BaseModel
from config import settings



from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from notifications.servicies import NotificationsService
from utils.uow import UnitOfWork

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from notifications import apshed

# from notifications.handlers import router as price_notification_router

# All handlers should be attached to the Router (or Dispatcher)
bot = Bot(token=settings.BOT_TOKEN,)


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет для подробной информации отправь /help")



async def main() -> None:
    res = await NotificationsService().add_new_notification(uow = UnitOfWork(), telegram_id=2123, symbol="BTC", target_price=1231)
    print(res)
#     dp.include_router(price_notification_router)

#     await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


# class USD(BaseModel):
#     price: float

# class Quote(BaseModel):
#     USD: USD

# class Coin(BaseModel):
#     name: str
#     quote: Quote

# class DataModel(BaseModel):
#     name: str
#     data: List[Coin]



# base_url = "https://pro-api.coinmarketcap.com"

# logging.basicConfig(filename="noti.log", filemode="w")
# headers = {
#             'Accepts': 'application/json',
#             'X-CMC_PRO_API_KEY': settings.COIN_MARKET_TOKEN,
            
#             }

# params = {
#             'symbol': "BTC,ETH"
#         }
