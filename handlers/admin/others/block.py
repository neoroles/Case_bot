from aiogram.types import CallbackQuery

from data import variable, config
from keyboards.inline.admins.other.block import block_key
from loader import dp, bot, db


@dp.callback_query_handler(text='block', user_id=config.moderators)
async def block(call: CallbackQuery):
    await call.answer()
    text = '''Вы можете заблокировать игры и кейсы
    
🚫 - Заблокировано
✅ - Не заблокировано'''
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=block_key())


@dp.callback_query_handler(text_contains='block', user_id=config.moderators)
async def block_func(call: CallbackQuery):
    if call.data[-1] == '1':
        await call.answer('Лотерея заблокирована', show_alert=True)
        await db.update_block_part(x=1, y=1)
        variable.block_lottery = 1
    elif call.data[-1] == '2':
        await call.answer('Кейсы заблокированы', show_alert=True)
        await db.update_block_part(x=2, y=1)
        variable.block_case = 1
    elif call.data[-1] == '3':
        await call.answer('НВУТИ заблокированы', show_alert=True)
        await db.update_block_part(x=3, y=1)
        variable.block_nvuti = 1
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=block_key())


@dp.callback_query_handler(text_contains='unlock', user_id=config.moderators)
async def block_func(call: CallbackQuery):
    if call.data[-1] == '1':
        await call.answer('Лотерея разблокирована', show_alert=True)
        await db.update_block_part(x=1, y=0)
        variable.block_lottery = 0
    elif call.data[-1] == '2':
        await call.answer('Кейсы разблокированы', show_alert=True)
        await db.update_block_part(x=2, y=0)
        variable.block_case = 0
    elif call.data[-1] == '3':
        await call.answer('НВУТИ разблокированы', show_alert=True)
        await db.update_block_part(x=3, y=0)
        variable.block_nvuti = 0
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=block_key())