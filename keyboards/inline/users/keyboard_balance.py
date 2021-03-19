from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def key_cash(r):
    if r == 0:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='⬆️Пополнить', callback_data='up_balance'),
                    InlineKeyboardButton(text='⬇️Вывести', callback_data='down_balance')
                ],
                [
                    InlineKeyboardButton(text='« Назад', callback_data='back_start')
                ]
            ]
        )
    else:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='⬆️Пополнить', callback_data='up_balance'),
                    InlineKeyboardButton(text='⬇️Вывести', callback_data='down_balance')
                ],
                [
                    InlineKeyboardButton(text='« Назад', callback_data='profile')
                ]
            ]
        )
    return keyboard


key_back_up = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Отмена', callback_data='cash')
        ]
    ]
)


def key_payment_method():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='', callback_data='')
            ],
            [
                InlineKeyboardButton(text='', callback_data='')
            ],
            [
                InlineKeyboardMarkup(text='', callback_data='')
            ]
        ]
    )
    return keyboard
