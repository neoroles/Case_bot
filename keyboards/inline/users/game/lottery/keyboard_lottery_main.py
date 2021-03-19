from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key_lottery = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='⚫ Черное', callback_data='lottery_bet_1'),
            InlineKeyboardButton(text='🔴 Красное', callback_data='lottery_bet_2')
        ],
        [
            InlineKeyboardButton(text='« Назад', callback_data='back_game')
        ]
    ]
)

key_lottery_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='« Назад', callback_data='back_game')
        ]
    ]
)

key_lottery_bet_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='« Отмена »', callback_data='lottery')
        ]
    ]
)