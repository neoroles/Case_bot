import asyncio
import asyncpg

from data import config


class Database:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncio.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                database='testdb',
                user=config.PGUSER,
                password=config.PGPASSWORD,
                host=config.ip
            )
        )

# ГЛАВНАЯ ТАБЛИЦА
    async def create_main_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS main (
        user_id BIGINT NOT NULL,
        full_name VARCHAR(255),
        username VARCHAR(255),
        status VARCHAR(255),
        ref_id BIGINT,
        col_ref SMALLINT,
        conf_ref SMALLINT,
        ref_percent SMALLINT,
        ban_bot SMALLINT,
        data_reg DATE,
        data_active TIMESTAMP,
        balance BIGINT,
        up_sum BIGINT,
        down_sum BIGINT,
        key INTEGER,
        col_key INTEGER,
        ticket_1 SMALLINT,
        ticket_2 SMALLINT,
        ticket_3 SMALLINT,
        ticket_4 SMALLINT,
        ticket_5 SMALLINT,
        ticket_6 SMALLINT,
        case_1 SMALLINT,
        case_2 SMALLINT,
        case_3 SMALLINT,
        case_4 SMALLINT,
        case_5 SMALLINT,
        case_6 SMALLINT,
        case_all INTEGER,
        nv_cof INTEGER,
        nv_ver SMALLINT,
        nv_bet BIGINT,
        nv_min INTEGER,
        nv_max INTEGER,
        nv_user_min INTEGER,
        nv_user_max INTEGER,
        nv_all_game INTEGER,
        nv_all_win INTEGER,
        lottery_bet INTEGER,
        lottery_answer SMALLINT,
        lottery_win SMALLINT,
        lottery_col_win SMALLINT,
        get_free SMALLINT,
        get_1 VARCHAR,
        get_2 VARCHAR,
        get_3 VARCHAR,
        get_4 VARCHAR,
        get_5 VARCHAR,
        data_free TIMESTAMP,
        get_free_all SMALLINT,
        drawing SMALLINT,
        drawing_on_speed SMALLINT,
        drawing_on_random SMALLINT,
        drawing_all SMALLINT,
        max_win BIGINT,
        par_max_win VARCHAR,
        data_up_win TIMESTAMP,
        PRIMARY KEY (user_id))'''
        await self.pool.execute(sql)

# ЗАПИСЬ ЮЗЕРА ПРИ РЕГИСТРАЦИИ
    async def write_user(self, user_id: int, full_name: str, username: str, ref_id: int):
        sql = '''INSERT INTO main (user_id, full_name, username, status,
        ref_id, col_ref, conf_ref, ref_percent, ban_bot, data_reg, data_active, 
        balance, up_sum, down_sum, key, col_key, ticket_1,
        ticket_2, ticket_3, ticket_4, ticket_5, ticket_6,
        case_1, case_2, case_3, case_4, case_5, case_6,
        case_all, nv_cof, nv_ver, nv_bet, nv_min, nv_max, 
        nv_user_min, nv_user_max, nv_all_game, nv_all_win, 
        lottery_bet, lottery_answer, lottery_win, lottery_col_win,
        get_free, get_1, get_2, get_3, get_4, get_5, data_free, get_free_all, 
        drawing, drawing_on_speed, drawing_on_random, drawing_all, max_win, par_max_win, data_up_win) 
        VALUES ($1, $2, $3, \'user\', $4, 0, 0, 0, 0, CURRENT_DATE, CURRENT_TIMESTAMP(0), 
        10000000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10526, 95, 100000, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 3, \'\', \'\', \'\', \'\', \'\', CURRENT_TIMESTAMP(0), 0, 0, 
        0, 0, 0, 0, \'\', CURRENT_TIMESTAMP(0))'''
        await self.pool.execute(sql, user_id, full_name, username, ref_id)

# ПРОВЕРКА РЕГИСТРАЦИИ
    async def select_user(self, user_id):
        sql = f'SELECT user_id FROM main WHERE user_id={user_id} LIMIT 1'
        return True if await self.pool.fetchval(sql) is None else False

# БЛОКИРОВКА И РАЗБЛОКИРОВКА ЮЗЕРОВ
    async def up_ban(self, user_id: int, ban: int):
        sql = f'UPDATE main SET ban_bot={ban} WHERE user_id={user_id}'
        await self.pool.execute(sql)

# ВСЕ ДАННЫЕ ПРОФИЛЯ ПОЛУЧАЕМ ЗДЕСЬ
    async def select_user_profile(self, user_id: int):
        sql = f'''SELECT user_id, full_name, username, col_ref, data_reg, balance, key, col_key, case_1, case_2, case_3,
case_4, case_5, case_6, case_all, nv_all_game, nv_all_win, lottery_win, lottery_col_win, get_free_all, drawing_all, 
max_win, par_max_win FROM main WHERE user_id={user_id} LIMIT 1'''
        return await self.pool.fetchrow(sql)

# ВСЕ ДАННЫЕ ПРИГЛАШЕНИЙ ПОЛУЧАЕМ ЗДЕСЬ
    async def select_invite_stat(self, user_id: int):
        sql = f'''SELECT status, col_ref, conf_ref, ref_percent FROM main WHERE user_id = {user_id}'''
        return await self.pool.fetchrow(sql)

# ПОЛУЧАЕМ ТОЛЬКО БИЛЕТ
    async def select_ticket_case(self, user_id: int, x: int):
        sql = f'SELECT ticket_{x} FROM main WHERE user_id={user_id} LIMIT 1'
        return await self.pool.fetchval(sql)

# ПОЛУЧАЕМ НУЖНЫЙ БИЛЕТ ОТ ПОЛЬЗОВАТЕЛЯ А ТАК ЖЕ ДАТУ И ВРЕМЯ АПДЕЙТА ВЫИГРЫША
    async def select_ticket_user(self, user_id: int, x: int):
        sql = f'SELECT ticket_{x}, max_win, data_up_win FROM main WHERE user_id={user_id} LIMIT 1'
        return await self.pool.fetchrow(sql)

# ПОЛУЧАЕМ НУЖНЫЙ БИЛЕТ И БАЛАНС ОТ ПОЛЬЗОВАТЕЛЯ А ТАК ЖЕ ДАТУ И ВРЕМЯ АПДЕЙТА ВЫИГРЫША
    async def select_balance_and_ticked_user(self, user_id: int, x: int):
        sql = f'SELECT balance, ticket_{x}, max_win, data_up_win FROM main WHERE user_id={user_id} LIMIT 1'
        return await self.pool.fetchrow(sql)

# ОТКРЫЛ КЕЙС --- СМЕНА БАЛАНСА
    async def update_case_balance(self, user_id: int, balance: int, x: int):
        sql = f'''UPDATE main SET data_active=CURRENT_TIMESTAMP(0), balance = balance + {balance}, case_{x}=case_{x}+1, 
case_all=case_all+1  WHERE user_id={user_id}'''
        await self.pool.execute(sql)

# ОТКРЫЛ КЕЙС --- СМЕНА БАЛАНСА БИЛЕТОВ И МАКС ВЫИГРЫША
    async def update_case_win_user(self, user_id: int, balance: int, x: int, y: int, par: str):
        sql = f'''UPDATE main SET data_active=CURRENT_TIMESTAMP(0), balance = balance + {balance}, case_{x}=case_{x}+1, 
case_all=case_all+1, max_win={y}, par_max_win=\'{par}\', data_up_win=CURRENT_TIMESTAMP(0) WHERE user_id={user_id}'''
        await self.pool.execute(sql)

# ОТКРЫЛ КЕЙС --- СМЕНА БАЛАНСА И БИЛЕТОВ
    async def update_case_balance_and_ticket(self, user_id: int, x: int, balance: int):
        sql = f'''UPDATE main SET data_active=CURRENT_TIMESTAMP(0), balance=balance+{balance}, ticket_{x}=ticket_{x}-1,
case_{x}=case_{x}+1, case_all=case_all+1 WHERE user_id={user_id}'''
        await self.pool.execute(sql)

# ОТКРЫЛ КЕЙС --- СМЕНА БАЛАНСА И БИЛЕТОВ И МАКС ВЫИГРЫША
    async def update_case_win_balance_and_ticket(self, user_id: int, x: int, balance: int, y: int, par: str):
        sql = f'''UPDATE main SET data_active=CURRENT_TIMESTAMP(0), balance=balance+{balance}, ticket_{x}=ticket_{x}-1,
case_{x}=case_{x}+1, case_all=case_all+1, max_win={y}, par_max_win=\'{par}\', 
data_up_win=CURRENT_TIMESTAMP(0) WHERE user_id={user_id}'''
        await self.pool.execute(sql)

# ПОЛУЧАЕМ КЛЮЧИ ПОЛЬЗОВАТЕЛЯ
    async def select_key_user(self, user_id: int):
        sql = f'SELECT key FROM main WHERE user_id={user_id} LIMIT 1'
        return await self.pool.fetchval(sql)

# ОТКРЫЛ КЕЙС --- КЛЮЧИ --- ПОПОЛНИТЬ БИЛЕТЫ
    async def update_case_ticket(self, user_id: int, x: int):
        sql = f'''UPDATE main SET data_active=CURRENT_TIMESTAMP(0), key=key-1, col_key=col_key+1, 
ticket_{x}=ticket_{x}+1, case_all=case_all+1 WHERE user_id={user_id}'''
        await self.pool.execute(sql)

# РЕФЕРАЛКА --- ПОЛУЧАЕМ ЧИСЛО РЕФЕРАЛОВ
    async def select_col_ref(self, user_id: int):
        sql = f'SELECT col_ref FROM main WHERE user_id={user_id} LIMIT 1'
        return await self.pool.fetchval(sql)

# РЕФЕРАЛКА --- БОНУСЫ
    async def update_col_ref(self, user_id: int, x: int):
        sql = f'UPDATE main SET col_ref=col_ref+1, key=key+{x} WHERE user_id={user_id}'
        await self.pool.execute(sql)

# ЕЖЕДНЕВНЫЙ БОНУС --- ПОЛУЧАЕМ ДАТУ И КОЛ-ВО ПОПЫТОК
    async def select_get_free(self, user_id: int):
        sql = f'''SELECT get_free, get_1, get_2, get_3, data_free, get_4, get_5, col_ref FROM 
main WHERE user_id={user_id} LIMIT 1'''
        return await self.pool.fetchrow(sql)

# ЕЖЕДНЕВНЫЙ БОНУС --- МЕНЯЕМ ДАТУ И ЧИСЛО БОНУСОВ
    async def update_data_get_free(self, user_id: int, x: str):
        sql = f'''UPDATE main SET data_active=CURRENT_TIMESTAMP(0), get_free=get_free-1, get_1=$1,  
data_free=CURRENT_TIMESTAMP(0), get_free_all=get_free_all+1 WHERE user_id={user_id}'''
        await self.pool.execute(sql, x)

# ЕЖЕДНЕВНЫЙ БОНУС --- МЕНЯЕМ ЧИСЛО БОНУСОВ
    async def update_get_free(self, user_id: int, x: str, z: int):
        sql = f'''UPDATE main SET data_active=CURRENT_TIMESTAMP(0), get_free=get_free-1, get_{z}=$1, 
get_free_all=get_free_all+1 WHERE user_id={user_id}'''
        await self.pool.execute(sql, x)

# ЕЖЕДНЕВНЫЙ БОНУС --- ОБНУЛЯЕМ БОНУСЫ
    async def update_get_free_start(self, user_id: int , x: int):
        sql = f'''UPDATE main SET data_active=CURRENT_TIMESTAMP(0), get_free={x}, get_1=\'\', 
get_2=\'\', get_3=\'\', get_4=\'\', get_5=\'\' WHERE user_id={user_id}'''
        await self.pool.execute(sql)

# ЕЖЕДНЕВНЫЙ БОНУС --- ОБНУЛЯЕМ БОНУСЫ И АКТИВИРУЕМ ОДИН
    async def update_get_free_start_next(self, user_id: int, x: str, attempts: int):
        sql = f'''UPDATE main SET data_active=CURRENT_TIMESTAMP(0), get_free={attempts}-1, get_1=$1, 
get_2=\'\', get_3=\'\', get_4=\'\', get_5=\'\', data_free=CURRENT_TIMESTAMP(0),
get_free_all=get_free_all+1 WHERE user_id={user_id}'''
        await self.pool.execute(sql, x)

# ЕЖЕДНЕВНЫЙ БОНУС --- ПОПОЛНЯЕМ КЛЮЧИ
    async def up_key_user_id(self, user_id: int):
        sql = f'UPDATE main SET key=key+1 WHERE user_id={user_id}'
        await self.pool.execute(sql)

# ЕЖЕДНЕВНЫЙ БОНУС --- ПОПОЛНЯЕМ БАЛАНС
    async def up_balance_user_id(self, user_id: int, x: int):
        sql = f'UPDATE main SET balance=balance+{x} WHERE user_id={user_id}'
        await self.pool.execute(sql)

# РАЗБЛОКИРОВКА БОТА
    async def unban_user(self, user_id: int, name: str, username: str):
        sql = f'''UPDATE main SET full_name=\'{name}\', username=\'{username}\', ban_bot=0,
data_active=CURRENT_TIMESTAMP(0) WHERE user_id={user_id}'''
        await self.pool.execute(sql)

# БЛОКИРОВКА БОТА
    async def ban_user(self, user_id: int):
        sql = f'UPDATE main SET ban_bot=1 WHERE user_id={user_id}'
        await self.pool.execute(sql)

# ЛОТЕРЕЯ И ВСЕ ЗАПРОСЫ СВЯЗАННЫЕ С ЛОТЕРЕЕЙ
#
# ЛОТЕРЕЯ --- ПРОВЕРКА НА ТО ЧТО УЖЕ УЧАСТВУЕТ
    async def select_lottery_user(self, user_id: int):
        sql = f'SELECT lottery_bet, lottery_answer FROM main WHERE user_id={user_id} LIMIT 1'
        return await self.pool.fetchrow(sql)

# ЛОТЕРЕЯ --- ПРОВЕРКА НА ТО ЧТО УЖЕ УЧАСТВУЕТ И НА ТО, ЧТО БАЛАНС БОЛЬШЕ И РАВЕН 1
    async def select_lottery_and_balance_user(self, user_id: int):
        sql = f'SELECT balance, lottery_bet, lottery_answer FROM main WHERE user_id={user_id} LIMIT 1'
        return await self.pool.fetchrow(sql)

# ЛОТЕРЕЯ --- ПРИЕМ СТАВКИ
    async def update_lottery_user(self, user_id: int, bal: int, x: int, y: int):
        sql = f'''UPDATE main SET data_active=CURRENT_TIMESTAMP(0), balance=balance-{bal},
lottery_bet={x}, lottery_answer={y} WHERE user_id={user_id}'''
        await self.pool.execute(sql)

# NVUTI И ВСЕ ЗАПРОСЫ СВЯЗАННЫЕ С НИМ
#
# NVUTI --- ПОЛУЧЕНИЕ ВЕРОЯТНОСТИ, КОЭФФИЦЕНТОВ
    async def select_nvuti(self, user_id: int):
        sql = f'SELECT balance, nv_cof, nv_ver, nv_bet FROM main WHERE user_id={user_id} LIMIT 1'
        return await self.pool.fetchrow(sql)

# NVUTI --- СМЕНА СТАВКИ --- ПОЛУЧЕНИЕ БАЛАНСА И СТАВКИ
    async def select_nvuti_change_bet(self, user_id: int):
        sql = f'SELECT balance, nv_bet FROM main WHERE user_id={user_id} LIMIT 1'
        return await self.pool.fetchrow(sql)

# NVUTI --- СМЕНА СТАВКИ --- ИЗМЕНЕНИЕ СТАВКИ НА МАКСИМУМ
    async def update_nv_max_bet(self, user_id: int):
        sql = f'UPDATE main SET data_active=CURRENT_TIMESTAMP(0), nv_bet=balance WHERE user_id={user_id}'
        await self.pool.execute(sql)

# NVUTI --- СМЕНА СТАВКИ --- ИЗМЕНЕНИЕ СТАВКИ НА МИНИМУМ
    async def update_nv_min_bet(self, user_id: int):
        sql = f'UPDATE main SET data_active=CURRENT_TIMESTAMP(0), nv_bet=100000 WHERE user_id={user_id}'
        await self.pool.execute(sql)

# NVUTI --- СМЕНА СТАВКИ --- УДВОИТЬ
    async def update_nv_2x_bet(self, user_id: int):
        sql = f'UPDATE main SET data_active=CURRENT_TIMESTAMP(0), nv_bet=nv_bet*2 WHERE user_id={user_id}'
        await self.pool.execute(sql)

# NVUTI --- СМЕНА СТАВКИ --- ПОЛОВИНА
    async def update_nv_05x_bet(self, user_id: int):
        sql = f'UPDATE main SET data_active=CURRENT_TIMESTAMP(0), nv_bet=nv_bet/2 WHERE user_id={user_id}'
        await self.pool.execute(sql)

# NVUTI --- СМЕНА СТАВКИ --- ВРУЧНУЮ
    async def update_nv_input_bet(self, user_id: int, x: int):
        sql = f'UPDATE main SET data_active=CURRENT_TIMESTAMP(0), nv_bet={x} WHERE user_id={user_id}'
        await self.pool.execute(sql)

# NVUTI --- СМЕНА ВЕРОЯТНОСТИ --- ПОЛУЧЕНИЕ КОЭФФИЦЕНТА И ВЕРОЯТНОСТИ
    async def select_nv_change_ver(self, user_id: int):
        sql = f'SELECT nv_cof, nv_ver, nv_bet FROM main WHERE user_id={user_id} LIMIT 1'
        return await self.pool.fetchrow(sql)

# NVUTI --- СМЕНА ВЕРОЯТНОСТИ --- ИЗМЕНЕНИЕ НА МАКСИМУМ
    async def update_nv_max_ver(self, user_id: int):
        sql = f'UPDATE main SET data_active=CURRENT_TIMESTAMP(0), nv_cof=10526, nv_ver=95 WHERE user_id={user_id}'
        await self.pool.execute(sql)

# NVUTI --- СМЕНА ВЕРОЯТНОСТИ --- ИЗМЕНЕНИЕ НА МИНИМУМ
    async def update_nv_min_ver(self, user_id: int):
        sql = f'UPDATE main SET data_active=CURRENT_TIMESTAMP(0), nv_cof=1000000, nv_ver=1 WHERE user_id={user_id}'
        await self.pool.execute(sql)

# NVUTI --- СМЕНА ВЕРОЯТНОСТИ --- ПОЛУЧЕНИЕ КОЭФИЦЕНТОВ ИЗ КОНСТАНТ
    async def select_nv_constant(self, ver: int):
        sql = f'SELECT co_ef FROM const_nv WHERE id={ver} LIMIT 1'
        return await self.pool.fetchval(sql)

# NVUTI --- СМЕНА ВЕРОЯТНОСТИ --- ИЗМЕНЕНИЕ
    async def update_nv_ver(self, user_id: int, ver: int, co_ef: int):
        sql = f'''UPDATE main SET data_active=CURRENT_TIMESTAMP(0), nv_cof={co_ef}, nv_ver={ver} 
WHERE user_id={user_id}'''
        await self.pool.execute(sql)

# NVUTI --- СМЕНА ВЕРОЯТНОСТИ --- ИЗМЕНЕНИЕ
    async def select_nv_bet(self, user_id: int):
        sql = f'SELECT nv_bet FROM main WHERE user_id={user_id} LIMIT 1'
        return await self.pool.fetchval(sql)

# NVUTI --- ИГРА --- ПОЛУЧАЕМ СТАВКУ, БАЛАНС, ВЕРОЯТНОСТЬ, КОЭФФИЦЕНТ
    async def select_nv_game_const(self, user_id: int):
        sql = f'''SELECT balance, nv_cof, nv_ver, nv_bet, nv_min, nv_max, nv_user_min, nv_user_max,
max_win, data_up_win FROM main WHERE user_id={user_id} LIMIT 1'''
        return await self.pool.fetchrow(sql)

# NVUTI --- ИГРА --- ИЗМЕНЕНИЕ КОНСТАНТОВ
    async def update_nv_const(self, user_id: int, nv_min: int, nv_user_min: int, nv_max: int, nv_user_max: int):
        sql = f'''UPDATE main SET data_active=CURRENT_TIMESTAMP(0), nv_min={nv_min}, nv_max={nv_max}, 
nv_user_min={nv_user_min}, nv_user_max={nv_user_max} WHERE user_id={user_id}'''
        await self.pool.execute(sql)

# NVUTI --- ИГРА --- ЗАПИСЬ ВСЕГО
    async def update_after_nvuti_max_win(self, user_id: int, x: int, max_win: int, par: str, nv_min: int,
                                         nv_user_min: int, nv_max: int, nv_user_max: int):
        sql = f'''UPDATE main SET data_active=CURRENT_TIMESTAMP(0), balance=balance+{x}, nv_min={nv_min}, 
nv_max={nv_max}, nv_user_min={nv_user_min}, nv_user_max={nv_user_max}, nv_all_game=nv_all_game+1, 
nv_all_win=nv_all_win+{max_win}, max_win={max_win}, par_max_win=\'{par}\', data_up_win=CURRENT_TIMESTAMP(0) 
WHERE user_id={user_id}'''
        await self.pool.execute(sql)

# NVUTI --- ИГРА --- ЗАПИСЬ ВСЕГО
    async def update_after_nvuti(self, user_id: int, x: int, nv_min: int, nv_user_min: int,
                                 nv_max: int, nv_user_max: int, max_win: int):
        sql = f'''UPDATE main SET data_active=CURRENT_TIMESTAMP(0), balance=balance+{x}, nv_min={nv_min}, 
nv_max={nv_max}, nv_user_min={nv_user_min}, nv_user_max={nv_user_max}, nv_all_game=nv_all_game+1, 
nv_all_win=nv_all_win+{max_win} WHERE user_id={user_id}'''
        await self.pool.execute(sql)

# NVUTI --- ИГРА --- ЗАПИСЬ ВСЕГО
    async def update_game_nvuti_lose_max_win(self, user_id: int, x: int, max_win: int, par: str):
        sql = f'''UPDATE main SET data_active=CURRENT_TIMESTAMP(0), balance=balance+{x}, nv_all_game=nv_all_game+1, 
nv_all_win=nv_all_win+{max_win}, max_win={max_win}, par_max_win=\'{par}\', data_up_win=CURRENT_TIMESTAMP(0) 
WHERE user_id={user_id}'''
        await self.pool.execute(sql)

# NVUTI --- ИГРА --- ЗАПИСЬ ВСЕГО
    async def update_game_nvuti_lose(self, user_id: int, x: int, max_win: int):
        sql = f'''UPDATE main SET data_active=CURRENT_TIMESTAMP(0), balance=balance+{x}, nv_all_game=nv_all_game+1, 
nv_all_win=nv_all_win+{max_win} WHERE user_id={user_id}'''
        await self.pool.execute(sql)

# БАЛАНС --- Смена сообщения
    async def select_balance_user(self, user_id):
        sql = f'''SELECT balance, key, ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6 FROM main 
WHERE user_id={user_id}'''
        return await self.pool.fetchrow(sql)

# СТАТИСТИКА --- Топ по выигрышу за сутки
    async def select_stat_top_win(self):
        sql = f'''SELECT full_name, username, max_win, par_max_win FROM main WHERE data_up_win>
CURRENT_TIMESTAMP - interval \'1 days\' ORDER BY max_win DESC LIMIT 6'''
        return await self.pool.fetch(sql)

# СТАТИСТИКА --- Топ по балансу
    async def select_stat_top_bal(self):
        sql = f'''SELECT full_name, username, balance FROM main ORDER BY balance DESC LIMIT 3'''
        return await self.pool.fetch(sql)

# СТАТИСТИКА --- Топ по кейсам
    async def select_stat_top_case_all(self):
        sql = f'''SELECT full_name, username, case_all FROM main ORDER BY case_all DESC LIMIT 3'''
        return await self.pool.fetch(sql)

# СТАТИСТИКА --- Топ по кейсам
    async def select_stat_top_up_sum(self):
        sql = f'''SELECT full_name, username, up_sum FROM main ORDER BY up_sum DESC LIMIT 3'''
        return await self.pool.fetch(sql)

# СТАТИСТИКА --- Топ по ключам
    async def select_stat_top_key(self):
        sql = f'''SELECT full_name, username, key FROM main ORDER BY key DESC LIMIT 3'''
        return await self.pool.fetch(sql)

# СТАТИСТИКА --- Топ по ключам
    async def select_stat_top_friend(self):
        sql = f'''SELECT full_name, username, col_ref FROM main WHERE status=\'user\' ORDER BY col_ref DESC LIMIT 3'''
        return await self.pool.fetch(sql)

# СТАТИСТИКА --- Топ по кол-ву ежедневных бонусов
    async def select_stat_top_get_free(self):
        sql = f'''SELECT full_name, username, get_free_all FROM main ORDER BY get_free_all DESC LIMIT 3'''
        return await self.pool.fetch(sql)

    '''баланс и зависимости от баланса
-----------------------------------------------------------------------------------------------------------------------  
    Создание таблицы
    Начальная запись
    Изменение на каждый запрос
-----------------------------------------------------------------------------------------------------------------------
    '''
    async def create_balance(self):
        sql = '''CREATE TABLE IF NOT EXISTS bal (
        id SMALLINT NOT NULL,
        balance_all BIGINT,
        balance_bot BIGINT,
        PRIMARY KEY (id))'''
        await self.pool.execute(sql)

    async def write_balance(self):
        sql = '''INSERT INTO bal (id, balance_all, balance_bot) VALUES (1, 0, 0)'''
        await self.pool.execute(sql)

    async def update_balance(self, balance_all: int, balance_bot: int):
        sql = f'''UPDATE bal SET balance_all=balance_all+{balance_all}, balance_bot=balance_bot+{balance_bot}'''
        await self.pool.execute(sql)

    async def select_balance(self):
        sql = '''SELECT balance_all, balance_bot FROM bal'''
        return await self.pool.fetchrow(sql)

    '''
    ---------------------------------------------------------------------------------------------------------------  
    
    ---------------------------------------------------------------------------------------------------------------
    
    '''
# СТАТИСТИКА ПОЛЬЗОВАТЕЛЬСКАЯ --- ТОП ПО БАЛАНСУ
    async def stat_top_balance(self):
        sql = '''SELECT full_name, balance FROM main ORDER BY balance DESC LIMIT 3'''
        return await self.pool.fetch(sql)

    '''
    ---------------------------------------------------------------------------------------------------------------  
    АДМИНСКАЯ ЧАСТЬ БАЗЫ ДАННЫХ И ЗАПРОСОВ
    ---------------------------------------------------------------------------------------------------------------
    
    '''
    async def stat_lottery(self, x: int):
        sql = f'''SELECT SUM(lottery_bet), COUNT(lottery_answer) FROM main WHERE lottery_answer = {x}'''
        return await self.pool.fetchrow(sql)

    async def stat_all_bets_lottery(self):
        sql = '''SELECT COUNT(lottery_answer) FROM main WHERE lottery_answer != 0'''
        return await self.pool.fetchval(sql)

    async def users_lottery_active(self, x: int):
        sql = f'''SELECT user_id, lottery_bet FROM main WHERE lottery_answer = {x}'''
        return await self.pool.fetch(sql)

    async def lottery_discharge(self):
        sql = '''UPDATE main SET lottery_answer = 0, lottery_bet = 0'''
        await self.pool.execute(sql)

    async def up_balance_lottery(self, user_id: int, balance: int, x: int):
        sql = f'''UPDATE main SET balance=balance+{balance}, lottery_win={x}, lottery_col_win=lottery_col_win+1 
WHERE user_id={user_id}'''
        await self.pool.execute(sql)

#

    async def up_balance(self, user_id: int, balance: int):
        sql = f'UPDATE main SET balance=balance+{balance}, up_sum=up_sum+{balance} WHERE user_id={user_id}'
        await self.pool.execute(sql)

    async def up_key(self, user_id: int, key: int):
        sql = f'''UPDATE main SET key=key+{key} WHERE user_id={user_id}'''
        await self.pool.execute(sql)

    '''
    ---------------------------------------------------------------------------------------------------------------  
    ТАБЛИЦА НВУТИ --- ВЕРОЯТНОСТИ И КОЭФФИЦЕНТЫ
    ---------------------------------------------------------------------------------------------------------------

    '''
# Таблица коэффицентов нвути
    async def create_table_nv_const(self):
        sql = '''CREATE TABLE IF NOT EXISTS const_nv (
        id SMALLINT NOT NULL,
        co_ef INTEGER NOT NULL,
        PRIMARY KEY (id))
        '''
        await self.pool.execute(sql)

    async def write_nv_const(self):
        sql = '''INSERT INTO const_nv (id, co_ef) VALUES (1, 1000000), (2, 500000), (3, 333333), (4, 250000),
        (5, 200000), (6, 166667), (7, 142857), (8, 125000), (9, 111111), (10, 100000), (11, 90909), (12, 83333),
        (13, 76923), (14, 71429), (15, 66667), (16, 62500), (17, 58824), (18, 55556), (19, 52632), (20, 50000),
        (21, 47619), (22, 45455), (23, 43478), (24, 41667), (25, 40000), (26, 38462), (27, 37037), (28, 35714),
        (29, 34483), (30, 33333), (31, 32258), (32, 31250), (33, 30303), (34, 29412), (35, 28571), (36, 27778),
        (37, 27027), (38, 26316), (39, 25641), (40, 25000), (41, 24390), (42, 23810), (43, 23256), (44, 22727),
        (45, 22222), (46, 21739), (47, 21277), (48, 20833), (49, 20408), (50, 20000), (51, 19608), (52, 19231),
        (53, 18868), (54, 18519), (55, 18182), (56, 17857), (57, 17544), (58, 17241), (59, 16949), (60, 16667),
        (61, 16393), (62, 16129), (63, 15873), (64, 15625), (65, 15385), (66, 15152), (67, 14925), (68, 14706),
        (69, 14493), (70, 14286), (71, 14085), (72, 13889), (73, 13699), (74, 13514), (75, 13333), (76, 13158),
        (77, 12987), (78, 12821), (79, 12658), (80, 12500), (81, 12346), (82, 12195), (83, 12048), (84, 11905),
        (85, 11765), (86, 11628), (87, 11494), (88, 11364), (89, 11236), (90, 11111), (91, 10989), (92, 10870),
        (93, 10753), (94, 10638), (95, 10526)'''
        await self.pool.execute(sql)

    '''
    ---------------------------------------------------------------------------------------------------------------  
    ТАБЛИЦА КЕЙСОВ --- ВСЕ КОНСТАНТЫ
    создание
    запись при запуске
    изменение
    ---------------------------------------------------------------------------------------------------------------

    '''
# ТАБЛИЦА КЕЙСОВ И КОНСТАНТЫ КЕЙСОВ
    async def create_table_const_case(self):
        sql = '''CREATE TABLE IF NOT EXISTS case_const (
        id SMALLINT NOT NULL,
        name VARCHAR(255) NOT NULL,
        photo_id VARCHAR(255) NOT NULL,
        caption VARCHAR(1023) NOT NULL,
        bet INTEGER NOT NULL,
        cost INTEGER NOT NULL,
        PRIMARY KEY (id))'''
        await self.pool.execute(sql)

    async def write_case(self):
        sql = 'INSERT INTO case_const (id, name, photo_id, caption, bet, cost) VALUES (1, \'\', \'\', \'\', 1, 1),' \
              '(2, \'\', \'\', \'\', 1, 1),' \
              '(3, \'\', \'\', \'\', 1, 1),' \
              '(4, \'\', \'\', \'\', 1, 1),' \
              '(5, \'\', \'\', \'\', 1, 1),' \
              '(6, \'\', \'\', \'\', 1, 1),' \
              '(7, \'\', \'\', \'\', 1, 1)'
        await self.pool.execute(sql)

    async def update_case(self, name: str, photo: str, caption: str, bet: int, cost: int, case: int):
        sql = f'''UPDATE case_const SET name=\'{name}\', photo_id=\'{photo}\', caption=\'{caption}\', bet={bet}, 
cost={cost} WHERE id={case}'''
        await self.pool.execute(sql)

    async def select_case_const(self, x: int):
        sql = f'''SELECT name, photo_id, caption, bet, cost FROM case_const WHERE id={x}'''
        return await self.pool.fetchrow(sql)

    '''
    ---------------------------------------------------------------------------------------------------------------  

    ---------------------------------------------------------------------------------------------------------------

    '''
# ТАБЛИЦА КОНСТАНТ
    async def create_table_const(self):
        sql = '''CREATE TABLE IF NOT EXISTS constants (
        id SMALLINT,
        win_percent SMALLINT,
        c_block_1 SMALLINT,
        c_block_2 SMALLINT,
        c_block_3 SMALLINT,
        nv_winner BIGINT,
        case_1_winner BIGINT,
        case_2_winner BIGINT,
        case_3_winner BIGINT,
        case_4_winner BIGINT,
        case_5_winner BIGINT,
        case_6_winner BIGINT,
        case_7_winner BIGINT,        
        PRIMARY KEY (id))'''
        await self.pool.execute(sql)

    async def write_const(self):
        sql = '''INSERT INTO constants (id, win_percent, c_block_1, c_block_2, c_block_3, nv_winner, case_1_winner, 
case_2_winner, case_3_winner, case_4_winner, case_5_winner, case_6_winner, case_7_winner) 
VALUES (1, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)'''
        await self.pool.execute(sql)

    async def select_const(self):
        sql = '''SELECT win_percent, c_block_1, c_block_2, c_block_3, nv_winner, case_1_winner, case_2_winner, 
case_3_winner, case_4_winner, case_5_winner, case_6_winner, case_7_winner FROM constants'''
        return await self.pool.fetchrow(sql)

    async def update_win_percent(self, x: int):
        sql = f'''UPDATE constants SET win_percent={x}'''
        await self.pool.execute(sql)

    async def update_block_part(self, x: int, y: int):
        sql = f'''UPDATE constants SET c_block_{x}={y}'''
        await self.pool.execute(sql)
