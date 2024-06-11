import asyncio
from datetime import timezone
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
from notifications import apsched

from notifications.handlers import router as price_notification_router

# All handlers should be attached to the Router (or Dispatcher)
bot = Bot(token=settings.BOT_TOKEN,)


dp = Dispatcher()

scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
scheduler.add_job(apsched.send_ready_alerts, trigger="interval", seconds=5, kwargs={'bot':bot})
scheduler.start()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет для подробной информации отправь /help")



async def main() -> None:

    dp.include_router(price_notification_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

