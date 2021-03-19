from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key_game = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🎮 Угадай число', callback_data='nvuti'),
            InlineKeyboardButton(text='🎱 Лотерея', callback_data='lottery')
        ],
        [
            InlineKeyboardButton(text='« Назад', callback_data='back_start')
        ]
    ]
)