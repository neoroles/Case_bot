from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key_nvuti_game = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔼 Больше', callback_data='nv_game_max'),
            InlineKeyboardButton(text='🔽 Меньше', callback_data='nv_game_min')
        ],
        [
            InlineKeyboardButton(text='« Выйти »', callback_data='nvuti')
        ]
    ]
)

key_nvuti_game_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='« Выйти »', callback_data='nvuti')
        ]
    ]
)