from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def key_invite(r):
    keyboard = ''
    if r == 0:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='« Назад', callback_data='back_start')
                ]
            ]
        )
    elif r == 1:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='« Назад', callback_data='profile')
                ]
            ]
        )
    elif r == 2:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='« Назад', callback_data='get_free')
                ]
            ]
        )
    return keyboard
