
# ВЕЗДЕ ДОБАВИТЬ ФУНКЦИЮ СМЕНЫ БАЛАНСА БОТА
from utils.update_balance import change_balance


async def case_data_one_money(user_id):
    from data import variable
    from random import choice, randint
    data = ['', '', '', '', '', '']
    bet = int(variable.case_1_bet)
    min_0 = bet // 5
    min_1 = bet // 4
    min_2 = bet // 3
    min_3 = bet // 2
    min_4 = (bet // 3) * 2
    max_0 = bet * 2
    max_1 = bet * 3 // 2
    max_2 = bet * 4 // 3
    max_3 = bet * 5 // 3
    max_4 = bet * 5
    bets = [min_0, min_1, min_2, min_3, min_4, max_0, max_1, max_2, max_3, max_4]
    if str(user_id) == str(variable.case_1_winners):
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        data[4] = '🔥'
        variable.case_1_winners = 0
        await change_balance(balance_all=0, balance_bot=(-variable.case_1_cost+variable.case_1_bet)*10000)
        return data
    if variable.balance_bot < variable.balance_all // 100 * variable.win_percent:
        print(1)
        mins = [min_0, min_1, min_2, min_3, min_4]
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        delta = 6
        while delta == 6 or delta == 4:
            delta = randint(0, 5)
        data[delta] = '🔥'
        if variable.balance_bot + (-data[4] + variable.case_1_bet)*10000 < variable.balance_all // 100 * \
                variable.win_percent:
            print(2)
            data[4] = choice(mins)
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_1_bet)*10000)
            return data
        else:
            print(3)
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_1_bet)*10000)
            return data
    else:
        print(4)
        mins = [min_0, min_1, min_2, min_3, min_4]
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        delta = 6
        while delta == 6 or delta == 4:
            delta = randint(0, 5)
        data[delta] = '🔥'
        if variable.balance_bot + (-data[4] + variable.case_1_bet)*10000 < variable.balance_all // 100 * \
                variable.win_percent:
            print(5)
            data[4] = choice(mins)
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_1_bet)*10000)
            return data
        else:
            print(6)
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_1_bet)*10000)
            return data


async def case_data_one_ticket():
    from data import variable
    from random import choice, randint
    data = ['', '', '', '', '', '']
    bet = int(variable.case_1_bet)
    min_0 = bet // 5
    min_1 = bet // 4
    min_2 = bet // 3
    min_3 = bet // 2
    min_4 = (bet // 3) * 2
    max_0 = bet * 2
    max_1 = bet * 3 // 2
    max_2 = bet * 4 // 3
    max_3 = bet * 5 // 3
    bets = [min_0, min_1, min_2, min_3, min_4, max_0, max_1, max_2, max_3]
    mins = [min_0, min_1, min_2, min_3, min_4]
    i = 0
    while i < 6:
        data[i] = choice(bets)
        i += 1
    delta = 6
    while delta == 6 or delta == 4:
        delta = randint(0, 5)
    data[delta] = '🔥'
    data[4] = choice(mins)
    await change_balance(balance_all=0, balance_bot=-data[4]*10000)
    return data


async def case_data_two_money(user_id):
    from data import variable
    from random import choice, randint
    data = ['', '', '', '', '', '']
    bet = int(variable.case_2_bet)
    min_0 = bet // 5
    min_1 = bet // 4
    min_2 = bet // 3
    min_3 = bet // 2
    min_4 = (bet // 3) * 2
    max_0 = bet * 2
    max_1 = bet * 3 // 2
    max_2 = bet * 4 // 3
    max_3 = bet * 5 // 3
    bets = [min_0, min_1, min_2, min_3, min_4, max_0, max_1, max_2, max_3]
    if str(user_id) == str(variable.case_2_winners):
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        data[4] = '🌟'
        variable.case_2_winners = 0
        await change_balance(balance_all=0, balance_bot=(-variable.case_2_cost + variable.case_2_bet) * 10000)
        return data
    if variable.balance_bot < variable.balance_all // 100 * variable.win_percent:
        mins = [min_0, min_1, min_2, min_3, min_4]
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        delta = 6
        while delta == 6 or delta == 4:
            delta = randint(0, 5)
        data[delta] = '🌟'
        if variable.balance_bot + (-data[4] + variable.case_2_bet) * 10000 < variable.balance_all // 100 * \
                variable.win_percent:
            data[4] = choice(mins)
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_2_bet) * 10000)
            return data
        else:
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_2_bet) * 10000)
            return data
    else:
        mins = [min_0, min_1, min_2, min_3, min_4]
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        delta = 6
        while delta == 6 or delta == 4:
            delta = randint(0, 5)
        data[delta] = '🌟'
        if variable.balance_bot + (-data[4] + variable.case_2_bet) * 10000 < variable.balance_all // 100 * \
                variable.win_percent:
            data[4] = choice(mins)
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_2_bet) * 10000)
            return data
        else:
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_2_bet) * 10000)
            return data


async def case_data_two_ticket():
    from data import variable
    from random import choice, randint
    data = ['', '', '', '', '', '']
    bet = int(variable.case_2_bet)
    min_0 = bet // 5
    min_1 = bet // 4
    min_2 = bet // 3
    min_3 = bet // 2
    min_4 = (bet // 3) * 2
    max_0 = bet * 2
    max_1 = bet * 3 // 2
    max_2 = bet * 4 // 3
    max_3 = bet * 5 // 3
    bets = [min_0, min_1, min_2, min_3, min_4, max_0, max_1, max_2, max_3]
    mins = [min_0, min_1, min_2, min_3, min_4]
    i = 0
    while i < 6:
        data[i] = choice(bets)
        i += 1
    delta = 6
    while delta == 6 or delta == 4:
        delta = randint(0, 5)
    data[delta] = '🌟'
    data[4] = choice(mins)
    await change_balance(balance_all=0, balance_bot=-data[4]*10000)
    return data


async def case_data_three_money(user_id):
    from data import variable
    from random import choice, randint
    data = ['', '', '', '', '', '']
    bet = int(variable.case_3_bet)
    min_0 = bet // 5
    min_1 = bet // 4
    min_2 = bet // 3
    min_3 = bet // 2
    min_4 = (bet // 3) * 2
    max_0 = bet * 2
    max_1 = bet * 3 // 2
    max_2 = bet * 4 // 3
    max_3 = bet * 5 // 3
    bets = [min_0, min_1, min_2, min_3, min_4, max_0, max_1, max_2, max_3]
    if str(user_id) == str(variable.case_3_winners):
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        data[4] = '🥇'
        variable.case_3_winners = 0
        await change_balance(balance_all=0, balance_bot=(-variable.case_3_cost + variable.case_3_bet) * 10000)
        return data
    if variable.balance_bot < variable.balance_all // 100 * variable.win_percent:
        mins = [min_0, min_1, min_2, min_3, min_4]
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        delta = 6
        while delta == 6 or delta == 4:
            delta = randint(0, 5)
        data[delta] = '🥇'
        if variable.balance_bot + (-data[4] + variable.case_3_bet) * 10000 < variable.balance_all // 100 * \
                variable.win_percent:
            data[4] = choice(mins)
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_3_bet) * 10000)
            return data
        else:
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_3_bet) * 10000)
            return data
    else:
        mins = [min_0, min_1, min_2, min_3, min_4]
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        delta = 6
        while delta == 6 or delta == 4:
            delta = randint(0, 5)
        data[delta] = '🥇'
        if variable.balance_bot + (-data[4] + variable.case_3_bet) * 10000 < variable.balance_all // 100 * \
                variable.win_percent:
            data[4] = choice(mins)
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_3_bet) * 10000)
            return data
        else:
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_3_bet) * 10000)
            return data


async def case_data_three_ticket():
    from data import variable
    from random import choice, randint
    data = ['', '', '', '', '', '']
    bet = int(variable.case_3_bet)
    min_0 = bet // 5
    min_1 = bet // 4
    min_2 = bet // 3
    min_3 = bet // 2
    min_4 = (bet // 3) * 2
    max_0 = bet * 2
    max_1 = bet * 3 // 2
    max_2 = bet * 4 // 3
    max_3 = bet * 5 // 3
    bets = [min_0, min_1, min_2, min_3, min_4, max_0, max_1, max_2, max_3]
    mins = [min_0, min_1, min_2, min_3, min_4]
    i = 0
    while i < 6:
        data[i] = choice(bets)
        i += 1
    delta = 6
    while delta == 6 or delta == 4:
        delta = randint(0, 5)
    data[delta] = '🥇'
    data[4] = choice(mins)
    await change_balance(balance_all=0, balance_bot=-data[4]*10000)
    return data


async def case_data_four_money(user_id):
    from data import variable
    from random import choice, randint
    data = ['', '', '', '', '', '']
    bet = int(variable.case_4_bet)
    min_0 = bet // 5
    min_1 = bet // 4
    min_2 = bet // 3
    min_3 = bet // 2
    min_4 = (bet // 3) * 2
    max_0 = bet * 2
    max_1 = bet * 3 // 2
    max_2 = bet * 4 // 3
    max_3 = bet * 5 // 3
    bets = [min_0, min_1, min_2, min_3, min_4, max_0, max_1, max_2, max_3]
    if str(user_id) == str(variable.case_4_winners):
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        data[4] = '🃏'
        variable.case_4_winners = 0
        await change_balance(balance_all=0, balance_bot=(-variable.case_4_cost + variable.case_4_bet) * 10000)
        return data
    if variable.balance_bot < variable.balance_all // 100 * variable.win_percent:
        mins = [min_0, min_1, min_2, min_3, min_4]
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        delta = 6
        while delta == 6 or delta == 4:
            delta = randint(0, 5)
        data[delta] = '🃏'
        if variable.balance_bot + (-data[4] + variable.case_4_bet) * 10000 < variable.balance_all // 100 * \
                variable.win_percent:
            data[4] = choice(mins)
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_4_bet) * 10000)
            return data
        else:
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_4_bet)*10000)
            return data
    else:
        mins = [min_0, min_1, min_2, min_3, min_4]
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        delta = 6
        while delta == 6 or delta == 4:
            delta = randint(0, 5)
        data[delta] = '🃏'
        if variable.balance_bot + (-data[4] + variable.case_4_bet) * 10000 < variable.balance_all // 100 * \
                variable.win_percent:
            data[4] = choice(mins)
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_4_bet) * 10000)
            return data
        else:
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_4_bet) * 10000)
            return data


async def case_data_four_ticket():
    from data import variable
    from random import choice, randint
    data = ['', '', '', '', '', '']
    bet = int(variable.case_4_bet)
    min_0 = bet // 5
    min_1 = bet // 4
    min_2 = bet // 3
    min_3 = bet // 2
    min_4 = (bet // 3) * 2
    max_0 = bet * 2
    max_1 = bet * 3 // 2
    max_2 = bet * 4 // 3
    max_3 = bet * 5 // 3
    bets = [min_0, min_1, min_2, min_3, min_4, max_0, max_1, max_2, max_3]
    mins = [min_0, min_1, min_2, min_3, min_4]
    i = 0
    while i < 6:
        data[i] = choice(bets)
        i += 1
    delta = 6
    while delta == 6 or delta == 4:
        delta = randint(0, 5)
    data[delta] = '🃏'
    data[4] = choice(mins)
    await change_balance(balance_all=0, balance_bot=-data[4]*10000)
    return data


async def case_data_five_money(user_id):
    from data import variable
    from random import choice, randint
    data = ['', '', '', '', '', '']
    bet = int(variable.case_5_bet)
    min_0 = bet // 5
    min_1 = bet // 4
    min_2 = bet // 3
    min_3 = bet // 2
    min_4 = (bet // 3) * 2
    max_0 = bet * 2
    max_1 = bet * 3 // 2
    max_2 = bet * 4 // 3
    max_3 = bet * 5 // 3
    bets = [min_0, min_1, min_2, min_3, min_4, max_0, max_1, max_2, max_3]
    if str(user_id) == str(variable.case_5_winners):
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        data[4] = '🏆'
        variable.case_5_winners = 0
        await change_balance(balance_all=0, balance_bot=(-variable.case_5_cost + variable.case_5_bet) * 10000)
        return data
    if variable.balance_bot < variable.balance_all // 100 * variable.win_percent:
        mins = [min_0, min_1, min_2, min_3, min_4]
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        delta = 6
        while delta == 6 or delta == 4:
            delta = randint(0, 5)
        data[delta] = '🏆'
        if variable.balance_bot + (-data[4] + variable.case_5_bet) * 10000 < variable.balance_all // 100 * \
                variable.win_percent:
            data[4] = choice(mins)
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_5_bet) * 10000)
            return data
        else:
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_5_bet) * 10000)
            return data
    else:
        mins = [min_0, min_1, min_2, min_3, min_4]
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        delta = 6
        while delta == 6 or delta == 4:
            delta = randint(0, 5)
        data[delta] = '🏆'
        if variable.balance_bot + (-data[4] + variable.case_5_bet) * 10000 < variable.balance_all // 100 * \
                variable.win_percent:
            data[4] = choice(mins)
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_5_bet) * 10000)
            return data
        else:
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_5_bet) * 10000)
            return data


async def case_data_five_ticket():
    from data import variable
    from random import choice, randint
    data = ['', '', '', '', '', '']
    bet = int(variable.case_5_bet)
    min_0 = bet // 5
    min_1 = bet // 4
    min_2 = bet // 3
    min_3 = bet // 2
    min_4 = (bet // 3) * 2
    max_0 = bet * 2
    max_1 = bet * 3 // 2
    max_2 = bet * 4 // 3
    max_3 = bet * 5 // 3
    bets = [min_0, min_1, min_2, min_3, min_4, max_0, max_1, max_2, max_3]
    mins = [min_0, min_1, min_2, min_3, min_4]
    i = 0
    while i < 6:
        data[i] = choice(bets)
        i += 1
    delta = 6
    while delta == 6 or delta == 4:
        delta = randint(0, 5)
    data[delta] = '🏆'
    data[4] = choice(mins)
    await change_balance(balance_all=0, balance_bot=-data[4]*10000)
    return data


async def case_data_six_money(user_id):
    from data import variable
    from random import choice, randint
    data = ['', '', '', '', '', '']
    bet = int(variable.case_6_bet)
    min_0 = bet // 5
    min_1 = bet // 4
    min_2 = bet // 3
    min_3 = bet // 2
    min_4 = (bet // 3) * 2
    max_0 = bet * 2
    max_1 = bet * 3 // 2
    max_2 = bet * 4 // 3
    max_3 = bet * 5 // 3
    bets = [min_0, min_1, min_2, min_3, min_4, max_0, max_1, max_2, max_3]
    if str(user_id) == str(variable.case_6_winners):
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        data[4] = '💎'
        variable.case_6_winners = 0
        await change_balance(balance_all=0, balance_bot=(-variable.case_6_cost + variable.case_6_bet) * 10000)
        return data
    if variable.balance_bot < variable.balance_all // 100 * variable.win_percent:
        mins = [min_0, min_1, min_2, min_3, min_4]
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        delta = 6
        while delta == 6 or delta == 4:
            delta = randint(0, 5)
        data[delta] = '💎'
        if variable.balance_bot + (-data[4] + variable.case_6_bet) * 10000 < variable.balance_all // 100 * \
                variable.win_percent:
            data[4] = choice(mins)
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_6_bet) * 10000)
            return data
        else:
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_6_bet) * 10000)
            return data
    else:
        mins = [min_0, min_1, min_2, min_3, min_4]
        i = 0
        while i < 6:
            data[i] = choice(bets)
            i += 1
        delta = 6
        while delta == 6 or delta == 4:
            delta = randint(0, 5)
        data[delta] = '💎'
        if variable.balance_bot + (-data[4] + variable.case_6_bet) * 10000 < variable.balance_all // 100 * \
                variable.win_percent:
            data[4] = choice(mins)
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_6_bet) * 10000)
            return data
        else:
            await change_balance(balance_all=0, balance_bot=(-data[4] + variable.case_6_bet) * 10000)
            return data


async def case_data_six_ticket():
    from data import variable
    from random import choice, randint
    data = ['', '', '', '', '', '']
    bet = int(variable.case_6_bet)
    min_0 = bet // 5
    min_1 = bet // 4
    min_2 = bet // 3
    min_3 = bet // 2
    min_4 = (bet // 3) * 2
    max_0 = bet * 2
    max_1 = bet * 3 // 2
    max_2 = bet * 4 // 3
    max_3 = bet * 5 // 3
    bets = [min_0, min_1, min_2, min_3, min_4, max_0, max_1, max_2, max_3]
    mins = [min_0, min_1, min_2, min_3, min_4]
    i = 0
    while i < 6:
        data[i] = choice(bets)
        i += 1
    delta = 6
    while delta == 6 or delta == 4:
        delta = randint(0, 5)
    data[delta] = '💎'
    data[4] = choice(mins)
    await change_balance(balance_all=0, balance_bot=-data[4]*10000)
    return data


async def case_data_secret(user_id):
    from data import variable
    from random import choice
    from loader import db
    data = ['', '', '', '', '', '']
    wins = ['🎟 на 🔥', '🎟 на 🌟', '🎟 на 🥇', '🎟 на 🃏', '🎟 на 🏆', '🎟 на 💎']
    i = 0
    while i < 6:
        data[i] = choice(wins)
        i += 1
    if str(variable.case_secret_winners) == str(user_id):
        data[4] = '🎟 на 💎'
        variable.case_secret_winners = 0
        await db.update_case_ticket(user_id=user_id, x=6)
        return data
    else:
        var = [1, 1, 1, 1, 1, 3, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 4, 1,
               1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 3, 1, 2, 1, 1, 1, 3, 4, 5]
        m = choice(var)
        await db.update_case_ticket(user_id=user_id, x=m)
        data[4] = wins[m-1]
        return data
