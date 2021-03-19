from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.config import admins
from keyboards.inline.admins.systems.main import key_systems
from loader import dp, bot, db
from states.admin_state import WinPercent


@dp.callback_query_handler(text='sys_setting', user_id=admins)
async def sys_setting(call: CallbackQuery):
    await call.answer()
    text = 'Тут системные настройки'
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=key_systems)


@dp.callback_query_handler(text='sys_setting', user_id=admins, state=WinPercent)
async def sys_setting(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.finish()
    text = 'Тут системные настройки'
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=key_systems)