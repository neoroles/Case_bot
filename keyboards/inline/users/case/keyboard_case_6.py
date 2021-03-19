from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def key_case_six_game(ticket):
    from data import variable
    if ticket <= 0:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=f'Открыть за {variable.case_6_bet}₽',
                                         callback_data=f'case_six_money_{variable.case_6_change_increment}')
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
                                         callback_data=f'case_six_ticket_{variable.case_6_change_increment}')
                ],
                [
                    InlineKeyboardButton(text=f'Открыть за {variable.case_6_bet}₽',
                                         callback_data=f'case_six_money_{variable.case_6_change_increment}')
                ],
                [
                    InlineKeyboardButton(text='« Назад', callback_data='cases_back')
                ]
            ]
        )
    return keyboard


def key_case_6_win(x, ticket):
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
                    InlineKeyboardButton(text=f'Открыть за {variable.case_6_bet}₽',
                                         callback_data=f'case_six_money_{variable.case_6_change_increment}')
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
                                         callback_data=f'case_six_ticket_{variable.case_6_change_increment}')
                ],
                [
                    InlineKeyboardButton(text=f'Открыть за {variable.case_6_bet}₽',
                                         callback_data=f'case_six_money_{variable.case_6_change_increment}')
                ],
                [
                    InlineKeyboardButton(text='« Назад', callback_data='cases_back')
                ]
            ]
        )
    return keyboard