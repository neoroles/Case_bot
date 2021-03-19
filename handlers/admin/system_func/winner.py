from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from data import config, variable
from keyboards.inline.admins.systems.main import key_systems
from keyboards.inline.users.profile.misc import key, key_del
from loader import dp, bot, db
from states.admin_state import Winner


@dp.callback_query_handler(text='winner', user_id=config.admins)
async def winner(call: CallbackQuery):
    await call.answer()
    text = '''Одновременно можно выбрать только одного победителя
Введите все по условию
<code>case_</code>1:user_id

Пример:
<code>case_1</code>:123344566
<code>case_2</code>:76543456
...
<code>nv_win</code>:54654677'''
    await Winner.Input.set()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key)


@dp.message_handler(user_id=config.admins, state=Winner.Input)
async def winner_choice(message: Message, state: FSMContext):
    if message.text == 'Отмена':
        await message.answer('Действие отменено', reply_markup=key_del)
        text = 'Тут системные настройки'
        await state.finish()
        await message.answer(text=text, reply_markup=key_systems)
    else:
        try:
            answer = message.text
            data = answer.split(':', 1)
            case = data[0]
            user_id = data[1]
            if await db.select_user(user_id=user_id):
                await message.answer('Пользователь не найден в бд')
            elif case[0:5] == 'case_':
                if 1 <= int(case[-1]) <= 7:
                    case_id = int(case[-1])
                    if case_id == 1:
                        variable.case_1_winners = user_id
                    elif case_id == 2:
                        variable.case_2_winners = user_id
                    elif case_id == 3:
                        variable.case_3_winners = user_id
                    elif case_id == 4:
                        variable.case_4_winners = user_id
                    elif case_id == 5:
                        variable.case_5_winners = user_id
                    elif case_id == 6:
                        variable.case_6_winners = user_id
                    elif case_id == 7:
                        variable.case_secret_winners = user_id
                    await message.answer(text=f'{user_id} победит в кейсе {case_id}', reply_markup=key_del)
                    text = 'Тут системные настройки'
                    await message.answer(text=text, reply_markup=key_systems)
                    await state.finish()
                else:
                    await message.answer('Неверный номер кейса')
            elif case[0:6] == 'nv_win':
                variable.nvuti_winner = user_id
                await message.answer(text=f'{user_id} победит в нвути', reply_markup=key_del)
                text = 'Тут системные настройки'
                await message.answer(text=text, reply_markup=key_systems)
                await state.finish()
            else:
                await message.answer(text=f'ошибка', reply_markup=key_del)
                text = 'Тут системные настройки'
                await message.answer(text=text, reply_markup=key_systems)
                await state.finish()
        except Exception as e:
            await message.answer(f'Ошибка {e}, повтори попытку')






