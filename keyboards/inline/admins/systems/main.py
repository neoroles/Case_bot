from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key_systems = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Статистика и реклама', callback_data='stat_and_advertisement')
        ],
        [
            InlineKeyboardButton(text='Победитель', callback_data='winner'),
            InlineKeyboardButton(text='% win', callback_data='win_percent')
        ],
        [
            InlineKeyboardButton(text='Реквизиты', callback_data='requisites'),
            InlineKeyboardButton(text='Партнеры', callback_data='partner')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='back_start_adm')
        ]
    ]
)