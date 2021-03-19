from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.admins.other.misc import mod_set
from keyboards.inline.admins.start_key import adm_start
from loader import dp, bot
from data import config


@dp.message_handler(CommandStart(), user_id=config.admins)
async def bot_start_adm(message: types.Message):
    text = 'Выбирай настройки:\n\nТут много писать смысла нет'
    await message.answer(text=text, reply_markup=adm_start)


@dp.message_handler(CommandStart(), user_id=config.moderators)
async def bot_start_moder(message: types.Message):
    text = '''Общие настройки:

    🗃 <b>Настройка кейсов:</b> меняешь каждый кейс по выбору

    ⚫ <b>Лотерея:</b> распределение ставок и запуск

    🎰 <b>Розыгрыш:</b> запуск розыгрыша на канале

    ✅ <b>Блок:</b> блокировка игровой части бота

    💰 <b>Пополнить баланс 🔑:</b> смена баланса и ключей
    Меняется вместе с балансом бота'''
    await message.answer(text=text, reply_markup=mod_set(message.chat.id))


@dp.callback_query_handler(text='back_start_adm', user_id=config.admins)
async def back_start_adm(call: types.CallbackQuery):
    await call.answer()
    text = 'Выбирай настройки:\n\nТут много писать смысла нет'
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=adm_start)

