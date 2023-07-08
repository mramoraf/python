from aiogram.dispatcher.filters.state import StatesGroup, State

class Operations(StatesGroup):
    StateOn = State()
    CardNumberState = State()
    PinState = State()
    ChooseOperationState = State()
    CheckBalanceState = ()
    GetCashState = State()
    GettingMoneyState = State()
    
