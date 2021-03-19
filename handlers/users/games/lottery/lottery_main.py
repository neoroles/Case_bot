from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from data import variable
from keyboards.inline.users.game.lottery.keyboard_lottery_main import key_lottery, key_lottery_back, \
    key_lottery_bet_back
from keyboards.inline.users.start_key import key_start
from loader import dp, db, bot
from states.user_state import Lottery
from utils.update_balance import change_balance


@dp.callback_query_handler(text='lottery')
async def lottery(call: CallbackQuery):
    if variable.block_lottery == 1:
        await call.answer('Лотерея времено заблокирована')
    else:
        data = await db.select_lottery_user(user_id=call.message.chat.id)
        if data[1] == 0:
            await call.answer()
            text = '''🎱  <b>Лотерея</b>

Твоя задача — загадать цвет. Так что, давай проверим, черный или красный тебе больше всего подобает?

❗ <i>Сделать ставку можно всего один раз в день. Чтобы использовать её пару раз, ты должен привести 25 рефералов.</i>'''
            await bot.edit_message_text(text=text,
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        disable_web_page_preview=True,
                                        reply_markup=key_lottery)
        else:
            await call.answer()
            if data[1] == 1:
                text = f'''<b>🎱 Лотерея > Режим игры</b>

Ставки деланы, ставок больше нет.

👁‍🗨 <b>Ваша ставка:</b> Черное
💸 <b>Сумма ставки:</b> {data[0]}'''
            else:
                text = f'''<b>🎱 Лотерея > Режим игры</b>

Ставки деланы, ставок больше нет.

👁‍🗨 <b>Ваша ставка:</b> Красное
💸 <b>Сумма ставки:</b> {data[0]}'''
            await bot.edit_message_text(text=text,
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        disable_web_page_preview=True,
                                        reply_markup=key_lottery_back)


@dp.callback_query_handler(text='lottery', state=Lottery.Input)
async def lottery_back(call: CallbackQuery, state: FSMContext):
    await state.finish()
    # data = await db.select_lottery_user(user_id=call.message.chat.id)
    # if data[1] == 0:
    await call.answer()
    text = '''🎱  <b>Лотерея</b>

Твоя задача — загадать цвет. Так что, давай проверим, черный или красный тебе больше всего подобает?'''
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                disable_web_page_preview=True,
                                reply_markup=key_lottery)
    # else:
    #     if data[1] == 1:
    #         answer = 'Черное'
    #     else:
    #         answer = 'Красное'
    #     text = f'Ставки сделаны, ставок больше нет\nВаша ставка: {answer}\nСумма ставки: {data[0]}'
    #     await bot.edit_message_text(text=text,
    #                                 chat_id=call.message.chat.id,
    #                                 message_id=call.message.message_id,
    #                                 disable_web_page_preview=True,
    #                                 reply_markup=key_lottery_back)


@dp.callback_query_handler(text_contains='lottery_bet')
async def lottery_bet(call: CallbackQuery, state: FSMContext):
    if variable.block_lottery == 1:
        await call.answer('Лотерея времено заблокирована')
    else:
        data = await db.select_lottery_and_balance_user(user_id=call.message.chat.id)
        if data[2] == 1 or data[2] == 2:
            await call.answer()
            if data[2] == 1:
                text = f'''<b>🎱 Лотерея > Режим игры</b>

Ставки деланы, ставок больше нет.

👁‍🗨 <b>Ваша ставка:</b> Черное
💸 <b>Сумма ставки:</b> {data[1]}'''
            else:
                text = f'''<b>🎱 Лотерея > Режим игры</b>

Ставки деланы, ставок больше нет.

👁‍🗨 <b>Ваша ставка:</b> Красное
💸 <b>Сумма ставки:</b> {data[1]}'''
            await bot.edit_message_text(text=text,
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        disable_web_page_preview=True,
                                        reply_markup=key_lottery_back)
        elif data[0] // 10000 < 1:
            await call.answer('На вашем балансе не достаточно денег', show_alert=True, cache_time=10)
        else:
            await call.answer()
            answer = int(call.data[-1])
            await Lottery.Input.set()
            await state.update_data(mes_id=call.message.message_id)
            await state.update_data(answer=answer)
            await state.update_data(balance=data[0]//10000)
            if answer == 1:
                text = f'''⚫️ <b>Вы выбрали:</b> Черное

Пришлите сумму ставки от «1» до {data[0]//10000} или нажмите отмена.
❗️<i>Необходимо ввести целое число</i>'''
            else:
                text = f'''⚫️ <b>Вы выбрали:</b> Красное

Пришлите сумму ставки от «1» до {data[0]//10000} или нажмите отмена.
❗️<i>Необходимо ввести целое число</i>'''
            await bot.edit_message_text(text=text,
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=key_lottery_bet_back)


@dp.message_handler(state=Lottery.Input)
async def input_lottery(message: Message, state: FSMContext):
    response = message.text
    data = await state.get_data()
    mes_id = data.get("mes_id")
    answer = data.get("answer")
    balance = data.get("balance")
    if response.isdigit():
        if 1 <= int(response) <= balance:
            from data import config
            await db.update_lottery_user(user_id=message.chat.id, bal=int(response)*10000,
                                         x=int(response), y=answer)
            await change_balance(balance_all=-int(response)*10000//1, balance_bot=-int(response)*10000//1)
            await state.finish()
            if answer == 1:
                par = 'Черное'
                text = f'''<b>🎱 Лотерея > Режим игры</b>

Ставки деланы, ставок больше нет.

👁‍🗨 <b>Ваша ставка:</b> Черное
💸 <b>Сумма ставки:</b> {response}'''
            else:
                par = 'Красное'
                text = f'''<b>🎱 Лотерея > Режим игры</b>

Ставки деланы, ставок больше нет.

👁‍🗨 <b>Ваша ставка:</b> Красное
💸 <b>Сумма ставки:</b> {response}'''
            notification = f'''ЛОТЕРЕЯ
id: #user{message.chat.id}
name: {message.chat.full_name}
win: {par} {response} ₽'''
            await bot.send_message(chat_id=config.logs_users_channel, text=notification)
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            await bot.edit_message_text(text=text,
                                        chat_id=message.chat.id,
                                        message_id=mes_id,
                                        disable_web_page_preview=True,
                                        reply_markup=key_lottery_back)
        elif int(response) < 1:
            if answer == 1:
                text = f'''⚫️ <b>Вы выбрали:</b> Черное

<b>Ваш баланс</b>: {balance}

⚠️<i>Необходимо ввести число</i> <b>не меньше единицы</b>'''
            else:
                text = f'''⚫️ <b>Вы выбрали:</b> Красное

<b>Ваш баланс</b>: {balance}

⚠️<i>Необходимо ввести число</i> <b>не меньше единицы</b>'''
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            await bot.edit_message_text(text=text,
                                        chat_id=message.chat.id,
                                        message_id=mes_id,
                                        reply_markup=key_lottery_bet_back)
        else:
            if answer == 1:
                text = f'''⚫️ <b>Вы выбрали:</b> Черное

<b>Ваш баланс</b>: {balance}

⚠️<i>Необходимо ввести число</i> <b>не больше своего баланса</b>'''
            else:
                text = f'''⚫️ <b>Вы выбрали:</b> Красное

<b>Ваш баланс</b>: {balance}

⚠️<i>Необходимо ввести число</i> <b>не больше своего баланса</b>'''
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            await bot.edit_message_text(text=text,
                                        chat_id=message.chat.id,
                                        message_id=mes_id,
                                        reply_markup=key_lottery_bet_back)
    elif response == '/start':
        await state.finish()
        await bot.delete_message(message.chat.id, mes_id)
        text = '''💈 <b>Главное меню</b>

Здесь вы можете сыграть в игры и выиграть 💰 или приз.   
<i>Призы можно посмотреть в кейсах.</i>'''
        await message.answer(text, reply_markup=key_start)
    else:
        if answer == 1:
            text = f'''⚫️ <b>Вы выбрали:</b> Черное

⚠️<i>Необходимо ввести целое</i> <b>число</b>'''
        else:
            text = f'''⚫️ <b>Вы выбрали:</b> Красное

⚠️<i>Необходимо ввести целое</i> <b>число</b>'''
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await bot.edit_message_text(text=text,
                                    chat_id=message.chat.id,
                                    message_id=mes_id,
                                    reply_markup=key_lottery_bet_back)



