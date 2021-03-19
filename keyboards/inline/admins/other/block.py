from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def block_key():
    from data import variable
    if variable.block_lottery == 0:
        one = InlineKeyboardButton(text='✅ Лотерея', callback_data='block_1')
    else:
        one = InlineKeyboardButton(text='🚫 Лотерея', callback_data='unlock_1')
    if variable.block_case == 0:
        two = InlineKeyboardButton(text='✅ Кейсы', callback_data='block_2')
    else:
        two = InlineKeyboardButton(text='🚫 Кейсы', callback_data='unlock_2')
    if variable.block_nvuti == 0:
        three = InlineKeyboardButton(text='✅ Нвути', callback_data='block_3')
    else:
        three = InlineKeyboardButton(text='🚫 Нвути', callback_data='unlock_3')
    four = InlineKeyboardButton(text='« Назад', callback_data='other_setting')
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                one,
                two,
                three
            ],
            [
                four
            ]
        ]
    )
    return keyboard
