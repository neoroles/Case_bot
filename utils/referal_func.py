from loader import db


async def update_refer(user_id: int, col_ref: int):
    if col_ref + 1 == 500:
        await db.update_col_ref(user_id=user_id, x=10)
        text = 'Ваш приз: +10🔑 и статус «ТОП-Друг» в нашем Чате'
        return text
    elif col_ref + 1 == 400:
        await db.update_col_ref(user_id=user_id, x=7)
        text = 'Ваш приз: +7🔑'
        return text
    elif col_ref + 1 == 300:
        await db.update_col_ref(user_id=user_id, x=6)
        text = 'Ваш приз: +6🔑'
        return text
    elif col_ref + 1 == 250:
        await db.update_col_ref(user_id=user_id, x=5)
        text = 'Ваш приз: +5🔑'
        return text
    elif col_ref + 1 == 200:
        await db.update_col_ref(user_id=user_id, x=5)
        text = 'Ваш приз: +5🔑'
        return text
    elif col_ref + 1 == 150:
        await db.update_col_ref(user_id=user_id, x=4)
        text = 'Ваш приз: +4🔑'
        return text
    elif col_ref + 1 == 125:
        await db.update_col_ref(user_id=user_id, x=4)
        text = 'Ваш приз: +4🔑'
        return text
    elif col_ref + 1 == 100:
        await db.update_col_ref(user_id=user_id, x=4)
        text = 'Ваш приз: +4🔑'
        return text
    elif col_ref + 1 == 90:
        await db.update_col_ref(user_id=user_id, x=3)
        text = 'Ваш приз: +3🔑'
        return text
    elif col_ref + 1 == 70:
        await db.update_col_ref(user_id=user_id, x=3)
        text = 'Ваш приз: +3🔑'
        return text
    elif col_ref + 1 == 50:
        await db.update_col_ref(user_id=user_id, x=3)
        text = 'Ваш приз: +3🔑'
        return text
    elif col_ref + 1 == 40:
        await db.update_col_ref(user_id=user_id, x=3)
        text = 'Ваш приз: +3🔑'
        return text
    elif col_ref + 1 == 30:
        await db.update_col_ref(user_id=user_id, x=3)
        text = 'Ваш приз: +3🔑'
        return text
    elif col_ref + 1 == 25:
        await db.update_col_ref(user_id=user_id, x=5)
        text = 'Ваш приз: +5🔑 и +5% с последующих пополнений друзей'
        return text
    elif col_ref + 1 == 20:
        await db.update_col_ref(user_id=user_id, x=2)
        text = 'Ваш приз: +2🔑'
        return text
    elif col_ref + 1 == 15:
        await db.update_col_ref(user_id=user_id, x=2)
        text = 'Ваш приз: +2🔑'
        return text
    elif col_ref + 1 == 10:
        await db.update_col_ref(user_id=user_id, x=2)
        text = 'Ваш приз: +2🔑'
        return text
    elif col_ref + 1 == 5:
        await db.update_col_ref(user_id=user_id, x=2)
        text = 'Ваш приз: +2🔑'
        return text
    elif col_ref + 1 == 4:
        await db.update_col_ref(user_id=user_id, x=1)
        text = 'Ваш приз: +🔑'
        return text
    elif col_ref + 1 == 3:
        await db.update_col_ref(user_id=user_id, x=1)
        text = 'Ваш приз: +🔑'
        return text
    elif col_ref + 1 == 2:
        await db.update_col_ref(user_id=user_id, x=1)
        text = 'Ваш приз: +🔑'
        return text
    elif col_ref + 1 == 1:
        await db.update_col_ref(user_id=user_id, x=1)
        text = 'Ваш приз: +🔑'
        return text
    else:
        text = ''
        return text

