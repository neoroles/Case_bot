from aiogram.types import CallbackQuery

from keyboards.inline.users.keyboard_profile import key_profile
from loader import dp, bot, db


@dp.callback_query_handler(text='profile')
async def profile(call: CallbackQuery):
    await call.answer()
    data = await db.select_user_profile(call.message.chat.id)
    if len(data[2]) > 1:
        name = f'<a href="https://t.me/{data[2]}">{data[1]}</a>'
    else:
        name = data[1]
    text = f'''💼 <b>Профиль</b>
   
👤 Имя: {name} 
<b>ID:</b>  <code>{data[0]}</code>

💰 Баланс: {round(data[5]//100/100, 2)} ₽
🔑 Ключей: {data[6]}
👥 Друзей: {data[3]}
📆 Регистрация: {data[4]}

<b>Статистика по кейсам:</b>
🗃 Всего: {data[14]}
🔥 Новичок: {data[8]}
🌟 Везунчик: {data[9]}
🥇 Топовый: {data[10]}
🃏 Фартовый: {data[11]}
🏆 Лакшери: {data[12]}
💎 Олигарх: {data[13]}
🔐 Секрет: {data[7]}

<b>Игры:</b>

🎮 Игр всего: {data[15]}
Выиграл всего: {data[16]} ₽

🎱 Игр всего: {data[18]}
Выиграл всего: {data[17]} ₽

Побед в розыгрышах: {data[20]}
Всего ежедневных бонусов: {data[19]}
Максимальный выигрыш за сутки: {data[21]} ₽ {data[22]}'''
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                disable_web_page_preview=True,
                                reply_markup=key_profile())