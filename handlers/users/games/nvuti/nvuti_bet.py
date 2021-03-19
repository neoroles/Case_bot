from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from data import variable
from keyboards.inline.users.game.nvuti.keyboard_nvuti_bet import key_bet, key_bet_input_back
from keyboards.inline.users.start_key import key_start
from loader import dp, db, bot
from states.user_state import Bet
from utils.check_float import float_check


@dp.callback_query_handler(text='nv_change_bet')
async def nv_change_bet(call: CallbackQuery):
    if variable.block_nvuti == 1:
        await call.answer('nvuti Временно заблокирована')
    else:
        data = await db.select_nvuti_change_bet(call.message.chat.id)
        if data[0] < 100000:
            await call.answer('На вашем балансе не достаточно средств')
        else:
            await call.answer()
            balance = round(data[0]/10000, 2)
            text = f'''🎮  <b>Угадай число > Изменить ставку</b>

💰 <b>Ваш баланс:</b> {balance} ₽
💵 <b>Ваша ставка:</b> {round(data[1]/10000, 2)} ₽

➖ <b>Минимально возможная ставка:</b>  10 ₽
➕ <b>Максимально возможная ставка:</b> {balance}'''
            await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=key_bet)


@dp.callback_query_handler(text='nv_change_bet', state=Bet.Input)
async def nvuti_bet_back(call: CallbackQuery, state: FSMContext):
    await call.answer()
    data = await db.select_nvuti_change_bet(call.message.chat.id)
    await state.finish()
    balance = round(data[0] / 10000, 2)
    text = f'''🎮  <b>Угадай число > Изменить ставку</b>

💰 <b>Ваш баланс:</b> {balance} ₽
💵 <b>Ваша ставка:</b> {round(data[1] / 10000, 2)} ₽

➖ <b>Минимально возможная ставка:</b>  10 ₽
➕ <b>Максимально возможная ставка:</b> {balance}'''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=key_bet)


@dp.callback_query_handler(text='nv_bet_max')
async def nv_bet_max(call: CallbackQuery):
    if variable.block_nvuti == 1:
        await call.answer('nvuti Временно заблокирована')
    else:
        data = await db.select_nvuti_change_bet(call.message.chat.id)
        if data[0] < 100000:
            await call.answer('На вашем балансе не достаточно средств')
        else:
            await db.update_nv_max_bet(call.message.chat.id)
            await call.answer('Ставка изменена')
            balance = round(data[0] / 10000, 2)
            text = f'''🎮  <b>Угадай число > Изменить ставку</b>

💰 <b>Ваш баланс:</b> {balance} ₽
💵 <b>Ваша ставка:</b> {balance} ₽

➖ <b>Минимально возможная ставка:</b>  10 ₽
➕ <b>Максимально возможная ставка:</b> {balance}'''
            await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=key_bet)


@dp.callback_query_handler(text='nv_bet_min')
async def nv_bet_min(call: CallbackQuery):
    if variable.block_nvuti == 1:
        await call.answer('nvuti Временно заблокирована')
    else:
        data = await db.select_nvuti_change_bet(call.message.chat.id)
        if data[0] < 100000:
            await call.answer('На вашем балансе не достаточно средств')
        else:
            await db.update_nv_min_bet(call.message.chat.id)
            await call.answer('Ставка изменена')
            balance = round(data[0] / 10000, 2)
            text = f'''🎮  <b>Угадай число > Изменить ставку</b>

💰 <b>Ваш баланс:</b> {balance} ₽
💵 <b>Ваша ставка:</b> 10 ₽

➖ <b>Минимально возможная ставка:</b>  10 ₽
➕ <b>Максимально возможная ставка:</b> {balance}'''
            await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=key_bet)


@dp.callback_query_handler(text='nv_bet_2')
async def nv_bet_2(call: CallbackQuery):
    if variable.block_nvuti == 1:
        await call.answer('nvuti Времени заблокирована')
    else:
        data = await db.select_nvuti_change_bet(call.message.chat.id)
        if data[0] < 100000:
            await call.answer('На вашем балансе не достаточно средств')
        else:
            if data[1] * 2 > data[0]:
                await call.answer('На вашем балансе не достаточно средств')
            else:
                await db.update_nv_2x_bet(call.message.chat.id)
                await call.answer('Ставка изменена')
                balance = round(data[0] / 10000, 2)
                text = f'''🎮  <b>Угадай число > Изменить ставку</b>

💰 <b>Ваш баланс:</b> {balance} ₽
💵 <b>Ваша ставка:</b> {round(data[1] / 5000, 2)} ₽

➖ <b>Минимально возможная ставка:</b>  10 ₽
➕ <b>Максимально возможная ставка:</b> {balance}'''
                await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                            message_id=call.message.message_id,
                                            reply_markup=key_bet)


@dp.callback_query_handler(text='nv_bet_05')
async def nv_bet_05(call: CallbackQuery):
    if variable.block_nvuti == 1:
        await call.answer('nvuti Времени заблокирована')
    else:
        data = await db.select_nvuti_change_bet(call.message.chat.id)
        if data[0] < 100000:
            await call.answer('На вашем балансе не достаточно средств')
        else:
            if data[1]//2 < 100000:
                await call.answer('Нельзя понизить ставку ниже 10 бакинских')
            else:
                await db.update_nv_05x_bet(call.message.chat.id)
                await call.answer('Ставка изменена')
                balance = round(data[0] / 10000, 2)
                text = f'''🎮  <b>Угадай число > Изменить ставку</b>

💰 <b>Ваш баланс:</b> {balance} ₽
💵 <b>Ваша ставка:</b> {round(data[1] / 20000, 2)} ₽

➖ <b>Минимально возможная ставка:</b>  10 ₽
➕ <b>Максимально возможная ставка:</b> {balance}'''
                await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                            message_id=call.message.message_id,
                                            reply_markup=key_bet)


@dp.callback_query_handler(text='nv_bet_input')
async def nv_bet_input(call: CallbackQuery, state: FSMContext):
    if variable.block_nvuti == 1:
        await call.answer('nvuti Времени заблокирована')
    else:
        data = await db.select_nvuti_change_bet(call.message.chat.id)
        if data[0] < 100000:
            await call.answer('На вашем балансе не достаточно средств')
        else:
            await call.answer()
            await Bet.Input.set()
            await state.update_data(balance=data[0])
            await state.update_data(mes_id=call.message.message_id)
            text = f'''🎮  <b>Угадай число > Изменить ставку</b>
            
⚠ Введите сумму ставки от 10 до {round(data[0] / 10000, 2)}'''
            await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=key_bet_input_back)


@dp.message_handler(state=Bet.Input)
async def bet_input(message: Message, state: FSMContext):
    response = message.text
    data = await state.get_data()
    mes_id = data.get("mes_id")
    balance = data.get("balance")
    if float_check(response):
        bet = int(float(response) * 10000)
        if bet > balance:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            text = '''🎮  <b>Угадай число > Изменить ставку</b>
            
⚠ Недостаточно средств'''
            await bot.edit_message_text(text=text,
                                        chat_id=message.chat.id,
                                        message_id=mes_id,
                                        reply_markup=key_bet_input_back)
        elif bet < 100000:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            text = '''🎮  <b>Угадай число > Изменить ставку</b>
            
⚠️Нельзя опустить ставку ниже 10 ₽'''
            await bot.edit_message_text(text=text,
                                        chat_id=message.chat.id,
                                        message_id=mes_id,
                                        reply_markup=key_bet_input_back)
        else:
            await db.update_nv_input_bet(user_id=message.chat.id, x=bet)
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            await state.finish()
            balance = round(balance / 10000, 2)
            text = f'''🎮  <b>Угадай число > Изменить ставку</b>

💰 <b>Ваш баланс:</b> {balance} ₽
💵 <b>Ваша ставка:</b> {round(bet / 10000, 2)} ₽

➖ <b>Минимально возможная ставка:</b>  10 ₽
➕ <b>Максимально возможная ставка:</b> {balance}'''
            await bot.edit_message_text(text=text,
                                        chat_id=message.chat.id,
                                        message_id=mes_id,
                                        reply_markup=key_bet)
    elif response == '/start':
        await state.finish()
        await bot.delete_message(message.chat.id, mes_id)
        text = '''💈 <b>Главное меню</b>

Здесь вы можете сыграть в игры и выиграть 💰 или приз.   
<i>Призы можно посмотреть в кейсах.</i>'''
        await message.answer(text, reply_markup=key_start)

    else:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        text = '''🎮  <b>Угадай число > Изменить ставку</b>
            
⚠ Вам необходимо ввести число'''
        await bot.edit_message_text(text=text,
                                    chat_id=message.chat.id,
                                    message_id=mes_id,
                                    reply_markup=key_bet_input_back)



