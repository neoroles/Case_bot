from aiogram.types import CallbackQuery

from data import config
from loader import dp


@dp.callback_query_handler(text='stat_and_advertisement', user_id=config.admins)
async def stat_and_advertisement(call: CallbackQuery):
    await call.answer('Пока не доступно')