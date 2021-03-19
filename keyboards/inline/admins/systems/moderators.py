from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key_modarators = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Добавить', callback_data='add_moderators'),
            InlineKeyboardButton(text='Удалить', callback_data='del_moderators')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='sys_setting')
        ]
    ]
)