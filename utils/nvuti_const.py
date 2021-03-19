from data import variable


async def create_const_nvuti_big(ver: int):
    from random import randint
    max_c = randint(2000, 9000)
    min_c = randint(100, 1000)
    difference = max_c - min_c
    subtrahend = difference * (100-ver) // 200
    min_const = max_c - subtrahend
    max_const = min_c + subtrahend
    return min_c, min_const, max_c, max_const


async def create_const_nvuti_small(ver: int):
    from random import randint
    max_c = randint(2000, 9000)
    min_c = randint(100, 1000)
    difference = max_c - min_c
    if ver == 50:
        subtrahend = difference // 2
        min_const = max_c - subtrahend
        max_const = min_const
        return min_c, min_const, max_c, max_const
    else:
        subtrahend = difference * ver // 200
        min_const = min_c + subtrahend
        max_const = max_c - subtrahend
        return min_c, min_const, max_c, max_const


async def check_win(possible_victory: int, ver: int, user_id: int):
    if variable.balance_bot - possible_victory < variable.balance_all * variable.win_percent // 100:
        return 0
    else:
        from random import randint
        chance = randint(0, 100)
        if ver >= 75:
            if chance > ver * 9 // 10:
                return 0
            else:
                return 1
        elif ver >= 40:
            if chance > ver * 8 // 10:
                return 0
            else:
                return 1
        elif ver >= 10:
            if chance > ver * 8 // 10:
                return 0
            else:
                return 1
        else:
            if int(variable.nvuti_winner) == int(user_id):
                return 1
            else:
                return 0






