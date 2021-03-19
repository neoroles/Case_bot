from datetime import datetime, timedelta

from aiogram.types import CallbackQuery
from asyncio import sleep

from keyboards.inline.users.case.main import key_case_animation, key_animation
from keyboards.inline.users.case.keyboard_case_6 import key_case_six_game, key_case_6_win
from loader import dp, bot, db
from utils.case_data_create import case_data_six_money, case_data_six_ticket
from data import variable


@dp.callback_query_handler(text='case_six')
async def case_six(call: CallbackQuery):
    if variable.block_case == 1:
        await call.answer('Кейсы заблокированы на несколько минут', cache_time=20)
    else:
        await call.answer()
        # Запрос на наличие билетов у пользователя
        data = await db.select_ticket_case(user_id=call.message.chat.id, x=6)
        await bot.delete_message(chat_id=call.message.chat.id,
                                 message_id=call.message.message_id)
        caption = f'''🗃 <b>Кейс на {variable.case_6_name}</b>
ℹ <b>Описание:</b> {variable.case_6_description}.

💰 <b>Стоимость:</b> {variable.case_6_cost}₽

'''
        await bot.send_photo(chat_id=call.message.chat.id,
                             photo=variable.case_6_photo,
                             caption=caption,
                             reply_markup=key_case_six_game(int(data)))


# ЗАПИСЬ БАЛАНСА БОТА
@dp.callback_query_handler(text_contains='case_six_money')
async def case_six_money(call: CallbackQuery):
    # Запрос на блокировку кейсов
    if variable.block_case == 1:
        await call.answer('Кейсы заблокирована на несколько минут', cache_time=20)
    else:
        # Запрос на обновление кейса
        data = call.data.split("_", 3)
        if variable.case_6_change_increment != int(data[3]):
            await call.answer('Кейсы обновились', show_alert=True)
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            data = await db.select_ticket_user(user_id=call.message.chat.id, x=6)
            caption = f'''🗃 <b>Кейс на {variable.case_6_name}</b>
ℹ <b>Описание:</b> {variable.case_6_description}.

💰 <b>Стоимость:</b> {variable.case_6_cost}₽

'''
            await bot.send_photo(chat_id=call.message.chat.id,
                                 photo=variable.case_6_photo,
                                 caption=caption,
                                 reply_markup=key_case_six_game(int(data)))
        else:
            var = await db.select_balance_and_ticked_user(user_id=call.message.chat.id, x=6)
            # Провекра балансов
            # Запрос билетов
            if var[0] // 10000 < variable.case_6_bet:
                await call.answer('На вашем балансе недостаточно средств', show_alert=True, cache_time=10)
            else:
                await call.answer()
                # Собственно сама функция расчета возможного выигрыша и рандом чисел
                data = await case_data_six_money(call.message.chat.id)
                delta = 0
                if datetime.now() - var[3] > timedelta(1):
                    delta = 1
                # Запись балансов
                # Функция подсчета максимального выигрыша за сутки
                if data[4] == '💎':
                    if delta == 1:
                        await db.update_case_win_user(user_id=call.message.chat.id,
                                                      balance=-variable.case_6_bet * 10000, x=6, y=0, par='💎')
                    else:
                        await db.update_case_balance(user_id=call.message.chat.id, balance=-variable.case_6_bet * 10000,
                                                     x=6)
                else:
                    from data import config
                    win = int(data[4]) - variable.case_6_bet
                    if delta == 1 or var[2] < win:
                        if win > 0:
                            await db.update_case_win_user(user_id=call.message.chat.id,
                                                          balance=win * 10000, x=6, y=win, par='💎')
                        else:
                            await db.update_case_win_user(user_id=call.message.chat.id,
                                                          balance=win * 10000, x=6, y=0, par='💎')
                    else:
                        await db.update_case_balance(user_id=call.message.chat.id,
                                                     balance=win * 10000, x=6)
                    notification = f'''Кейс ОЛИГАРХ 💎
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
                if data[4] != '💎':
                    await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                        message_id=call.message.message_id,
                                                        reply_markup=key_case_6_win(data[4], int(var[1])))
                else:
                    from data import config
                    caption = f'Поздравляем!\nВы выиграли {variable.case_6_name}.\n' \
                              f'Обратитесь к администратору для получения приза'
                    await bot.edit_message_caption(chat_id=call.message.chat.id,
                                                   message_id=call.message.message_id,
                                                   caption=caption,
                                                   reply_markup=key_animation('💎'))
                    text = f'Пользователь {call.message.chat.id} выиграл {variable.case_6_name}'
                    await bot.send_message(chat_id=config.chat, text=text)
                    caption = f'''🗃 <b>Кейс на {variable.case_6_name}</b>
ℹ <b>Описание:</b> {variable.case_6_description}.

💰 <b>Стоимость:</b> {variable.case_6_cost}₽

'''
                    await bot.send_photo(chat_id=call.message.chat.id,
                                         photo=variable.case_6_photo,
                                         caption=caption,
                                         reply_markup=key_case_six_game(int(var[1])))


# ЗАПИСЬ БАЛАНСА БОТА
@dp.callback_query_handler(text_contains='case_six_ticket')
async def case_six_ticket(call: CallbackQuery):
    # Запрос на блокировку кейсов
    if variable.block_case == 1:
        await call.answer('Кейсы заблокирована на несколько минут', cache_time=20)
    else:
        # Запрос на обновление кейса
        data = call.data.split("_", 3)
        if variable.case_6_change_increment != int(data[3]):
            await call.answer('Кейсы обновились', show_alert=True)
            await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            data = await db.select_ticket_user(user_id=call.message.chat.id, x=6)
            caption = f'''🗃 <b>Кейс на {variable.case_6_name}</b>
ℹ <b>Описание:</b> {variable.case_6_description}.

💰 <b>Стоимость:</b> {variable.case_6_cost}₽

'''
            await bot.send_photo(chat_id=call.message.chat.id,
                                 photo=variable.case_6_photo,
                                 caption=caption,
                                 reply_markup=key_case_six_game(int(data)))
        else:
            # Запрос билетов
            var = await db.select_ticket_user(user_id=call.message.chat.id, x=6)
            if int(var[0]) < 1:
                await call.answer('У вас недостаточно билетов', show_alert=True, cache_time=10)
            else:
                await call.answer()
                # Собственно сама функция расчета возможного выигрыша и рандом чисел
                data = await case_data_six_ticket()
                delta = 0
                if datetime.now() - var[2] > timedelta(1):
                    delta = 1
                # Минус один билет
                if data[4] == '💎':
                    if delta == 1:
                        await db.update_case_win_balance_and_ticket(user_id=call.message.chat.id,
                                                                    x=6, balance=0, y=0, par='🎟 на 💎')
                    else:
                        # Запись в балансы суммы выигрыша
                        await db.update_case_balance_and_ticket(user_id=call.message.chat.id, x=6, balance=0)
                else:
                    from data import config
                    win = int(data[4])
                    if delta == 1 or var[1] < win:
                        if win > 0:
                            await db.update_case_win_balance_and_ticket(user_id=call.message.chat.id, x=6,
                                                                        balance=win * 10000, y=win, par='🎟 на 💎')
                        else:
                            await db.update_case_win_balance_and_ticket(user_id=call.message.chat.id, x=6,
                                                                        balance=win * 10000, y=0, par='🎟 на 💎')
                    else:
                        await db.update_case_balance_and_ticket(user_id=call.message.chat.id, x=6,
                                                                balance=win * 10000)
                    notification = f'''Кейс ОЛИГАРХ 🎟 на 💎
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
                if data[4] != '💎':
                    await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                        message_id=call.message.message_id,
                                                        reply_markup=key_case_6_win(data[4], int(var[0]) - 1))
                else:
                    from data import config
                    caption = f'Поздравляем!\nВы выиграли {variable.case_6_name}.\n' \
                              f'Обратитесь к администратору для получения приза'
                    await bot.edit_message_caption(chat_id=call.message.chat.id,
                                                   message_id=call.message.message_id,
                                                   caption=caption,
                                                   reply_markup=key_animation('💎'))
                    text = f'Пользователь {call.message.chat.id} выиграл {variable.case_6_name}'
                    await bot.send_message(chat_id=config.chat, text=text)
                    caption = f'''🗃 <b>Кейс на {variable.case_6_name}</b>
ℹ <b>Описание:</b> {variable.case_6_description}.

💰 <b>Стоимость:</b> {variable.case_6_cost}₽

'''
                    await bot.send_photo(chat_id=call.message.chat.id,
                                         photo=variable.case_6_photo,
                                         caption=caption,
                                         reply_markup=key_case_six_game(int(var[0]) - 1))