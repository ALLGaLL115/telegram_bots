# from notifications.api import CoinMarketCapAPI

from notifications.api import CoinMarketCapAPI
from notifications.servicies import NotificationsService
from utils.uow import UnitOfWork


async def test_get_curent_prices():
    response = await CoinMarketCapAPI().get_curent_prices(["BTC"])
    assert response["data"]["BTC"]["name"] == 'Bitcoin'


async def test_add_notification():
    uow = UnitOfWork()
    result = await NotificationsService().add_new_notification(uow=uow, telegram_id=123123, symbol="BTC", target_price=1234.2)
    assert result == 'success'


async def test_update_prices():
    uow = UnitOfWork()
    result = await NotificationsService().update_prices()
    assert result == "success"
