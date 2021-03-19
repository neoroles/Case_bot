from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# key_start = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Профиль', callback_data='profile')
#         ],
#         [
#             InlineKeyboardButton(text='Кейсы', callback_data='cases')
#         ],
#         [
#             InlineKeyboardButton(text='Лотерея', callback_data='lottery')
#         ],
#         [
#             InlineKeyboardButton(text='nvuti', callback_data='nvuti')
#         ]
#     ]
# )


key_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🎰 Игры', callback_data='games'),
            InlineKeyboardButton(text='🗃 Кейсы', callback_data='cases')
        ],
        [
            InlineKeyboardButton(text='🏆 Таблица лидеров', callback_data='leaderboard')
        ],
        [
            InlineKeyboardButton(text='🎁 Бонус', callback_data='get_free'),
            InlineKeyboardButton(text='💵 Баланс', callback_data='cash')
        ],
        [
            InlineKeyboardButton(text='💼 Профиль', callback_data='profile'),
            InlineKeyboardButton(text='👫 Приглашения', callback_data='invite')
        ],
        [
            InlineKeyboardButton(text='💡 Информация о проекте', callback_data='about_me')
        ]
    ]
)