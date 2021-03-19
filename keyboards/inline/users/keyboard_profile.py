from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def key_profile():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='💰 Баланс', callback_data='profile:cash'),
                InlineKeyboardButton(text='👫 Приглашения', callback_data='profile:invite')
            ],
            [
                InlineKeyboardButton(text='« Назад', callback_data='back_start')
            ]
        ]
    )
    return keyboard
