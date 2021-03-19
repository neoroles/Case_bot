from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

adm_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ситемные настройки', callback_data='sys_setting')
        ],
        [
            InlineKeyboardButton(text='Общие настройки', callback_data='other_setting')
        ]
    ]
)



