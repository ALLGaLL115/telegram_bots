import aiohttp

from config import settings
from pydantic import BaseModel
from typing import Optional, List, Union

class USD(BaseModel):
    price: float

class Quote(BaseModel):
    USD: USD

class Coin(BaseModel):
    name: str
    quote: Quote

class DataModel(BaseModel):
    name: str
    data: List[Coin]
    



base_url = "https://pro-api.coinmarketcap.com"

headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': settings.COIN_MARKET_TOKEN,
            
            }

class CoinMarkteCapAPI:


    async def get_symbols_curent_price(self, session: aiohttp.ClientSession, symbols: list[str] ):
        
        try: 
            params = {
                'symbol': ",".join(symbols)
            }
            
            async with session.get(base_url+"/v1/cryptocurrency/quotes/latest", 
                                headers=headers, params=params) as response:
                
                result_json = await response.json()
                data = []
                for k in result_json["data"].keys():
                    data.append({
                        k: result_json["data"]["BTC"]["quote"]["USD"]["price"]
                    })

              

            return data

        except Exception as e: 
            print(e)

