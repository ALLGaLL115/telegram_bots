from typing import Annotated
import aiohttp
from fastapi import Depends
import pytest
import pytest_asyncio

from notifications.api import CoinMarketCapAPI




async def test_add_notification():
        
        response = await CoinMarketCapAPI().get_curent_prices(["BTC", "ETH"])
        print(response)
        assert 1 == 1
        
