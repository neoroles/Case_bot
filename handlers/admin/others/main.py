from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from data import config
from keyboards.inline.admins.other.misc import mod_set
from keyboards.inline.users.profile.misc import key, key_del
from loader import dp, bot, db
from states.admin_state import UpKeyBal


@dp.callback_query_handler(text='other_setting', user_id=config.moderators)
async def other_setting(call: CallbackQuery):
    await call.answer()
    text = '''Общие настройки:
    
🗃 <b>Настройка кейсов:</b> меняешь каждый кейс по выбору

⚫ <b>Лотерея:</b> распределение ставок и запуск

🎰 <b>Розыгрыш:</b> запуск розыгрыша на канале

✅ <b>Блок:</b> блокировка игровой части бота

💰 <b>Пополнить баланс 🔑:</b> смена баланса и ключей
Меняется вместе с балансом бота'''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=mod_set(call.message.chat.id))


@dp.callback_query_handler(text='up_balance', user_id=config.moderators)
async def up_key_balance(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await UpKeyBal.Input.set()
    text = 'Не ошибись:\n\n<code>Параметр - юзер_ид - количество</code>\n\nПример:\n<code>key - 111111 - 10</code>\n' \
           '<code>bal - 111111 - 100</code>'
    await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key)


# ЗАВИСИМОСТЬ НА БАЛАНСЫ ЕЩЕ НЕ ПРОПИСАНА
@dp.message_handler(state=UpKeyBal.Input)
async def input_parameters(message: Message, state: FSMContext):
    if message.text == 'Отмена':
        await message.answer('Действие отменено', reply_markup=key_del)
        text = '''Общие настройки:

        🗃 <b>Настройка кейсов:</b> меняешь каждый кейс по выбору

        ⚫ <b>Лотерея:</b> распределение ставок и запуск

        🎰 <b>Розыгрыш:</b> запуск розыгрыша на канале

        ✅ <b>Блок:</b> блокировка игровой части бота

        💰 <b>Пополнить баланс 🔑:</b> смена баланса и ключей
        Меняется вместе с балансом бота'''
        await message.answer(text=text, disable_notification=True, reply_markup=mod_set(message.chat.id))
        await state.finish()
    else:
        try:
            answer = message.text
            data = answer.split(' - ', 2)
            parameter = data[0]
            user = data[1]
            quantity = data[2]
            if parameter == 'key' or parameter == 'Key':
                try:
                    await db.up_key(user_id=user, key=int(quantity))
                    await message.answer('успешно - ключи', reply_markup=key_del)
                    await message.answer(text='Общие настройки', disable_notification=True,
                                         reply_markup=mod_set(message.chat.id))
                    await state.finish()
                except Exception as e:
                    await message.answer(f'Ошибка {e}')
            elif parameter == 'bal' or parameter == 'Bal':
                try:
                    await db.up_balance(user_id=user, balance=int(quantity)*10000)
                    await message.answer('успешно - баланс', reply_markup=key_del)
                    await message.answer(text='Общие настройки', disable_notification=True,
                                         reply_markup=mod_set(message.chat.id))
                    from utils.update_balance import change_balance
                    await change_balance(balance_all=int(quantity)*10000, balance_bot=0)
                    await state.finish()
                except Exception as e:
                    await message.answer(f'Ошибка {e}')
            else:
                await message.answer('ошибка ввода')
        except Exception as e:
            await message.answer(f'ошибка {e}')
