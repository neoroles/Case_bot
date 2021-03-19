from aiogram.types import CallbackQuery

from keyboards.inline.users.keyboard_invite import key_invite
from loader import dp, bot, db


@dp.callback_query_handler(text='invite')
async def invite(call: CallbackQuery):
    await call.answer()
    data = await db.select_invite_stat(call.message.chat.id)
    if data[0] == 'user':
        status = 'пользователь'
    elif data[0] == 'partner':
        status = 'партнер'
    else:
        status = data[0]
    text = f'''<b>👫 Приглашения</b>

Приглашай друзей и ты сможешь увеличить
количество ежедневных бонусов, получить 
ключи на открытие секретных кейсов, 
выделиться в таблице лидеров.

Пригласив 500 друзей, сможешь получить 
<b>статус «ТОП-друг»</b> в нашем чате.

Весь список призов вы найдете по ссылке:

<b>⚙️ Ваша реферальная ссылка для привлечения игроков:</b>
https://t.me/Case_altlook_bot?start=ref-{call.message.chat.id}

<b>👥 Рефералов:</b> {data[2]}
        <code>Незасчитанные рефералы:</code> {data[1]-data[2]}
        <code>Процент с пополнений:</code> {data[3]}
        <code>Статус:</code> <b>{status}</b>

За специальными условиями для админов, писать в лс - '''
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=key_invite(0))


@dp.callback_query_handler(text='profile:invite')
async def invite(call: CallbackQuery):
    await call.answer()
    data = await db.select_invite_stat(call.message.chat.id)
    if data[0] == 'user':
        status = 'пользователь'
    elif data[0] == 'partner':
        status = 'партнер'
    else:
        status = data[0]
    text = f'''<b>👫 Приглашения</b>

Приглашай друзей и ты сможешь увеличить
количество ежедневных бонусов, получить 
ключи на открытие секретных кейсов, 
выделиться в таблице лидеров.

Пригласив 500 друзей, сможешь получить 
<b>статус «ТОП-друг»</b> в нашем чате.

Весь список призов вы найдете по ссылке:

<b>⚙️ Ваша реферальная ссылка для привлечения игроков:</b>
https://t.me/Case_altlook_bot?start=ref-{call.message.chat.id}

<b>👥 Рефералов:</b> {data[2]}
        <code>Незасчитанные рефералы:</code> {data[1] - data[2]}
        <code>Процент с пополнений:</code> {data[3]}
        <code>Статус:</code> <b>{status}</b>

За специальными условиями для админов, писать в лс - '''
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=key_invite(1))


@dp.callback_query_handler(text='bonus:invite')
async def invite(call: CallbackQuery):
    await call.answer()
    data = await db.select_invite_stat(call.message.chat.id)
    if data[0] == 'user':
        status = 'пользователь'
    elif data[0] == 'partner':
        status = 'партнер'
    else:
        status = data[0]
    text = f'''<b>👫 Приглашения</b>

Приглашай друзей и ты сможешь увеличить
количество ежедневных бонусов, получить 
ключи на открытие секретных кейсов, 
выделиться в таблице лидеров.

Пригласив 500 друзей, сможешь получить 
<b>статус «ТОП-друг»</b> в нашем чате.

Весь список призов вы найдете по ссылке:

<b>⚙️ Ваша реферальная ссылка для привлечения игроков:</b>
https://t.me/Case_altlook_bot?start=ref-{call.message.chat.id}

<b>👥 Рефералов:</b> {data[2]}
        <code>Незасчитанные рефералы:</code> {data[1] - data[2]}
        <code>Процент с пополнений:</code> {data[3]}
        <code>Статус:</code> <b>{status}</b>

За специальными условиями для админов, писать в лс - '''
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=key_invite(2))