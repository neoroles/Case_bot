from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def key_case_secret_game(x):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f'Открыть за 🔑({x})', callback_data='case_secret_key')
            ],
            [
                InlineKeyboardButton(text='« Назад', callback_data='cases_back')
            ]
        ]
    )
    return keyboard


def key_case_secret_win(x, key):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='➡️', callback_data='case_animation'),
                InlineKeyboardButton(text=f'{x}', callback_data='case_animation'),
                InlineKeyboardButton(text='⬅️', callback_data='case_animation')
            ],
            [
                InlineKeyboardButton(text=f'Открыть за 🔑({key})', callback_data='case_secret_key')
            ],
            [
                InlineKeyboardButton(text='« Назад', callback_data='cases_back')
            ]
        ]
    )
    return keyboard
