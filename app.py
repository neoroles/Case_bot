from utils.set_bot_commands import set_default_commands
from loader import db


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)
    await db.create_main_table()
    await db.create_table_nv_const()
    await db.create_table_const_case()
    await db.create_balance()
    await db.create_table_const()
    try:
        await db.write_balance()
    except:
        pass
    try:
        await db.write_case()
    except:
        pass
    try:
        await db.write_nv_const()
    except:
        pass
    try:
        await db.write_const()
    except:
        pass
    from utils.downloader import download_cases, download_consts
    try:
        await download_cases()
    except:
        pass
    try:
        await download_consts()
    except:
        pass
    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
