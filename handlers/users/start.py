from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, Message

from keyboards.inline.users.start_key import key_start
from loader import dp, bot, db
from utils.misc import rate_limit
from re import compile

from utils.referal_func import update_refer


@rate_limit(limit=1)
@dp.message_handler(CommandStart(deep_link=compile(r'ref-\d+')))
async def bot_start_ref(message: Message):
    username = message.from_user.username
    name = message.from_user.full_name
    if name is None:
        name = ''
    if username is None:
        username = ''
    if await db.select_user(message.chat.id):
        try:
            ref_id = int(message.get_args()[4:])
            if await db.select_user(ref_id):
                ref_id = 0
            else:
                col_ref = await db.select_col_ref(user_id=ref_id)
                answer = f'Поздравляем!\nУ вас появился новый друг:\n\nID: <code>{message.chat.id}</code>\n' \
                         f'Имя: {message.from_user.full_name}'
                data = await update_refer(user_id=ref_id, col_ref=col_ref)
                if len(data) > 1:
                    answer = answer + '\n' + data
                try:
                    await bot.send_message(chat_id=ref_id, text=answer)
                except:
                    await db.ban_user(ref_id)
        except Exception as e:
            ref_id = 0
        await db.write_user(user_id=message.chat.id, full_name=name, username=username, ref_id=ref_id)
    else:
        await db.unban_user(message.chat.id, name=name, username=username)
    text = '''💈 <b>Главное меню</b>

Здесь вы можете сыграть в игры и выиграть 💰 или приз.   
<i>Призы можно посмотреть в кейсах.</i>'''
    await message.answer(text, reply_markup=key_start)


@rate_limit(limit=1)
@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    username = message.from_user.username
    name = message.from_user.full_name
    if name is None:
        name = ''
    if username is None:
        username = ''
    if await db.select_user(message.chat.id):
        ref_id = 0
        await db.write_user(user_id=message.chat.id, full_name=name, username=username, ref_id=ref_id)
    else:
        await db.unban_user(message.chat.id, name=name, username=username)
    text = '''💈 <b>Главное меню</b>

Здесь вы можете сыграть в игры и выиграть 💰 или приз.   
<i>Призы можно посмотреть в кейсах.</i>'''
    await message.answer(text, reply_markup=key_start)


@dp.callback_query_handler(text='back_start')
async def back_start(call: CallbackQuery):
    await call.answer(cache_time=1)
    text = '''💈 <b>Главное меню</b>

Здесь вы можете сыграть в игры и выиграть 💰 или приз.   
<i>Призы можно посмотреть в кейсах.</i>'''
    await bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                text=text,
                                reply_markup=key_start)

