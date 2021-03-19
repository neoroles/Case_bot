from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key_nv = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Играть', callback_data='nv_game'),
        ],
        [
            InlineKeyboardButton(text='Изменить ставку', callback_data='nv_change_bet'),
            InlineKeyboardButton(text='Изменить вероятность', callback_data='nv_change_ver')
        ],
        [
            InlineKeyboardButton(text='« Назад', callback_data='back_game')
        ]
    ]
)