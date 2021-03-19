from asyncio import sleep

from aiogram.types import CallbackQuery

from data import variable
from keyboards.inline.users.case.keyboard_secret_case import key_case_secret_game, key_case_secret_win
from keyboards.inline.users.case.main import key_case_animation
from loader import dp, bot, db
from utils.case_data_create import case_data_secret


@dp.callback_query_handler(text='secret')
async def secret(call: CallbackQuery):
    if variable.block_case == 1:
        await call.answer('Кейсы заблокирована на несколько минут', cache_time=20)
    else:
        await call.answer()
        data = await db.select_key_user(call.message.chat.id)
        await bot.delete_message(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id)
        caption = f'''<b>Секретный кейс</b>
Тут вы можете выиграть билеты(🎟) на бесплатное открытие любого другого кейса

Открытие стоит 1 ключ - ваш баланс ключей отображается на кнопке'''
        await bot.send_photo(chat_id=call.message.chat.id,
                             photo=variable.case_secret_photo,
                             caption=caption,
                             reply_markup=key_case_secret_game(int(data)))


@dp.callback_query_handler(text='case_secret_key')
async def case_secret(call: CallbackQuery):
    if variable.block_case == 1:
        await call.answer('Кейсы заблокированы на несколько минут', cache_time=20)
    else:
        var = await db.select_key_user(call.message.chat.id)
        if int(var) < 1:
            await call.answer('Недостаточно ключей', show_alert=True, cache_time=10)
        else:
            from data import config
            data = await case_data_secret(call.message.chat.id)
            notification = f'''Кейс СЕКРЕТ
id: #user{call.message.chat.id}
name: {call.message.chat.full_name}
win: {data[4]} за 🔑'''
            await bot.send_message(chat_id=config.logs_users_channel, text=notification)
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                message_id=call.message.message_id,
                                                reply_markup=key_case_animation(data[0], data[1], data[2]))
            await sleep(0.7)
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                message_id=call.message.message_id,
                                                reply_markup=key_case_animation(data[1], data[2], data[3]))
            await sleep(0.7)
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                message_id=call.message.message_id,
                                                reply_markup=key_case_animation(data[2], data[3], data[4]))
            await sleep(0.7)
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                message_id=call.message.message_id,
                                                reply_markup=key_case_animation(data[3], data[4], data[5]))
            await sleep(0.9)
            caption = f'''<b>Секретный кейс</b>
Тут вы можете выиграть билеты(🎟) на бесплатное открытие любого другого кейса

Вы выиграли: {data[4]}'''
            await bot.edit_message_caption(chat_id=call.message.chat.id,
                                           message_id=call.message.message_id,
                                           caption=caption,
                                           reply_markup=key_case_secret_win(data[4], int(var)-1))

