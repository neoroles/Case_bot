from datetime import datetime, timedelta

from aiogram.types import CallbackQuery

from keyboards.inline.users.keyboard_bonus import key_bonus, key_bonus_game
from loader import dp, bot, db
from utils.create_bonus import bonus_create


@dp.callback_query_handler(text='get_free')
async def get_free(call: CallbackQuery):
    await call.answer()
    text = '''<b>🎁 Бонус</b>

Каждый день ты можешь получать бонусы. 
Но, если их тебе будет мало, то не забудь заглянуть на наш канал или пригласить своих друзей в бота.'''
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=key_bonus())


@dp.callback_query_handler(text='prize')
async def prize(call: CallbackQuery):
    var = await db.select_get_free(call.message.chat.id)
    delta = 0
    if datetime.now() - var[4] > timedelta(1):
        delta = 1
    if var[0] < 1 and delta == 0:
        await call.answer('Сегодня вы использовали все свои попытки', show_alert=True, cache_time=10)
    elif delta == 1:
        await call.answer()
        if 10 > var[7] >= 3:
            attempts = 4
        elif var[7] >= 10:
            attempts = 5
        else:
            attempts = 3
        await db.update_get_free_start(call.message.chat.id, x=attempts)
        text = f'''🎁 <b>Ежедневный бонус</b> 

Здесь можно получить на халяву 💰, которые можно потратить на мини-игры и кейсы.  

📍Доступно открытий: {attempts}'''
        await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=key_bonus_game(0, 0, 0, 0, 0, '', '', '', '', ''))
    else:
        await call.answer()
        x = 0
        x_var = ''
        if len(var[1]) > 2:
            var_1 = str(var[1]).split(' - ', 1)
            x = int(var_1[0])
            x_var = str(var_1[1])
        y = 0
        y_var = ''
        if len(var[2]) > 2:
            var_2 = str(var[2]).split(' - ', 1)
            y = int(var_2[0])
            y_var = str(var_2[1])
        z = 0
        z_var = ''
        if len(var[3]) > 2:
            var_3 = str(var[3]).split(' - ', 1)
            z = int(var_3[0])
            z_var = str(var_3[1])
        k = 0
        k_var = ''
        m = 0
        m_var = ''
        if 10 > var[7] >= 3:
            if len(var[5]) > 2:
                var_5 = str(var[4]).split(' - ', 1)
                k = int(var_5[0])
                k_var = str(var_5[1])
        elif var[7] >= 10:
            if len(var[5]) > 2:
                var_5 = str(var[5]).split(' - ', 1)
                k = int(var_5[0])
                k_var = str(var_5[1])
            if len(var[6]) > 2:
                var_6 = str(var[6]).split(' - ', 1)
                m = int(var_6[0])
                m_var = str(var_6[1])
        text = f'''🎁 <b>Ежедневный бонус</b> 

Здесь можно получить на халяву 💰, которые можно потратить на мини-игры и кейсы.  

📍Доступно открытий: {var[0]}'''
        await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=key_bonus_game(x, y, z, k, m, x_var, y_var, z_var, k_var, m_var))


@dp.callback_query_handler(text_contains='bonus_default')
async def bonus_default(call: CallbackQuery):
    from data import config
    var = await db.select_get_free(call.message.chat.id)
    delta = 0
    if datetime.now() - var[4] > timedelta(1):
        delta = 1
    if var[0] < 1 and delta == 0:
        await call.answer('Сегодня вы использовали все свои попытки', show_alert=True, cache_time=10)
    elif delta == 1:
        await call.answer()
        if 10 > var[7] >= 3:
            attempts = 4
        elif var[7] >= 10:
            attempts = 5
        else:
            attempts = 3
        m = str(call.data).split('_', 2)[2]
        n = await bonus_create(user_id=call.message.chat.id)
        x = m + ' - ' + n
        notification = f'''Ежедневный бонус
id: #user{call.message.chat.id}
name: {call.message.chat.full_name}
win: {x}'''
        await bot.send_message(chat_id=config.logs_users_channel, text=notification)
        await db.update_get_free_start_next(call.message.chat.id, x, attempts)
        text = f'''🎁 <b>Ежедневный бонус</b> 

Здесь можно получить на халяву 💰, которые можно потратить на мини-игры и кейсы.  

📍Доступно открытий: {attempts-1}'''
        await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=key_bonus_game(int(m), 0, 0, 0, 0, f'{n}', '', '', '', ''))
    else:
        await call.answer()
        x = 0
        x_var = ''
        y = 0
        y_var = ''
        z = 0
        z_var = ''
        k = 0
        k_var = ''
        m = 0
        m_var = ''
        if len(var[1]) <= 1:
            x = str(call.data).split('_', 2)[2]
            x_var = await bonus_create(user_id=call.message.chat.id)
            par = x + ' - ' + x_var
            notification = f'''Ежедневный бонус
id: #user{call.message.chat.id}
name: {call.message.chat.full_name}
win: {par}'''
            await bot.send_message(chat_id=config.logs_users_channel, text=notification)
            await db.update_data_get_free(call.message.chat.id, par)
        elif len(var[1]) > 1:
            var_1 = str(var[1]).split(' - ', 1)
            x = int(var_1[0])
            x_var = str(var_1[1])
            if len(var[2]) <= 1:
                y = str(call.data).split('_', 2)[2]
                y_var = await bonus_create(user_id=call.message.chat.id)
                par = y + ' - ' + y_var
                notification = f'''Ежедневный бонус
id: #user{call.message.chat.id}
name: {call.message.chat.full_name}
win: {par}'''
                await bot.send_message(chat_id=config.logs_users_channel, text=notification)
                await db.update_get_free(call.message.chat.id, par, 2)
            elif len(var[2]) > 1:
                var_2 = str(var[2]).split(' - ', 1)
                y = int(var_2[0])
                y_var = str(var_2[1])
                if len(var[3]) <= 1:
                    z = str(call.data).split('_', 2)[2]
                    z_var = await bonus_create(user_id=call.message.chat.id)
                    par = z + ' - ' + z_var
                    notification = f'''Ежедневный бонус
id: #user{call.message.chat.id}
name: {call.message.chat.full_name}
win: {par}'''
                    await bot.send_message(chat_id=config.logs_users_channel, text=notification)
                    await db.update_get_free(call.message.chat.id, par, 3)
                elif len(var[3]) >= 1:
                    var_3 = str(var[3]).split(' - ', 1)
                    z = int(var_3[0])
                    z_var = str(var_3[1])
                    if len(var[5]) <= 1:
                        k = str(call.data).split('_', 2)[2]
                        k_var = await bonus_create(user_id=call.message.chat.id)
                        par = k + ' - ' + k_var
                        notification = f'''Ежедневный бонус
id: #user{call.message.chat.id}
name: {call.message.chat.full_name}
win: {par}'''
                        await bot.send_message(chat_id=config.logs_users_channel, text=notification)
                        await db.update_get_free(call.message.chat.id, par, 4)
                    elif len(var[5]) >= 1:
                        var_5 = str(var[5]).split(' - ', 1)
                        k = int(var_5[0])
                        k_var = str(var_5[1])
                        if len(var[6]) <= 1:
                            m = str(call.data).split('_', 2)[2]
                            m_var = await bonus_create(user_id=call.message.chat.id)
                            par = m + ' - ' + m_var
                            notification = f'''Ежедневный бонус
id: #user{call.message.chat.id}
name: {call.message.chat.full_name}
win: {par}'''
                            await bot.send_message(chat_id=config.logs_users_channel, text=notification)
                            await db.update_get_free(call.message.chat.id, par, 5)
                        elif len(var[6]) >= 1:
                            var_6 = str(var[6]).split(' - ', 1)
                            m = int(var_6[0])
                            m_var = str(var_6[1])

        text = f'''🎁 <b>Ежедневный бонус</b> 

Здесь можно получить на халяву 💰, которые можно потратить на мини-игры и кейсы.  

📍Доступно открытий: {var[0]-1}'''
        await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=key_bonus_game(int(x), int(y), int(z), int(k), int(m),
                                                                x_var, y_var, z_var, k_var, m_var))
