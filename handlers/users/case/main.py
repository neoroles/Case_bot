from aiogram.types import CallbackQuery

from data import variable
from keyboards.inline.users.case.main import key_cases
from loader import dp, bot


@dp.callback_query_handler(text='cases')
async def cases(call: CallbackQuery):
    if variable.block_case == 1:
        await call.answer('Кейсы заблокирована на несколько минут', cache_time=20)
    else:
        await call.answer()
        # Запрос к бд - забираем инфу по кейсам
        text = f'''🗃 <b>Кейсы</b>🎁

Любишь кейсы? А крутые призы, которые есть в них?
Выбери один из кейсов, который тебе по душе. Вытаскивай всё, что в нём есть!

🔥 <b>Новичок</b>
🎁<b>Приз:</b> {variable.case_1_name}
🌟 <b>Везунчик</b>
🎁<b>Приз:</b> {variable.case_2_name}
🥇 <b>Топовый</b>
🎁<b>Приз:</b> {variable.case_3_name}
🃏 <b>Фартовый</b>
🎁<b>Приз:</b> {variable.case_4_name}
🏆 <b>Лакшери</b>
🎁<b>Приз:</b> {variable.case_5_name}
💎 <b>Олигарх</b>
🎁<b>Приз:</b> {variable.case_6_name}
'''
        await bot.edit_message_text(text=text,
                                    chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=key_cases)


@dp.callback_query_handler(text='cases_back')
async def cases_back(call: CallbackQuery):
    # Запрос на блокировку кейсов
    await call.answer()
    # Запрос к бд не нужен - забираем инфу по кейсам
    await bot.delete_message(chat_id=call.message.chat.id,
                             message_id=call.message.message_id)
    text = f'''🗃 <b>Кейсы</b>🎁

Любишь кейсы? А крутые призы, которые есть в них?
Выбери один из кейсов, который тебе по душе. Вытаскивай всё, что в нём есть!

🔥 <b>Новичок</b>
🎁<b>Приз:</b> {variable.case_1_name}
🌟 <b>Везунчик</b>
🎁<b>Приз:</b> {variable.case_2_name}
🥇 <b>Топовый</b>
🎁<b>Приз:</b> {variable.case_3_name}
🃏 <b>Фартовый</b>
🎁<b>Приз:</b> {variable.case_4_name}
🏆 <b>Лакшери</b>
🎁<b>Приз:</b> {variable.case_5_name}
💎 <b>Олигарх</b>
🎁<b>Приз:</b> {variable.case_6_name}
'''
    await bot.send_message(text=text,
                           chat_id=call.message.chat.id,
                           reply_markup=key_cases)


@dp.callback_query_handler(text='case_animation')
async def case_animation(call: CallbackQuery):
    await call.answer(cache_time=60)








