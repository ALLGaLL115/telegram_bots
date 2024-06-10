import aiohttp

host = "https://pro-api.coinmarketcap.com"

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '18f9d072-ab45-4bc2-b241-adc0cccaafdb',
}



    

class CoinMarketCapAPI:

    
    async def get_curent_prices(self, symbols: list):
        params = {
            'symbol': ",".join(symbols)
        }
        async with aiohttp.ClientSession(base_url=host, headers=headers) as session:
            response = await session.get(url="/v1/cryptocurrency/quotes/latest",
                                              params=params )

        return await response.json()

        