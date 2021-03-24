from aiogram.types import CallbackQuery

from data.config import admins
from loader import dp, bot, db


@dp.callback_query_handler(text='partner', user_id=admins)
async def partner(call: CallbackQuery):
    await call.answer('Недоступно')