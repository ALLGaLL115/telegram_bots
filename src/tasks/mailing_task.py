import json
import os
from aiogram import Bot
from celery import Celery

from config import settings
from notifications.api import CoinMarketCapAPI
from notifications.schemas import NotificationSchema
from utils.uow import UnitOfWork


celery_app = Celery('tasks', broker="redis://localhost:6379")

tracable_file_path = "tracable_crypto.json"
uow = UnitOfWork()
bot = Bot(token=settings.BOT_TOKEN)

@celery_app.task
async def send_ready_alerts():

    if not os.path.exists(tracable_file_path):
        with open(tracable_file_path, 'w') as file:
            json.dump({"symbols":[], "data": {}}, file, indent=4)
            return None
    elif os.path.getsize(tracable_file_path) == 0:
        with open(tracable_file_path, 'w') as file:
            json.dump({"symbols":[], "data": {}}, file, indent=4)
            return None

    with open(tracable_file_path, 'r') as file:
        data = json.load(file)

    current_data = await CoinMarketCapAPI().get_curent_prices(symbols=data["symbols"])
    data["data"] = [{k:v["quote"]["USD"]["price"]} for k, v in current_data["data"].items()]

    with open(tracable_file_path, "w") as file:
        json.dump(data, file, indent=4)

    async with uow:
        notifications_chemas: list[NotificationSchema] = await uow.notifications.get_and_delete_suitable_notifications(data=data["data"])
        for i in notifications_chemas: 
            await bot.send_message(i.telegram_id, f"Цена {i.symbol} достигла значения {i.target_price}. Начальная цена {i.initial_price}")

        await uow.commit()


celery_app.conf.beat_schedule = {
    'check_notifications_every 10 seconds':{
        'task':'tasks.send_ready_alerts',
        'schedul':5
    }
}
