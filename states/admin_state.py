from aiogram.dispatcher.filters.state import StatesGroup, State


class CaseEditor(StatesGroup):
    Input = State()
    Key = State()


class UpKeyBal(StatesGroup):
    Input = State()


class WinPercent(StatesGroup):
    Input = State()


class Winner(StatesGroup):
    Input = State()


class CreateDrawing(StatesGroup):
    InputOnSpeed = State()
    InputOnRandom = State()


