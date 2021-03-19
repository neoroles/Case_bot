from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def key_about_me():
    from data import config
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🌐 Наш канал', url=f'{config.link_channel}')
            ],
            [
                InlineKeyboardButton(text='👥 Наш чат', url=f'{config.link_chat}')
            ],
            [
                InlineKeyboardButton(text='« Назад', callback_data='back_start')
            ]
        ]
    )
    return keyboard
