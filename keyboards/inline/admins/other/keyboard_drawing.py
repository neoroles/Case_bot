from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

draw = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Участвовать', callback_data='draw')
        ]
    ]
)

draw_create = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='На скорость', callback_data='draw_on_speed'),
            InlineKeyboardButton(text='На рандом', callback_data='draw_on_random')
        ],
        [
            InlineKeyboardButton(text='« Назад', callback_data='other_setting')
        ]
    ]
)


create_or_active_on_speed = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Создать', callback_data='create_on_speed'),
            InlineKeyboardButton(text='Запустить', callback_data='active_on_speed')
        ],
        [
            InlineKeyboardButton(text='« Назад', callback_data='draw_on_speed')
        ]
    ]
)


create_back_on_speed = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Отмена', callback_data='draw_on_speed')
        ]
    ]
)