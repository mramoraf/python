from aiogram.dispatcher.filters.state import StatesGroup, State


class Registration(StatesGroup):
    StateOn = State()
    StateOff = State()
    StatePhone = State()
    StateEmail = State()
    StateName = State()