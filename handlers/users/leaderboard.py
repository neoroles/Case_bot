from aiogram.types import CallbackQuery

from keyboards.inline.users.keyboard_leaderboard import key_leaderboard, key_game_leaderboard
from loader import dp, bot, db


@dp.callback_query_handler(text='leaderboard')
async def leaderboard(call: CallbackQuery):
    await call.answer('Статистику можно запрашивать раз в 5 минут', show_alert=True, cache_time=10)
    wins = await db.select_stat_top_win()
    top_win = '<b>🔝 Топ по выигрышам за 24ч.</b>\n'
    for n, var in enumerate(wins, 1):
        name = f'<a href="tg://user?id={var[0]}">{var[1]}</a>'
        top_win = top_win + str(n) + '. ' + str(name) + ' - ' + str(var[2]) + ' ₽ ' + str(var[3]) + '\n'
    top_balance = '<b>💰 Топ по Балансу</b>\n'
    bal = await db.select_stat_top_bal()
    for n, var in enumerate(bal, 1):
        name = f'<a href="tg://user?id={var[0]}">{var[1]}</a>'
        top_balance = top_balance + str(n) + '. ' + str(name) + ' - ' + str(var[2]//10000) + ' ₽\n'
    top_case_all = '<b>🗃 Топ по количеству Открытий</b>\n'
    case_all = await db.select_stat_top_case_all()
    for n, var in enumerate(case_all, 1):
        name = f'<a href="tg://user?id={var[0]}">{var[1]}</a>'
        top_case_all = top_case_all + str(n) + '. ' + str(name) + ' - ' + str(var[2]) + ' шт.\n'
    top_up_sum = '<b>💸 Топ по сумме пополнений</b>\n'
    up_sum = await db.select_stat_top_up_sum()
    for n, var in enumerate(up_sum, 1):
        name = f'<a href="tg://user?id={var[0]}">{var[1]}</a>'
        top_up_sum = top_up_sum + str(n) + '. ' + str(name) + ' - ' + str(var[2]) + ' ₽\n'
    top_key = '<b>🔑 Топ по ключам</b>\n'
    key = await db.select_stat_top_key()
    for n, var in enumerate(key, 1):
        name = f'<a href="tg://user?id={var[0]}">{var[1]}</a>'
        top_key = top_key + str(n) + '. ' + str(name) + ' - ' + str(var[2]) + ' шт.\n'
    top_friend = '<b>👥 Топ по количеству друзей</b>\n'
    friend = await db.select_stat_top_friend()
    for n, var in enumerate(friend, 1):
        name = f'<a href="tg://user?id={var[0]}">{var[1]}</a>'
        top_friend = top_friend + str(n) + '. ' + str(name) + ' - ' + str(var[2]) + ' шт.\n'
    text = top_win + '\n' + top_balance + '\n' + top_case_all + '\n' +\
        top_up_sum + '\n' + top_key + '\n' + top_friend + '\n'
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                disable_web_page_preview=True,
                                reply_markup=key_leaderboard)


@dp.callback_query_handler(text='game_leaderboard')
async def game_leaderboard(call: CallbackQuery):
    await call.answer('Статистику можно запрашивать раз в 5 минут', show_alert=True, cache_time=10)
    top_get_free = '<b>🎁 Топ по количеству бонусов</b>\n'
    get_free = await db.select_stat_top_get_free()
    for n, var in enumerate(get_free, 1):
        name = f'<a href="tg://user?id={var[0]}">{var[1]}</a>'
        top_get_free = top_get_free + str(n) + '. ' + str(name) + ' - ' + str(var[2]) + ' шт.\n'
    top_lottery_col_win = '<b>🎱 Топ по победам в лотерею</b>\n'
    lottery_col_win = await db.select_stat_top_lottery_col_win()
    for n, var in enumerate(lottery_col_win, 1):
        name = f'<a href="tg://user?id={var[0]}">{var[1]}</a>'
        top_lottery_col_win = top_lottery_col_win + str(n) + '. ' + str(name) + ' - ' + str(var[2]) + ' шт.\n'
    top_lottery_win = '<b>🔝 Топ по выигрышам в лотерею</b>\n'
    lottery_win = await db.select_stat_top_lottery_win()
    for n, var in enumerate(lottery_win, 1):
        name = f'<a href="tg://user?id={var[0]}">{var[1]}</a>'
        top_lottery_win = top_lottery_win + str(n) + '. ' + str(name) + ' - ' + str(var[2]) + ' ₽.\n'
    top_nv_all_game = '<b>🎮 Топ по победам в "Угадай число"</b>\n'
    nv_all_game = await db.select_stat_top_lottery_nv_all_game()
    for n, var in enumerate(nv_all_game, 1):
        name = f'<a href="tg://user?id={var[0]}">{var[1]}</a>'
        top_nv_all_game = top_nv_all_game + str(n) + '. ' + str(name) + ' - ' + str(var[2]) + ' шт.\n'
    top_nv_all_win = '<b>🔝 Топ по выигрышам в "Угадай число"</b>\n'
    nv_all_win = await db.select_stat_top_lottery_nv_all_win()
    for n, var in enumerate(nv_all_win, 1):
        name = f'<a href="tg://user?id={var[0]}">{var[1]}</a>'
        top_nv_all_win = top_nv_all_win + str(n) + '. ' + str(name) + ' - ' + str(var[2]) + ' ₽.\n'
    text = top_get_free + '\n' + top_lottery_col_win + '\n' + top_lottery_win + '\n' + top_nv_all_game + '\n' \
        + top_nv_all_win
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                disable_web_page_preview=True,
                                reply_markup=key_game_leaderboard)
