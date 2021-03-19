from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key_bet = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Макс', callback_data='nv_bet_max'),
            InlineKeyboardButton(text='Мин', callback_data='nv_bet_min')
        ],
        [
            InlineKeyboardButton(text='Удвоить', callback_data='nv_bet_2'),
            InlineKeyboardButton(text='Половина', callback_data='nv_bet_05')
        ],
        [
            InlineKeyboardButton(text='Ввести вручную', callback_data='nv_bet_input'),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='nvuti')
        ]
    ]
)

key_bet_input_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardMarkup(text='« Отмена »', callback_data='nv_change_bet')
        ]
    ]
)