from typing import Annotated
import aiohttp
from fastapi import Depends
import pytest

from notifications.services import NotificationService
from utils.uow import IUnitOfWork, UnitOfWork



async def test_add_notification():


    unitOfWork = UnitOfWork()
    async with aiohttp.ClientSession() as session:
        async with session:
            result = await NotificationService().add_notification(unitOfWork, session, 
                telegram_id=7479635804, symbol="BTC", target_price=123
            )
            assert result == "success"