from aiogram.types import CallbackQuery

from data import variable
from keyboards.inline.users.game.nvuti.keyboard_nvuti_main import key_nv
from loader import dp, db, bot


@dp.callback_query_handler(text='nvuti')
async def nvuti(call: CallbackQuery):
    await call.answer()
    data = await db.select_nvuti(call.message.chat.id)
    win = round((data[3] * data[1] // 10000 - data[3]) / 10000, 2)
    text = f'''🎮  <b>Угадай число</b>

Это игра на вероятностях. Жми "Больше" или "Меньше", чтобы забрать все 💰, которые здесь есть!

💰 <b>Баланс:</b> {round(data[0]/10000, 2)} ₽

💵 <b>Ставка:</b> {round(data[3]/10000, 2)} ₽
📈 <b>Вероятность победы:</b> {data[2]}%
⚖ <b>Возможный выигрыш:</b> {win} ₽
'''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=key_nv)
