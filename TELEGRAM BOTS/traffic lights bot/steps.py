from aiogram.dispatcher.filters.state import StatesGroup, State


class Trafficlights(StatesGroup):
    StateOn = State()
    StateRed = State()
    StateYellow = State()
    StateGreeen = State()
    StateOff = State()