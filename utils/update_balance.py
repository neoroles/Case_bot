

async def change_balance(balance_all: int, balance_bot: int):
    from loader import db
    from data import variable
    await db.update_balance(balance_all=balance_all, balance_bot=balance_bot)
    variable.balance_bot += balance_bot
    variable.balance_all += balance_all
    print(f'balance_all {variable.balance_all}')
    print(f'balance_bot {variable.balance_bot}')
