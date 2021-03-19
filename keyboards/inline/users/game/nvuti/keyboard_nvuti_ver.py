from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key_ver = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Макс', callback_data='nv_ver_max'),
            InlineKeyboardButton(text='Мин', callback_data='nv_ver_min')
        ],
        [
            InlineKeyboardButton(text='Удвоить', callback_data='nv_ver_2'),
            InlineKeyboardButton(text='Половина', callback_data='nv_ver_05')
        ],
        [
            InlineKeyboardButton(text='Ввести вручную', callback_data='nv_ver_input'),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='nvuti')
        ]
    ]
)


key_ver_input_back = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardMarkup(text='« Отмена »', callback_data='nv_change_ver')
        ]
    ]
)