from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key_back_system = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='sys_setting')
        ]
    ]
)