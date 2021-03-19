from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def key_case_three_game(ticket):
    from data import variable
    if ticket <= 0:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f'Открыть за {variable.case_3_bet}₽',
                                         callback_data=f'case_three_money_{variable.case_3_change_increment}')
                ],
                [
                    InlineKeyboardButton(text='« Назад', callback_data='cases_back')
                ]
            ]
        )
    else:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f'Открыть за 🎟({ticket})',
                                         callback_data=f'case_three_ticket_{variable.case_3_change_increment}')
                ],
                [
                    InlineKeyboardButton(text=f'Открыть за {variable.case_3_bet}₽',
                                         callback_data=f'case_three_money_{variable.case_3_change_increment}')
                ],
                [
                    InlineKeyboardButton(text='« Назад', callback_data='cases_back')
                ]
            ]
        )
    return keyboard


def key_case_3_win(x, ticket):
    from data import variable
    if ticket <= 0:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='➡️', callback_data='case_animation'),
                    InlineKeyboardButton(text=f'{x}', callback_data='case_animation'),
                    InlineKeyboardButton(text='⬅️', callback_data='case_animation')
                ],
                [
                    InlineKeyboardButton(text=f'Открыть за {variable.case_3_bet}₽',
                                         callback_data=f'case_three_money_{variable.case_3_change_increment}')
                ],
                [
                    InlineKeyboardButton(text='« Назад', callback_data='cases_back')
                ]
            ]
        )
    else:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='➡️', callback_data='case_1_animation'),
                    InlineKeyboardButton(text=f'{x}', callback_data='case_1_animation'),
                    InlineKeyboardButton(text='⬅️', callback_data='case_1_animation')
                ],
                [
                    InlineKeyboardButton(text=f'Открыть за 🎟({ticket})',
                                         callback_data=f'case_three_ticket_{variable.case_3_change_increment}')
                ],
                [
                    InlineKeyboardButton(text=f'Открыть за {variable.case_3_bet}₽',
                                         callback_data=f'case_three_money_{variable.case_3_change_increment}')
                ],
                [
                    InlineKeyboardButton(text='« Назад', callback_data='cases_back')
                ]
            ]
        )
    return keyboard