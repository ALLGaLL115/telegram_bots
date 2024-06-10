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

# async def main():
#     async with aiohttp.ClientSession() as session:




#         async with session.get(base_url+"/v1/cryptocurrency/quotes/latest", 
#                                headers=headers,
#                                params=params
#                                ) as response:
#             curent_price = await response.json()
#             with open("train.json", "w", encoding="UTF-8") as filee:
#                 json.dump( curent_price, filee, indent=4 )
            
            
#             # ["1"]["quote"]["usdt"]["price"]

# def somee():

#     with open("train.json", "r", ) as file:
      
#             curent_prices =  json.load(file)
#             # print(curent_prices)

#             a = {k: curent_prices["data"]["BTC"]["quote"]["USD"]["price"] for k in curent_prices["data"].keys()}

#             print(a)
            

#             # data_list: list[DataModel]
#             # for i in curent_prices['data'].keys():
#             #     data_list.append(DataModel(name=i, data=curent_prices['data'][i] ))



#             # print([i.model_dump() for i in data_list])

# def dd():
#      with open("train.json", "r", ) as file:
      
#             curent_prices =  json.load(file)

#             print(type(curent_prices))
if __name__=="__main__":
    asyncio.run(main())
    # somee()
    # dd()

    
   