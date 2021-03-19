from aiogram.types import CallbackQuery

from keyboards.inline.users.game.main import key_game
from loader import dp, bot


@dp.callback_query_handler(text='games')
async def games(call: CallbackQuery):
    await call.answer()
    text = '''🕹 <b>Игры</b>

Испытай свою удачу и выиграй столько 💰, сколько тебе удастся. 
🔸В этих играх твой выигрыш основан на твоих умениях предсказывать!'''
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=key_game)


@dp.callback_query_handler(text='back_game')
async def back_game(call: CallbackQuery):
    await call.answer()
    text = '''🕹 <b>Игры</b>

Испытай свою удачу и выиграй столько 💰, сколько тебе удастся. 
🔸В этих играх твой выигрыш основан на твоих умениях предсказывать!'''
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=key_game)