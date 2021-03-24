from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key_leaderboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🎰 Игровая', callback_data='game_leaderboard')
        ],
        [
            InlineKeyboardButton(text='« Назад', callback_data='back_start')
        ]
    ]
)

key_game_leaderboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🏆 Основная', callback_data='leaderboard')
        ],
        [
            InlineKeyboardButton(text='« Назад', callback_data='back_start')
        ]
    ]
)