from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from notifications.servicies import NotificationsService


router = Router()

class NotificationState(StatesGroup):
    symbol = State()
    target_price = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет с помощью этого бота ты можешь создавать уведомления о достижении криптовалютой указанной цены.")


@router.message(Command("notification"))
async def choose_symbol(message: Message, state: FSMContext):
    await state.set_state(NotificationState.symbol)
    await message.answer("Введите символ криптовалюты")


@router.message(NotificationState.symbol)
async def choose_symbol(message: Message, state: FSMContext):
    await state.update_data(symbol=message.text)
    await state.set_state(NotificationState.target_price)
    await message.answer("Введите цену при достижении которой вас нужно оповестить")

    
@router.message(NotificationState.target_price)
async def choose_symbol(message: Message, state: FSMContext):
    await state.set_state(NotificationState.symbol)
    data = await state.get_data()
    await NotificationsService().add_new_notification(
        telegram_id=message.from_user.id,
        symbol=data["symbol"],
        target_price=message.text
    )
    await message.answer(f"При достижении {data["symbol"]} цены {message.text} вам придет сообщение.")
    await state.clear()

