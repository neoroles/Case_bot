from aiogram.types import CallbackQuery

from data import config
from keyboards.inline.admins.other.keyboard_drawing import draw
from loader import dp, db, bot


@dp.callback_query_handler(text='draw')
async def drawing(call: CallbackQuery):
    await call.answer('Принял', show_alert=True)

