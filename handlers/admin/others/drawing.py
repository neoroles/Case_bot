from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from data import config, variable
from keyboards.inline.admins.other.keyboard_drawing import draw_create, create_or_active_on_speed, \
    create_back_on_speed
from loader import dp, db, bot
from states.admin_state import CreateDrawing


@dp.callback_query_handler(text='drawing', user_id=config.moderators)
async def drawing(call: CallbackQuery):
    await call.answer()
    text = '''Два вида розыгрышей

<b>На скорость</b> - Кто успел тот получил приз
<b>На рандом</b> - Набирается кол-во участников и между ними разыгрывается'''
    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=draw_create)


@dp.callback_query_handler(text='draw_on_speed', user_id=config.moderators)
async def draw_on_speed(call: CallbackQuery):
    await call.answer()
    text = '''Это розыгрыш на скорость

Кто быстрее нажмет на кнопку в сообщении на канале, тот и выиграл приз
Кол-во мест ограничено и призы выбираешь ты (смотри от зависимости в балансе)
    
'''
    if variable.save_on_speed == 0:
        text = text + '''\n<b>Сообщение не подготовлено</b>'''
    else:
        text = text + f'''\n<b>Сообщение подготовлено</b>
        
Текст сообщения: {variable.description_on_speed}
Приз: {variable.win_bal_on_speed} ₽ и/или {variable.win_key_on_speed} 🔑
Кол-во мест: {variable.quantity_on_speed}'''

    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=create_or_active_on_speed)


@dp.callback_query_handler(text='draw_on_speed', user_id=config.moderators)
async def draw_on_speed(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.finish()
    text = '''Это розыгрыш на скорость

Кто быстрее нажмет на кнопку в сообщении на канале, тот и выиграл приз
Кол-во мест ограничено и призы выбираешь ты (смотри от зависимости в балансе)

'''
    if variable.save_on_speed == 0:
        text = text + '''\n<b>Сообщение не подготовлено</b>'''
    else:
        text = text + f'''\n<b>Сообщение подготовлено</b>

Текст сообщения: {variable.description_on_speed}
Приз: {variable.win_bal_on_speed} ₽ и/или {variable.win_key_on_speed} 🔑
Кол-во мест: {variable.quantity_on_speed}'''

    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=create_or_active_on_speed)


@dp.callback_query_handler(text='create_on_speed', user_id=config.moderators)
async def create_on_speed(call: CallbackQuery):
    await call.answer()
    text = '''Пришлите все данные в формате:
    
<code>Количество участников: 
Деньги:
Ключи:
Описание:</code>
'''
    await CreateDrawing.InputOnSpeed.set()

    await bot.edit_message_text(text=text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=create_back_on_speed)


@dp.message_handler(state=CreateDrawing.InputOnSpeed, user_id=config.moderators)
async def input_on_speed(message: Message, state: FSMContext):
    import re
    try:
        answer = message.text
        quantity_text = re.search(r'Количество участников:', answer)
        win_bal_text = re.search(r'Деньги:', answer)
        win_key_text = re.search(r'Ключи:', answer)
        description_text = re.search(r'Описание:', answer)
        variable.quantity_on_speed = int(answer[quantity_text.end():win_bal_text.start()])
        variable.win_bal_on_speed = int(answer[win_bal_text.end():win_key_text.start()])
        variable.win_key_on_speed = int(answer[win_key_text.end():description_text.start()])
        variable.description_on_speed = answer[description_text.end():]
        variable.save_on_speed = 1
        text = '''Это розыгрыш на скорость

        Кто быстрее нажмет на кнопку в сообщении на канале, тот и выиграл приз
        Кол-во мест ограничено и призы выбираешь ты (смотри от зависимости в балансе)

        '''
        if variable.save_on_speed == 0:
            text = text + '''\n<b>Сообщение не подготовлено</b>'''
        else:
            text = text + f'''\n<b>Сообщение подготовлено</b>

        Текст сообщения: {variable.description_on_speed}
        Приз: {variable.win_bal_on_speed} ₽ и/или {variable.win_key_on_speed} 🔑
        Кол-во мест: {variable.quantity_on_speed}'''
        await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=create_or_active_on_speed)
        variable.enumerator_on_speed = 0
        await state.finish()
    except Exception as e:
        await message.answer(f'Ошибка\n {e}')








