import os
import json
import logging
from notifications.api import CoinMarketCapAPI
from utils.uow import IUnitOfWork


logger = logging.getLogger(__name__)

log_format = "%(asctime)s - %(filename)s - %(lineno)s - %(levelname)s - %(message)s"
log_formater = logging.Formatter(log_format, style="%")

developing_handler = logging.StreamHandler()
developing_handler.setFormatter(log_formater)

product_handler = logging.FileHandler("product_handler.log")
product_handler.setFormatter(log_formater)


logger.addHandler(product_handler)
logger.addHandler(developing_handler)

tracable_file_path = "tracable_crypto.json"

class NotificationsService:


    async def add_new_notification(self, uow: IUnitOfWork, telegram_id: int, symbol: str, target_price: float):
        if not os.path.exists(tracable_file_path):
            with open(tracable_file_path, 'w') as file:
                json.dump({"symbols":[], "data": {}}, file, indent=4)
        elif os.path.getsize(tracable_file_path) == 0:
            with open(tracable_file_path, 'w') as file:
                json.dump({"symbols":[], "data": {}}, file, indent=4)

        with open(tracable_file_path, "r") as file:
            data = json.load(file)

        if symbol in data["symbols"]:
            current_price = data["data"][symbol]
        else: 
            response_json = await CoinMarketCapAPI().get_curent_prices([symbol])
            current_price = response_json["data"]["BTC"]["quote"]["USD"]["price"]
            print(data)
            data["symbols"].append(symbol)
            print(data)
            data["data"][symbol] = current_price
            with open(tracable_file_path, "w") as file:
                json.dump(data, file, indent=4)
        async with uow:
            res= await uow.notifications.create(
                telegram_id = telegram_id, 
                symbol = symbol, 
                target_price = target_price, 
                initial_price = current_price )
            await uow.commit()
            return "success"
            




