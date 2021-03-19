from aiogram.types import CallbackQuery

from data.config import admins
from loader import dp, bot


@dp.callback_query_handler(text='requisites', user_id=admins)
async def requisites(call: CallbackQuery):
    await call.answer('Недоступно')