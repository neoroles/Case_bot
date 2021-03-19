from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data import config


def mod_set(user_id):
    if user_id in config.admins:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='🗃 Настройка кейсов 🗃', callback_data='case_set')
                ],
                [
                    InlineKeyboardButton(text='⚫ Лотерея 🔴', callback_data='stat_lottery'),
                    InlineKeyboardButton(text='🎰 Розыгрыш', callback_data='drawing'),
                    InlineKeyboardButton(text='✅ Блок 🚫', callback_data='block')
                ],
                [
                    InlineKeyboardButton(text='💰 Пополнить баланс 🔑', callback_data='up_balance')
                ],
                [
                    InlineKeyboardButton(text='« Назад', callback_data='back_start_adm')
                ]
            ]
        )
    else:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='🗃 Настройка кейсов 🗃', callback_data='case_set')
                ],
                [
                    InlineKeyboardButton(text='⚫ Лотерея 🔴', callback_data='stat_lottery'),
                    InlineKeyboardButton(text='🎰 Розыгрыш 🎰', callback_data='drawing'),
                    InlineKeyboardButton(text='✅ Блок 🚫', callback_data='block')
                ],
                [
                    InlineKeyboardButton(text='💰 Пополнить баланс 🔑', callback_data='up_balance')
                ]
            ]
        )
    return keyboard


mod_editor_case = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🗃 1', callback_data='editor_case_1'),
            InlineKeyboardButton(text='🗃 2', callback_data='editor_case_2'),
            InlineKeyboardButton(text='🗃 3', callback_data='editor_case_3'),
        ],
[
            InlineKeyboardButton(text='🗃 4', callback_data='editor_case_4'),
            InlineKeyboardButton(text='🗃 5', callback_data='editor_case_5'),
            InlineKeyboardButton(text='🗃 6', callback_data='editor_case_6'),
        ],
        [
            InlineKeyboardButton(text='Секретный кейс', callback_data='edit_case_secret')
        ],
        [
            InlineKeyboardButton(text='« Назад', callback_data='other_setting')
        ]

    ]
)

mod_lottery = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Распределние ⚫|🔴', callback_data='mod_lottery_bet')
        ],
        [
            InlineKeyboardButton(text='Запустить лотерею ⚠', callback_data='start_lottery')
        ],
        [
            InlineKeyboardButton(text='« Назад', callback_data='other_setting')
        ]
    ]
)