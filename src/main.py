import asyncio

from config import settings

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from notifications.handlers import router as price_notification_router

# All handlers should be attached to the Router (or Dispatcher)

bot = Bot(token=settings.BOT_TOKEN,)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет для подробной информации отправь /help")



async def main() -> None:

    dp.include_router(price_notification_router)

    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())

