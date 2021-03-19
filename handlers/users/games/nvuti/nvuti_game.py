from datetime import timedelta, datetime
from asyncio import sleep

from aiogram.types import CallbackQuery

from data import variable
from keyboards.inline.users.game.nvuti.keyboard_nvuti_game import key_nvuti_game, key_nvuti_game_back
from loader import dp, db, bot
from utils.nvuti_const import create_const_nvuti_big, create_const_nvuti_small, check_win
from utils.update_balance import change_balance


@dp.callback_query_handler(text='nv_game')
async def nv_game(call: CallbackQuery):
    if variable.block_nvuti == 1:
        await call.answer('nvuti Временно заблокирована')
    else:
        data = await db.select_nvuti(call.message.chat.id)
        if data[0] < data[3]:
            await call.answer('Ваша ставка не должна превышать ваш баланс', show_alert=True, cache_time=3)
        else:
            await call.answer()
            if data[2] > 50:
                nv_min, nv_user_min, nv_max, nv_user_max = await create_const_nvuti_big(data[2])
            else:
                nv_min, nv_user_min, nv_max, nv_user_max = await create_const_nvuti_small(data[2])
            await db.update_nv_const(user_id=call.message.chat.id, nv_min=nv_min, nv_max=nv_max,
                                     nv_user_min=nv_user_min, nv_user_max=nv_user_max)
            win = round((data[3] * data[1] // 10000 - data[3]) / 10000, 2)
            text = f'''*🎮  Угадай число > Режим игры*

📈 *Вероятность победы:* {data[2]}%
⚖️*Возможный выигрыш:* {win} ₽

↕: *{nv_min}*<========>*{nv_max}*
🔼: {nv_user_max}====>*{nv_max}*
🔽: *{nv_min}*<===={nv_user_min}
'''
            await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                        message_id=call.message.message_id, parse_mode='Markdown',
                                        reply_markup=key_nvuti_game)


@dp.callback_query_handler(text='nv_game_max')
async def nv_game_max(call: CallbackQuery):
    if variable.block_nvuti == 1:
        await call.answer('nvuti Временно заблокирована')
    else:
        data = await db.select_nv_game_const(call.message.chat.id)
        if data[0] < data[3]:
            await call.answer('Ваша ставка не должна превышать ваш баланс', show_alert=True, cache_time=3)
        else:
            from data import config
            win = data[3] * data[1] // 10000 - data[3]
            from random import randint
            winner = await check_win(win, data[2], user_id=call.message.chat.id)
            if winner == 0:
                result = randint(data[4], data[7])
                answer = f'''*Поражение*
↕: *{data[4]}*<========>*{data[5]}*
🔼: {data[7]}====>*{data[5]}*
🔽: *{data[4]}*<===={data[6]}

*Бот загадал* {result}
'''
                win = -data[3]
                max_win = 0
                await call.answer('Ты проиграл', show_alert=True)
                await change_balance(balance_all=0, balance_bot=-win)
            else:
                result = randint(data[7], data[5])
                answer = f'''*Победа*
↕: *{data[4]}*<========>*{data[5]}*
🔼: {data[7]}====>*{data[5]}*
🔽: *{data[4]}*<===={data[6]}

*Бот загадал* {result}
'''
                # win = data[3] * data[1] // 10000 - data[3]
                max_win = (data[3] * data[1] / 10000 - data[3]) // 10000
                await call.answer(f'Ты выиграл {max_win}', show_alert=True)
                await change_balance(balance_all=0, balance_bot=-win)
            notification = f'''Нвути 🎮
id: #user{call.message.chat.id}
name: {call.message.chat.full_name}
win: {round(win/10000, 2)}'''
            await bot.send_message(chat_id=config.logs_users_channel, text=notification)
            delta = 1 if datetime.now() - data[9] > timedelta(1) else 0
            if data[0] - data[3] < data[3] and winner == 0:
                if delta == 1:
                    await db.update_game_nvuti_lose_max_win(user_id=call.message.chat.id, x=win, max_win=max_win,
                                                            par='🎮')
                else:
                    await db.update_game_nvuti_lose(user_id=call.message.chat.id, x=win, max_win=max_win)
                await bot.edit_message_text(text=answer, chat_id=call.message.chat.id, parse_mode='Markdown',
                                            message_id=call.message.message_id)
                text = 'На вашем балансе не достаточно средств'
                await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key_nvuti_game_back)
            else:
                if data[2] > 50:
                    nv_min, nv_user_min, nv_max, nv_user_max = await create_const_nvuti_big(data[2])
                else:
                    nv_min, nv_user_min, nv_max, nv_user_max = await create_const_nvuti_small(data[2])
                if delta == 1 or data[8] < max_win:
                    await db.update_after_nvuti_max_win(user_id=call.message.chat.id, x=win, max_win=max_win, par='🎮',
                                                        nv_min=nv_min, nv_max=nv_max, nv_user_min=nv_user_min,
                                                        nv_user_max=nv_user_max)
                else:
                    await db.update_after_nvuti(user_id=call.message.chat.id, x=win,
                                                nv_min=nv_min, nv_max=nv_max, nv_user_min=nv_user_min,
                                                nv_user_max=nv_user_max, max_win=max_win)
                await bot.edit_message_text(text=answer, chat_id=call.message.chat.id, parse_mode='Markdown',
                                            message_id=call.message.message_id)
                possible_victory = round((data[3] * data[1] // 10000 - data[3]) / 10000, 2)
                text = f'''*🎮  Угадай число > Режим игры*

📈 *Вероятность победы:* {data[2]}%
⚖️*Возможный выигрыш:* {possible_victory} ₽

↕: *{nv_min}*<========>*{nv_max}*
🔼: {nv_user_max}====>*{nv_max}*
🔽: *{nv_min}*<===={nv_user_min}
'''
                await sleep(1)
                await bot.send_message(chat_id=call.message.chat.id, text=text, parse_mode='Markdown',
                                       reply_markup=key_nvuti_game)


@dp.callback_query_handler(text='nv_game_min')
async def nv_game_max(call: CallbackQuery):
    if variable.block_nvuti == 1:
        await call.answer('nvuti Временно заблокирована')
    else:
        data = await db.select_nv_game_const(call.message.chat.id)
        if data[0] < data[3]:
            await call.answer('Ваша ставка не должна превышать ваш баланс', show_alert=True, cache_time=3)
        else:
            from data import config
            win = data[3] * data[1] // 10000 - data[3]
            from random import randint
            winner = await check_win(win, data[2], user_id=call.message.chat.id)
            if winner == 0:
                result = randint(data[6], data[5])
                answer = f'''*Поражение*
↕: *{data[4]}*<========>*{data[5]}*
🔼: {data[7]}====>*{data[5]}*
🔽: *{data[4]}*<===={data[6]}

*Бот загадал* {result}
'''
                win = -data[3]
                max_win = 0
                await call.answer('Ты проиграл', show_alert=True)
                await change_balance(balance_all=0, balance_bot=-win)
            else:
                result = randint(data[4], data[6])
                answer = f'''*Победа*
↕: *{data[4]}*<========>*{data[5]}*
🔼: {data[7]}====>*{data[5]}*
🔽: *{data[4]}*<===={data[6]}

*Бот загадал* {result}
'''
                # win = data[3]*data[1]//10000-data[3]
                max_win = (data[3] * data[1]/10000 - data[3]) // 10000
                await call.answer(f'Ты выиграл {max_win}', show_alert=True)
                await change_balance(balance_all=0, balance_bot=-win)
            notification = f'''Нвути 🎮
id: #user{call.message.chat.id}
name: {call.message.chat.full_name}
win: {round(win/10000, 2)}'''
            await bot.send_message(chat_id=config.logs_users_channel, text=notification)
            delta = 1 if datetime.now() - data[9] > timedelta(1) else 0
            if data[0] - data[3] < data[3] and winner == 0:
                if delta == 1:
                    await db.update_game_nvuti_lose_max_win(user_id=call.message.chat.id, x=win, max_win=max_win,
                                                            par='🎮')
                else:
                    await db.update_game_nvuti_lose(user_id=call.message.chat.id, x=win)
                await bot.edit_message_text(text=answer, chat_id=call.message.chat.id, parse_mode='Markdown',
                                            message_id=call.message.message_id)
                text = 'На вашем балансе не достаточно средств'
                await bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=key_nvuti_game_back)
            else:
                if data[2] > 50:
                    nv_min, nv_user_min, nv_max, nv_user_max = await create_const_nvuti_big(data[2])
                else:
                    nv_min, nv_user_min, nv_max, nv_user_max = await create_const_nvuti_small(data[2])
                if delta == 1 or data[8] < max_win:
                    await db.update_after_nvuti_max_win(user_id=call.message.chat.id, x=win, max_win=max_win, par='🎮',
                                                        nv_min=nv_min, nv_max=nv_max, nv_user_min=nv_user_min,
                                                        nv_user_max=nv_user_max)
                else:
                    await db.update_after_nvuti(user_id=call.message.chat.id, x=win,
                                                nv_min=nv_min, nv_max=nv_max, nv_user_min=nv_user_min,
                                                nv_user_max=nv_user_max, max_win=max_win)
                await bot.edit_message_text(text=answer, chat_id=call.message.chat.id, parse_mode='Markdown',
                                            message_id=call.message.message_id)
                possible_victory = round((data[3] * data[1] // 10000 - data[3]) / 10000, 2)
                text = f'''*🎮  Угадай число > Режим игры*

📈 *Вероятность победы:* {data[2]}%
⚖️*Возможный выигрыш:* {possible_victory} ₽

↕: *{nv_min}*<========>*{nv_max}*
🔼: {nv_user_max}====>*{nv_max}*
🔽: *{nv_min}*<===={nv_user_min}
'''
                await sleep(1)
                await bot.send_message(chat_id=call.message.chat.id, text=text, parse_mode='Markdown',
                                       reply_markup=key_nvuti_game)


