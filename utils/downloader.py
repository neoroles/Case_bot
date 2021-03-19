

async def download_cases():
    from loader import db
    from data import variable
    data_1 = await db.select_case_const(x=1)
    variable.case_1_name = data_1[0]
    variable.case_1_photo = data_1[1]
    variable.case_1_description = data_1[2]
    variable.case_1_bet = data_1[3]
    variable.case_1_cost = data_1[4]
    data_2 = await db.select_case_const(x=2)
    variable.case_2_name = data_2[0]
    variable.case_2_photo = data_2[1]
    variable.case_2_description = data_2[2]
    variable.case_2_bet = data_2[3]
    variable.case_2_cost = data_2[4]
    data_3 = await db.select_case_const(x=3)
    variable.case_3_name = data_3[0]
    variable.case_3_photo = data_3[1]
    variable.case_3_description = data_3[2]
    variable.case_3_bet = data_3[3]
    variable.case_3_cost = data_3[4]
    data_4 = await db.select_case_const(x=4)
    variable.case_4_name = data_4[0]
    variable.case_4_photo = data_4[1]
    variable.case_4_description = data_4[2]
    variable.case_4_bet = data_4[3]
    variable.case_4_cost = data_4[4]
    data_5 = await db.select_case_const(x=5)
    variable.case_5_name = data_5[0]
    variable.case_5_photo = data_5[1]
    variable.case_5_description = data_5[2]
    variable.case_5_bet = data_5[3]
    variable.case_5_cost = data_5[4]
    data_6 = await db.select_case_const(x=6)
    variable.case_6_name = data_6[0]
    variable.case_6_photo = data_6[1]
    variable.case_6_description = data_6[2]
    variable.case_6_bet = data_6[3]
    variable.case_6_cost = data_6[4]
    data_7 = await db.select_case_const(x=7)
    variable.case_secret_photo = data_7[1]


async def download_consts():
    from loader import db
    from data import variable
    bal = await db.select_balance()
    variable.balance_all = bal[0]
    variable.balance_bot = bal[1]
    data = await db.select_const()
    variable.win_percent = data[0]
    variable.block_lottery = data[1]
    variable.block_case = data[2]
    variable.block_nvuti = data[3]
    variable.nvuti_winner = data[4]
    variable.case_1_winners = data[5]
    variable.case_2_winners = data[6]
    variable.case_3_winners = data[7]
    variable.case_4_winners = data[8]
    variable.case_5_winners = data[9]
    variable.case_6_winners = data[10]
    variable.case_secret_winners = data[11]
