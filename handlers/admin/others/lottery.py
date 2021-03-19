from aiogram.types import CallbackQuery

from data import variable, config
from data.config import moderators
from keyboards.inline.admins.other.misc import mod_lottery
from loader import dp, bot, db
from utils.update_balance import change_balance


@dp.callback_query_handler(text='stat_lottery', user_id=config.moderators)
async def stat_lottery(call: CallbackQuery):
    await call.answer()
    text = '''<b>Лотерея</b>

<b>Распределние ⚫|🔴</b>: посмотреть кол-во и суммы ставок

<b>Запустить лотерею ⚠</b>: запустить можно, когда набралось больше 10 участников

Лотерея запускается вручную ибо я не нашел простого решения сделать это по времени'''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=mod_lottery)


@dp.callback_query_handler(text='mod_lottery_bet', user_id=config.moderators)
async def check_lottery_bet(call: CallbackQuery):
    await call.answer()
    one = await db.stat_lottery(1)
    two = await db.stat_lottery(2)
    text = f'''Статистика лотереи
    
⚫ <b>Черное</b>
Сумма: {one[0]}
Количество: {one[1]}

🔴 <b>Красное</b>
Сумма: {two[0]}
Количество: {two[1]}
'''
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                        message_id=call.message.message_id)
    await bot.send_message(chat_id=call.message.chat.id, text=text, disable_notification=True)
    text_2 = '''<b>Лотерея</b>

<b>Распределние ⚫|🔴</b>: посмотреть кол-во и суммы ставок

<b>Запустить лотерею ⚠</b>: запустить можно, когда набралось больше 10 участников

Лотерея запускается вручную ибо я не нашел простого решения сделать это по времени'''
    await bot.send_message(text=text_2, chat_id=call.message.chat.id, reply_markup=mod_lottery)


@dp.callback_query_handler(text='start_lottery', user_id=config.moderators)
async def start_lottery(call: CallbackQuery):
    quantity = await db.stat_all_bets_lottery()
    if quantity < 10:
        await call.answer(f'Лотерея невозможна на такое кол-во человек({quantity})', show_alert=True)
    else:
        from asyncio import sleep
        await call.answer('Лотерея запущена', cache_time=60)
        one = await db.stat_lottery(1)
        two = await db.stat_lottery(2)
        if one[0] > two[1]:
            win = 2
            difference = one[0] - two[0]
            await change_balance(balance_all=two[0]*20000, balance_bot=difference*10000)
        else:
            win = 1
            difference = two[0] - one[0]
            await change_balance(balance_all=one[0] * 20000, balance_bot=difference * 10000)
        data = await db.users_lottery_active(win)
        variable.block_lottery = 1
        for user in data:
            try:
                await sleep(0.5)
                await db.up_balance_lottery(user[0], int(user[1])*20000, user[1])
                text = f'''Поздравляем!
                Вы выиграли в лотерею {user[1]} ₽'''
                await bot.send_message(user[0], text)
            except:
                await db.ban_user(user[0])
        await db.lottery_discharge()
        par = '⚫ Черное' if win == 1 else '🔴 Красное'
        notification = f'''В сегодняшней лотерее выиграло {par}'''
        await bot.send_message(chat_id=config.chat, text=notification)
        variable.block_lottery = 0





