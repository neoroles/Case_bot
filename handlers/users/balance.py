from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboards.inline.users.keyboard_balance import key_cash, key_back_up
from loader import dp, bot, db
from states.user_state import Balance


@dp.callback_query_handler(text='cash')
async def cash(call: CallbackQuery):
    await call.answer()
    data = await db.select_balance_user(call.message.chat.id)
    text = f'''💵 <b>Баланс</b> 

💰<b>Ваш баланс:</b> {round(data[0]/10000, 2)} ₽

🔐 <b>Ключи:</b> {data[1]} 🔑

🎟<b>Билеты:</b>
🔥 Новичок - {data[2]} 🎟
🌟 Везунчик - {data[3]} 🎟
🥇 Топовый - {data[4]} 🎟
🃏 Фартовый - {data[5]} 🎟
🏆 Лакшери - {data[6]} 🎟
💎 Олигарх - {data[7]} 🎟'''
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=key_cash(0))


@dp.callback_query_handler(text='cash', state=Balance.Up)
async def cash(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.finish()
    data = await db.select_balance_user(call.message.chat.id)
    text = f'''💵 <b>Баланс</b> 

💰<b>Ваш баланс:</b> {round(data[0]/10000, 2)} ₽

🔐 <b>Ключи:</b> {data[1]} 🔑

🎟<b>Билеты:</b>
🔥 Новичок - {data[2]} 🎟
🌟 Везунчик - {data[3]} 🎟
🥇 Топовый - {data[4]} 🎟
🃏 Фартовый - {data[5]} 🎟
🏆 Лакшери - {data[6]} 🎟
💎 Олигарх - {data[7]} 🎟'''
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=key_cash(0))


@dp.callback_query_handler(text='profile:cash')
async def cash(call: CallbackQuery):
    await call.answer()
    data = await db.select_balance_user(call.message.chat.id)
    text = f'''💵 <b>Баланс</b> 

💰<b>Ваш баланс:</b> {round(data[0]/10000, 2)} ₽

🔐 <b>Ключи:</b> {data[1]} 🔑

🎟<b>Билеты:</b>
🔥 Новичок - {data[2]} 🎟
🌟 Везунчик - {data[3]} 🎟
🥇 Топовый - {data[4]} 🎟
🃏 Фартовый - {data[5]} 🎟
🏆 Лакшери - {data[6]} 🎟
💎 Олигарх - {data[7]} 🎟'''
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=key_cash(1))


@dp.callback_query_handler(text='up_balance')
async def up_balance(call: CallbackQuery, state: FSMContext):
    await call.answer()
    text = '''<b>Введите сумму пополнения</b>

Минимальная сумма пополнения баланса: 50 рублей
Вам необходимо ввести целое число
'''
    await Balance.Up.set()
    await state.update_data(mes_id=call.message.message_id)
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=key_back_up)


@dp.message_handler(state=Balance.Up)
async def up_input(message: Message, state: FSMContext):
    response = message.text
    data = await state.get_data()
    mes_id = data.get("mes_id")
    if response.isdigit():
        if 1 <= int(response):
            await state.update_data(up_sum=int(response))
            await Balance.UpConf.set()
            text = f'''Пополнить баланс на {int(response)}'''
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            await bot.edit_message_text(text=text, chat_id=message.chat.id,
                                        message_id=mes_id, reply_markup=key_back_up)
        else:
            text = '''Сумма слишком мала'''
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            await bot.edit_message_text(text=text, chat_id=message.chat.id,
                                        message_id=mes_id, reply_markup=key_back_up)
    else:
        text = '''Вам необходимо ввести целое число'''
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await bot.edit_message_text(text=text, chat_id=message.chat.id,
                                    message_id=mes_id, reply_markup=key_back_up)



@dp.callback_query_handler(text='down_balance')
async def down_balance(call: CallbackQuery):
    await call.answer('Пока не доступно')