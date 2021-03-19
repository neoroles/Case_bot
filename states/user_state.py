from aiogram.dispatcher.filters.state import StatesGroup, State


class Balance(StatesGroup):
    Up = State()
    UpConf = State()
    Down = State()


class Bet(StatesGroup):
    Change = State()
    Input = State()


class Ver(StatesGroup):
    Change = State()
    Input = State()


class Lottery(StatesGroup):
    Bet = State()
    Input = State()
