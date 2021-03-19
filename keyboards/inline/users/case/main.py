from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


key_cases = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔥 Новичок', callback_data='case_one'),
            InlineKeyboardButton(text='🌟 Везунчик', callback_data='case_two'),
            InlineKeyboardButton(text='🥇 Топовый', callback_data='case_three'),
        ],
        [
            InlineKeyboardButton(text='🃏 Фартовый', callback_data='case_four'),
            InlineKeyboardButton(text='🏆 Лакшери', callback_data='case_five'),
            InlineKeyboardButton(text='💎 Олигарх', callback_data='case_six')
        ],
        [
            InlineKeyboardButton(text='🔐 Секрет', callback_data='secret')
        ],
        [
            InlineKeyboardButton(text='« Назад', callback_data='back_start')
        ]
    ]
)


def key_case_animation(x, y, z):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f'{x}', callback_data='case_animation'),
                InlineKeyboardButton(text=f'{y}', callback_data='case_animation'),
                InlineKeyboardButton(text=f'{z}', callback_data='case_animation')
            ]
        ]
    )
    return keyboard

def key_animation(x):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='➡', callback_data='case_1_animation'),
                InlineKeyboardButton(text=f'{x}', callback_data='case_1_animation'),
                InlineKeyboardButton(text='⬅', callback_data='case_1_animation')
            ]
        ]
    )
    return keyboard
