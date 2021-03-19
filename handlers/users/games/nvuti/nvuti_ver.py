from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from data import variable
from keyboards.inline.users.game.nvuti.keyboard_nvuti_ver import key_ver, key_ver_input_back
from keyboards.inline.users.start_key import key_start
from loader import dp, db, bot
from states.user_state import Ver


@dp.callback_query_handler(text='nv_change_ver')
async def nv_change_ver(call: CallbackQuery):
    if variable.block_nvuti == 1:
        await call.answer('nvuti Временно заблокирована')
    else:
        await call.answer()
        data = await db.select_nv_change_ver(call.message.chat.id)
        co_ef = round(data[0]/10000, 4)
        win = round(data[2]*data[0]//1000000 / 100, 2)
        bet = round(data[2]/10000, 2)
        text = f'''🎮  <b>Угадай число > Изменить вероятность</b>

💵 <b>Ваша ставка:</b> {bet} ₽

✖️<b>Множитель:</b> {co_ef}
📈 <b>Ваша вероятность</b> {data[1]}
⚖️<b>Возможный выигрыш:</b> {win} ₽
'''
        await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=key_ver)


@dp.callback_query_handler(text='nv_change_ver', state=Ver.Input)
async def nvuti_ver_back(call: CallbackQuery, state: FSMContext):
    await call.answer()
    data = await db.select_nv_change_ver(call.message.chat.id)
    co_ef = round(data[0] / 10000, 4)
    win = round(data[2] * data[0] // 1000000 / 100, 2)
    await state.finish()
    bet = round(data[2] / 10000, 2)
    text = f'''🎮  <b>Угадай число > Изменить вероятность</b>

💵 <b>Ваша ставка:</b> {bet} ₽

✖️<b>Множитель:</b> {co_ef}
📈 <b>Ваша вероятность</b> {data[1]}
⚖️<b>Возможный выигрыш:</b> {win} ₽
'''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=key_ver)


@dp.callback_query_handler(text='nv_ver_max')
async def nv_ver_max(call: CallbackQuery):
    if variable.block_nvuti == 1:
        await call.answer('nvuti Временно заблокирована')
    else:
        data = await db.select_nv_change_ver(call.message.chat.id)
        if data[1] == 95:
            await call.answer('Уже максимальная', cache_time=2)
        else:
            await call.answer('Вероятность изменена', cache_time=2)
            await db.update_nv_max_ver(user_id=call.message.chat.id)
            win = round(data[2] * 10526 // 1000000 / 100, 2)
            bet = round(data[2] / 10000, 2)
            text = f'''🎮  <b>Угадай число > Изменить вероятность</b>

💵 <b>Ваша ставка:</b> {bet} ₽

✖️<b>Множитель:</b> 1.0526
📈 <b>Ваша вероятность</b> 95
⚖️<b>Возможный выигрыш:</b> {win} ₽
'''
            await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=key_ver)


@dp.callback_query_handler(text='nv_ver_min')
async def nv_ver_max(call: CallbackQuery):
    if variable.block_nvuti == 1:
        await call.answer('nvuti Временно заблокирована')
    else:
        data = await db.select_nv_change_ver(call.message.chat.id)
        if data[1] == 1:
            await call.answer('Уже минимальная', cache_time=2)
        else:
            await call.answer('Вероятность изменена', cache_time=2)
            await db.update_nv_min_ver(call.message.chat.id)
            win = round(data[2] // 10 / 10, 2)
            bet = round(data[2] / 10000, 2)
            text = f'''🎮  <b>Угадай число > Изменить вероятность</b>

💵 <b>Ваша ставка:</b> {bet} ₽

✖️<b>Множитель:</b> 100
📈 <b>Ваша вероятность</b> 1
⚖️<b>Возможный выигрыш:</b> {win} ₽
'''
            await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=key_ver)


@dp.callback_query_handler(text='nv_ver_2')
async def nv_ver_2(call: CallbackQuery):
    if variable.block_nvuti == 1:
        await call.answer('nvuti Временно заблокирована')
    else:
        data = await db.select_nv_change_ver(call.message.chat.id)
        ver = data[1] * 2
        if ver > 95:
            await call.answer('Нельзя повысить выше 95')
        else:
            await call.answer('Вероятность изменена', cache_time=2)
            co_ef = await db.select_nv_constant(ver)
            await db.update_nv_ver(user_id=call.message.chat.id, ver=ver, co_ef=co_ef)
            win = round(data[2] * co_ef // 1000000 / 100, 2)
            bet = round(data[2] / 10000, 2)
            text = f'''🎮  <b>Угадай число > Изменить вероятность</b>

💵 <b>Ваша ставка:</b> {bet} ₽

✖️<b>Множитель:</b> {round(co_ef / 10000, 4)}
📈 <b>Ваша вероятность</b> {ver}
⚖️<b>Возможный выигрыш:</b> {win} ₽
'''
            await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=key_ver)


@dp.callback_query_handler(text='nv_ver_05')
async def nv_ver_05(call: CallbackQuery):
    if variable.block_nvuti == 1:
        await call.answer('nvuti Временно заблокирована')
    else:
        data = await db.select_nv_change_ver(call.message.chat.id)
        ver = data[1] // 2
        if ver < 1:
            await call.answer('Нельзя понизить ниже 1')
        else:
            await call.answer('Вероятность изменена', cache_time=2)
            co_ef = await db.select_nv_constant(ver)
            await db.update_nv_ver(user_id=call.message.chat.id, ver=ver, co_ef=co_ef)
            win = round(data[2] * co_ef // 1000000 / 100, 2)
            bet = round(data[2] / 10000, 2)
            text = f'''🎮  <b>Угадай число > Изменить вероятность</b>

💵 <b>Ваша ставка:</b> {bet} ₽

✖️<b>Множитель:</b> {round(co_ef / 10000, 4)}
📈 <b>Ваша вероятность</b> {ver}
⚖️<b>Возможный выигрыш:</b> {win} ₽
'''
            await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=key_ver)


@dp.callback_query_handler(text='nv_ver_input')
async def nv_ver_input(call: CallbackQuery, state: FSMContext):
    if variable.block_nvuti == 1:
        await call.answer('nvuti Временно заблокирована')
    else:
        await call.answer()
        await Ver.Input.set()
        await state.update_data(mes_id=call.message.message_id)
        text = '''🎮  <b>Угадай число > Изменить вероятность</b>
        
⚠ Введите число от 1 до 95'''
        await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=key_ver_input_back)


@dp.message_handler(state=Ver.Input)
async def ver_input(message: Message, state: FSMContext):
    response = message.text
    data = await state.get_data()
    mes_id = data.get("mes_id")
    if response.isdigit():
        ver = int(response)
        if ver > 95:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            text = '''🎮  <b>Угадай число > Изменить вероятность</b>
        
⚠ Вероятность не может превышать 95%, введите другое число'''
            await bot.edit_message_text(text=text,
                                        chat_id=message.chat.id,
                                        message_id=mes_id,
                                        reply_markup=key_ver_input_back)
        elif ver < 1:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            text = '''🎮  <b>Угадай число > Изменить вероятность</b>
        
⚠ Вероятность не может быть ниже 1%, введите другое число'''
            await bot.edit_message_text(text=text,
                                        chat_id=message.chat.id,
                                        message_id=mes_id,
                                        reply_markup=key_ver_input_back)
        else:
            co_ef = await db.select_nv_constant(ver)
            data = await db.select_nv_bet(message.chat.id)
            await db.update_nv_ver(user_id=message.chat.id, ver=ver, co_ef=co_ef)
            win = round(data * co_ef // 1000000 / 100, 2)
            await state.finish()
            bet = round(data / 10000, 2)
            text = f'''🎮  <b>Угадай число > Изменить вероятность</b>

💵 <b>Ваша ставка:</b> {bet}

✖️<b>Множитель:</b> {round(co_ef / 10000, 4)}
📈 <b>Ваша вероятность</b> {ver}
⚖️<b>Возможный выигрыш:</b> {win}
'''
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            await bot.edit_message_text(text=text, chat_id=message.chat.id,
                                        message_id=mes_id,
                                        reply_markup=key_ver)

    elif response == '/start':
        await state.finish()
        await bot.delete_message(message.chat.id, mes_id)
        text = '''💈 <b>Главное меню</b>

Здесь вы можете сыграть в игры и выиграть 💰 или приз.   
<i>Призы можно посмотреть в кейсах.</i>'''
        await message.answer(text, reply_markup=key_start)
    else:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        text = '''🎮  <b>Угадай число > Изменить вероятность</b>
        
⚠ Вам необходимо ввести число'''
        await bot.edit_message_text(text=text,
                                    chat_id=message.chat.id,
                                    message_id=mes_id,
                                    reply_markup=key_ver_input_back)

