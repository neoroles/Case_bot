from loader import db
from utils.update_balance import change_balance


async def bonus_create(user_id):
    from random import choice, choices
    # data = ['✖', '✖', '1₽', '2₽', '✖', '5₽', '1₽', '✖', '✖', '✖', '1₽', '2₽', '✖', '5₽', '1₽', '20₽', '✖', '5₽',
    #         '1₽', '2₽', '✖', '5₽', '1₽', '5₽', '✖', '🔑', '1₽', '2₽', '✖', '5₽', '1₽', '✖', '✖', '✖', '1₽',
    #         '2₽', '✖', '5₽', '1₽', '10₽', '✖', '✖', '1₽', '2₽', '✖', '5₽', '1₽', '✖', '✖', '✖']
    # x = choice(data)
    y = choices(['✖', '1₽', '2₽', '5₽', '10₽', '20₽', '🔑'], weights=[100, 100, 50, 10, 5, 3, 2], k=1)
    x = y[0]
    if x == '✖':
        return x
    elif x == '🔑':
        await db.up_key_user_id(user_id=user_id)
        return x
    elif x == '1₽':
        await db.up_balance_user_id(user_id=user_id, x=1*10000)
        await change_balance(balance_all=0, balance_bot=-1*10000)
        return x
    elif x == '2₽':
        await db.up_balance_user_id(user_id=user_id, x=2*10000)
        await change_balance(balance_all=0, balance_bot=-2*10000)
        return x
    elif x == '5₽':
        await db.up_balance_user_id(user_id=user_id, x=5*10000)
        await change_balance(balance_all=0, balance_bot=-5*10000)
        return x
    elif x == '10₽':
        await db.up_balance_user_id(user_id=user_id, x=10*10000)
        await change_balance(balance_all=0, balance_bot=-10*10000)
        return x
    elif x == '20₽':
        await db.up_balance_user_id(user_id=user_id, x=20*10000)
        await change_balance(balance_all=0, balance_bot=-20*10000)
        return x
