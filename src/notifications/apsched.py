import json
import os
from aiogram import Bot

from notifications.api import CoinMarketCapAPI
from notifications.schemas import NotificationSchema
from utils.uow import IUnitOfWork, UnitOfWork


tracable_file_path = "tracable_crypto.json"
uow = UnitOfWork()

async def send_ready_alerts(bot: Bot):

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
        mailing = await uow.notifications.delete_executed_notifications(data=data["data"])
        await uow.commit()

    for i in data: 
        await bot.send_message(i.telegram_id, f"Цена {i.symbol} достигла значения {i.target_price}. Начальная цена {i.initial_price}")

 
