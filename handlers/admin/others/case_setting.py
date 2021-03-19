from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from data import config
from keyboards.inline.admins.other.misc import mod_editor_case
from keyboards.inline.users.profile.misc import key, key_del
from loader import dp, bot, db
from states.admin_state import CaseEditor


@dp.callback_query_handler(text='case_set', user_id=config.moderators)
async def case_set(call: CallbackQuery):
    await call.answer()
    text = '''<b>Редактирвание кейсов</b>

Вы можете поменять:

<b>Ставку:</b> число (чем круче кейс тем больше ставка)
<b>Стоимость:</b> число (анологично что и выше
<b>Картинку:</b> это по твоей части
<b>Описание:</b> что угодно
<b>Название:</b> что угодно'''
    await bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=mod_editor_case)


@dp.callback_query_handler(text_contains='editor_case', user_id=config.moderators)
async def choice_case(call: CallbackQuery, state: FSMContext):
    await call.answer()
    text = f'''<b>Вы редактируете кейс номер {call.data[-1]}</b>

Отправляешь фото с подписью в таком формате

<code>Название:
Ставка:
Стоимость:
Описание:</code>

Копируй пример выше 
Порядок менять нельзя

'''
    await CaseEditor.Input.set()
    await state.update_data(case=call.data[-1])
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                        message_id=call.message.message_id)
    await bot.send_message(text=text, chat_id=call.message.chat.id, reply_markup=key)


@dp.message_handler(content_types=types.ContentTypes.PHOTO, user_id=config.moderators, state=CaseEditor.Input)
async def get_image(message: Message, state: FSMContext):
    import re
    try:
        data = await state.get_data()
        case = data.get("case")
        photo = message.photo[-1].file_id
        answer = message.caption
        name_text = re.search(r'Название:', answer)
        bet_text = re.search(r'Ставка:', answer)
        cost_text = re.search(r'Стоимость:', answer)
        caption_text = re.search(r'Описание:', answer)
        name = answer[name_text.end():bet_text.start()]
        bet = int(answer[bet_text.end():cost_text.start()])
        cost = int(answer[cost_text.end():caption_text.start()])
        captions = answer[caption_text.end():]
        text = f'''<b>Приз:</b> {name}
<b>Ставка:</b> {bet}
<b>Стоимость:</b> {cost} ₽
<b>Описание:</b> {captions}'''
        await bot.send_photo(chat_id=message.chat.id,
                             photo=photo, caption=text, disable_notification=True, reply_markup=key_del)
        await db.update_case(name=name, photo=photo, caption=captions, bet=bet, cost=cost, case=case)
        from data import variable
        next_text = '''<b>Редактирвание кейсов</b>

Вы можете поменять:

<b>Ставку:</b> число (чем круче кейс тем больше ставка)
<b>Стоимость:</b> число (анологично что и выше
<b>Картинку:</b> это по твоей части
<b>Описание:</b> что угодно
<b>Название:</b> что угодно'''
        await message.answer(text=next_text, reply_markup=mod_editor_case)
        await state.finish()
        if case == 1:
            variable.case_1_change_increment = variable.case_1_change_increment + 1
        elif case == 2:
            variable.case_2_change_increment = variable.case_2_change_increment + 1
        elif case == 3:
            variable.case_3_change_increment = variable.case_3_change_increment + 1
        elif case == 4:
            variable.case_4_change_increment = variable.case_4_change_increment + 1
        elif case == 5:
            variable.case_5_change_increment = variable.case_5_change_increment + 1
        elif case == 6:
            variable.case_6_change_increment = variable.case_6_change_increment + 1
        from utils.downloader import download_cases
        await download_cases()
    except Exception as e:
        await message.answer(f'{e}')


@dp.callback_query_handler(text='edit_case_secret', user_id=config.moderators)
async def edit_case_secret(call: CallbackQuery):
    await call.answer()
    text = '''Тут можно сменить только фото'''
    await CaseEditor.Key.set()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                        message_id=call.message.message_id)
    await bot.send_message(text=text, chat_id=call.message.chat.id, reply_markup=key)


@dp.message_handler(content_types=types.ContentTypes.PHOTO, user_id=config.moderators, state=CaseEditor.Key)
async def get_secret_image(message: Message, state: FSMContext):
    photo = message.photo[-1].file_id
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo, disable_notification=True, reply_markup=key_del)
    await db.update_case(name='', photo=photo, caption='', bet=1, cost=1, case=7)
    next_text = '''<b>Редактирвание кейсов</b>

Вы можете поменять:

<b>Ставку:</b> число (чем круче кейс тем больше ставка)
<b>Стоимость:</b> число (анологично что и выше
<b>Картинку:</b> это по твоей части
<b>Описание:</b> что угодно
<b>Название:</b> что угодно'''
    await message.answer(text=next_text, reply_markup=mod_editor_case)
    await state.finish()
    from utils.downloader import download_cases
    await download_cases()


@dp.message_handler(user_id=config.moderators, state=CaseEditor)
async def back_editor(message: Message, state: FSMContext):
    if message.text == 'Отмена':
        await message.answer('Действие отменено', reply_markup=key_del)
        next_text = '''<b>Редактирвание кейсов</b>

Вы можете поменять:

<b>Ставку:</b> число (чем круче кейс тем больше ставка)
<b>Стоимость:</b> число (анологично что и выше
<b>Картинку:</b> это по твоей части
<b>Описание:</b> что угодно
<b>Название:</b> что угодно'''
        await message.answer(text=next_text, reply_markup=mod_editor_case)
        await state.finish()
    else:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)