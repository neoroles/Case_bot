from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def key_bonus():
    from data import config
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🎁 Ежедневный бонус', callback_data='prize')
            ],
            [
                InlineKeyboardButton(text='🌐 Наш канал', url=f'{config.link_channel}'),
                InlineKeyboardButton(text='👫 Приглашения', callback_data='bonus:invite')
            ],
            [
                InlineKeyboardButton(text='« Назад', callback_data='back_start')
            ]
        ]
    )
    return keyboard


def key_bonus_game(x: int, y: int, z: int, k: int, m: int, x_var: str, y_var: str, z_var: str, k_var: str, m_var: str):
    keyboard = InlineKeyboardMarkup(row_width=5)
    for i in range(20):
        if i + 1 == x:
            key = InlineKeyboardButton(text=f'{x_var}', callback_data='case_animation')
        elif i + 1 == y:
            key = InlineKeyboardButton(text=f'{y_var}', callback_data='case_animation')
        elif i + 1 == z:
            key = InlineKeyboardButton(text=f'{z_var}', callback_data='case_animation')
        elif i + 1 == k:
            key = InlineKeyboardButton(text=f'{k_var}', callback_data='case_animation')
        elif i + 1 == m:
            key = InlineKeyboardButton(text=f'{m_var}', callback_data='case_animation')
        else:
            key = InlineKeyboardButton(text='📦', callback_data=f'bonus_default_{i+1}')
        keyboard.insert(key)
    key_1 = InlineKeyboardButton(text='« Назад', callback_data='get_free')
    keyboard.insert(key_1)
    return keyboard
