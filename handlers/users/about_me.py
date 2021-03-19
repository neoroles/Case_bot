from aiogram.types import CallbackQuery

from keyboards.inline.users.keyboard_about_me import key_about_me
from loader import dp, bot


@dp.callback_query_handler(text='about_me')
async def about_me(call: CallbackQuery):
    await call.answer()
    text = '''Тут будет много и много информации о боте'''
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=key_about_me())
