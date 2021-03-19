from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from data import variable
from data.config import admins
from keyboards.inline.admins.systems.key_percent_win import key_back_system
from loader import dp, bot, db
from states.admin_state import WinPercent


@dp.callback_query_handler(text='win_percent', user_id=admins)
async def win_percent(call: CallbackQuery, state: FSMContext):
    await call.answer()
    text = f'''Процент проигрышей: {variable.win_percent}\n\nЧисло означающее какой процент от суммы пополнений будет 
проигран пользователями\n\n<b>Пример</b>\nСумма пополнений: 10000\nБаланс бота: 1000\nПроцент: 15

Получается пока баланс бота не поднимется до 1500 пользователи будут в основном проигрывать или выигрывать, но минимум.
<b>Важно понимать, что число на балансе бота напрямую влияет на вероятность выигрыша супер приза в кейсах</b>\n\n\n
Введите число от 5 до 80'''
    await WinPercent.Input.set()
    await state.update_data(mes_id=call.message.message_id)
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                message_id=call.message.message_id, reply_markup=key_back_system)


@dp.message_handler(user_id=admins, state=WinPercent.Input)
async def change_win_percent(message: Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()
    mes_id = data.get('mes_id')
    if answer.isdigit():
        if 5 < int(answer) < 80:
            await db.update_win_percent(x=int(answer))
            variable.win_percent = int(answer)
            text = f'Процент проигрышей: {variable.win_percent}\n\nЧисло означающее какой процент от суммы пополнений' \
                   ' будет проигран пользователями\n\n' \
                   '<b>Пример</b>\nСумма пополнений: 10000\nБаланс бота: 1000\nПроцент: 15\n\n' \
                   'Получается пока баланс бота' \
                   'не поднимется до 1500 пользователи будут в основном проигрывать или выигрывать но минимум\n' \
                   '<b>Важно понимать что число на балансе бота напрямую влияет на вероятность выигрыша супер приза ' \
                   'в кейсах</b>\n\n\nВведите число от 5 до 80'
            await state.finish()
            await bot.edit_message_text(text=text, chat_id=message.chat.id,
                                        message_id=mes_id, reply_markup=key_back_system)
        else:
            await bot.edit_message_text(text='Введите число от 5 до 80', chat_id=message.chat.id,
                                        message_id=mes_id, reply_markup=key_back_system)
    else:
        await bot.edit_message_text(text='Введите число', chat_id=message.chat.id,
                                    message_id=mes_id, reply_markup=key_back_system)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
