from aiogram.types import CallbackQuery
from asyncio import sleep
from datetime import datetime, timedelta

from keyboards.inline.users.case.keyboard_case_1 import key_case_one_game, key_case_1_win
from keyboards.inline.users.case.main import key_case_animation, key_animation
from loader import dp, bot, db
from utils.case_data_create import case_data_one_money, case_data_one_ticket
from data import variable


@dp.callback_query_handler(text='case_one')
async def case_one(call: CallbackQuery):
    if variable.block_case == 1:
        await call.answer('Кейсы заблокирована на несколько минут', cache_time=20)
    else:
        await call.answer()
        data = await db.select_ticket_case(user_id=call.message.chat.id, x=1)
        await bot.delete_message(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id)
        caption = f'''🗃 <b>Кейс на {variable.case_1_name}</b>
ℹ <b>Описание:</b> {variable.case_1_description}.

💰 <b>Стоимость:</b> {variable.case_1_cost}₽

'''
        await bot.send_photo(chat_id=call.message.chat.id,
                             photo=variable.case_1_photo,
                             caption=caption,
                             reply_markup=key_case_one_game(int(data)))


@dp.callback_query_handler(text_contains='case_one_money')
async def case_one_money(call: CallbackQuery):
    if variable.block_case == 1:
        await call.answer('Кейсы заблокирована на несколько минут', cache_time=20)
    else:
        data = call.data.split("_", 3)
        if variable.case_1_change_increment != int(data[3]):
            await call.answer('Кейсы обновились', show_alert=True)
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            data = await db.select_ticket_user(user_id=call.message.chat.id, x=1)
            caption = f'''🗃 <b>Кейс на {variable.case_1_name}</b>
ℹ <b>Описание:</b> {variable.case_1_description}.

💰 <b>Стоимость:</b> {variable.case_1_cost}₽

'''
            await bot.send_photo(chat_id=call.message.chat.id,
                                 photo=variable.case_1_photo,
                                 caption=caption,
                                 reply_markup=key_case_one_game(int(data)))
        else:
            var = await db.select_balance_and_ticked_user(user_id=call.message.chat.id, x=1)
            if var[0]//10000 < variable.case_1_bet:
                await call.answer('На вашем балансе недостаточно средств', show_alert=True, cache_time=10)
            else:
                await call.answer()
                data = await case_data_one_money(call.message.chat.id)
                delta = 0
                if datetime.now() - var[3] > timedelta(1):
                    delta = 1
                if data[4] == '🔥':
                    if delta == 1:
                        await db.update_case_win_user(user_id=call.message.chat.id,
                                                      balance=-variable.case_1_bet*10000, x=1, y=0, par='🔥')
                    else:
                        await db.update_case_balance(user_id=call.message.chat.id, balance=-variable.case_1_bet*10000,
                                                     x=1)
                else:
                    from data import config
                    win = int(data[4])-variable.case_1_bet
                    if delta == 1 or var[2] < win:
                        if win > 0:
                            await db.update_case_win_user(user_id=call.message.chat.id,
                                                          balance=win * 10000, x=1, y=win, par='🔥')
                        else:
                            await db.update_case_win_user(user_id=call.message.chat.id,
                                                          balance=win * 10000, x=1, y=0, par='🔥')
                    else:
                        await db.update_case_balance(user_id=call.message.chat.id,
                                                     balance=win * 10000, x=1)
                    notification = f'''Кейс НОВИЧОК 🔥
id: #user{call.message.chat.id}
name: {call.message.chat.full_name}
win: {win}'''
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
                await sleep(0.7)
                if data[4] != '🔥':
                    await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                        message_id=call.message.message_id,
                                                        reply_markup=key_case_1_win(data[4], int(var[1])))
                else:
                    from data import config
                    caption = f'Поздравляем!\nВы выиграли {variable.case_1_name}.\n' \
                              f'Обратитесь к администратору для получения приза'
                    await bot.edit_message_caption(chat_id=call.message.chat.id,
                                                   message_id=call.message.message_id,
                                                   caption=caption,
                                                   reply_markup=key_animation('🔥'))
                    text = f'Пользователь {call.message.chat.id} выиграл {variable.case_1_name}'
                    await bot.send_message(chat_id=config.chat, text=text)
                    caption = f'''🗃 <b>Кейс на {variable.case_1_name}</b>
ℹ <b>Описание:</b> {variable.case_1_description}.

💰 <b>Стоимость:</b> {variable.case_1_cost}₽

'''
                    await bot.send_photo(chat_id=call.message.chat.id,
                                         photo=variable.case_1_photo,
                                         caption=caption,
                                         reply_markup=key_case_one_game(int(var[1])))


# ЗАПИСЬ БАЛАНСА БОТА И МАКСИМАЛЬНОГО ВЫИГРЫША ЗА СУТКИ
@dp.callback_query_handler(text_contains='case_one_ticket')
async def case_one_ticket(call: CallbackQuery):
    if variable.block_case == 1:
        await call.answer('Кейсы заблокирована на несколько минут', cache_time=20)
    else:
        data = call.data.split("_", 3)
        if variable.case_1_change_increment != int(data[3]):
            await call.answer('Кейсы обновились', show_alert=True)
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            data = await db.select_ticket_user(user_id=call.message.chat.id, x=1)
            caption = f'''🗃 <b>Кейс на {variable.case_1_name}</b>
ℹ <b>Описание:</b> {variable.case_1_description}.

💰 <b>Стоимость:</b> {variable.case_1_cost}₽

'''
            await bot.send_photo(chat_id=call.message.chat.id,
                                 photo=variable.case_1_photo,
                                 caption=caption,
                                 reply_markup=key_case_one_game(int(data)))
        else:
            var = await db.select_ticket_user(user_id=call.message.chat.id, x=1)
            if int(var[0]) < 1:
                await call.answer('У вас недостаточно билетов', show_alert=True, cache_time=10)
            else:
                await call.answer()
                data = await case_data_one_ticket()
                delta = 0
                if datetime.now() - var[2] > timedelta(1):
                    delta = 1
                if data[4] == '🔥':
                    if delta == 1:
                        await db.update_case_win_balance_and_ticket(user_id=call.message.chat.id,
                                                                    x=1, balance=0, y=0, par='🎟 на 🔥')
                    else:
                        await db.update_case_balance_and_ticket(user_id=call.message.chat.id, x=1, balance=0)
                else:
                    from data import config
                    win = int(data[4])
                    if delta == 1 or var[1] < win:
                        if win > 0:
                            await db.update_case_win_balance_and_ticket(user_id=call.message.chat.id, x=1,
                                                                        balance=win * 10000, y=win, par='🎟 на 🔥')
                        else:
                            await db.update_case_win_balance_and_ticket(user_id=call.message.chat.id, x=1,
                                                                        balance=win * 10000, y=0, par='🎟 на 🔥')
                    else:
                        await db.update_case_balance_and_ticket(user_id=call.message.chat.id, x=1,
                                                                balance=win * 10000)
                    notification = f'''Кейс НОВИЧОК 🎟 на 🔥
id: #user{call.message.chat.id}
name: {call.message.chat.full_name}
win: {win}'''
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
                await sleep(0.7)
                if data[4] != '🔥':
                    await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                        message_id=call.message.message_id,
                                                        reply_markup=key_case_1_win(data[4], int(var[0])-1))
                else:
                    from data import config
                    caption = f'Поздравляем!\nВы выиграли {variable.case_1_name}.\n' \
                              f'Обратитесь к администратору для получения приза'
                    await bot.edit_message_caption(chat_id=call.message.chat.id,
                                                   message_id=call.message.message_id,
                                                   caption=caption,
                                                   reply_markup=key_animation('🔥'))
                    text = f'Пользователь {call.message.chat.id} выиграл {variable.case_1_name}'
                    await bot.send_message(chat_id=config.chat, text=text)
                    caption = f'''🗃 <b>Кейс на {variable.case_1_name}</b>
ℹ <b>Описание:</b> {variable.case_1_description}.

💰 <b>Стоимость:</b> {variable.case_1_cost}₽

'''
                    await bot.send_photo(chat_id=call.message.chat.id,
                                         photo=variable.case_1_photo,
                                         caption=caption,
                                         reply_markup=key_case_one_game(int(var[0])-1))
