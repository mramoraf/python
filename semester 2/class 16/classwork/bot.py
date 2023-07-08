import logging
from aiogram import Bot, Dispatcher, executor, types
from keyboards import *

from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from steps import Operations




logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

balance = int(5000)


@dp.message_handler(commands='start')
async def start_process(message: types.Message):
    await Operations.StateOn.set()
    await message.answer("Hi. I am ATM bot. To begin using me type /use_atm")



@dp.message_handler(commands='use_atm', state='*')
async def start_process(message: types.Message):
    await Operations.CardNumberState.set()
    await message.answer("Awesome! At first, I need your card's number.")





@dp.message_handler(content_types=['text'], state=Operations.CardNumberState)
async def get_card_number(message: types.Message):
    if len(message.text) > 16 or len(message.text) < 16:
        await message.answer("Sorry, but you wrote your card's number wrongly.\nTry again and make sure you write without spaces.")
    else:
        await Operations.PinState.set()
        await message.answer('Okay. Now I need your PIN')




@dp.message_handler(content_types=['text'], state=Operations.PinState)
async def get_card_number(message: types.Message):
    if len(message.text) > 4 or len(message.text) < 4:
        await message.answer("Sorry, but you wrote your card's PIN wrongly, it must consist of 4 symbols.\nTry again.")
    else:
        await Operations.ChooseOperationState.set()
        await message.answer('Super! You got in. Please, choose the operation you need.', reply_markup=operations_kb)



@dp.message_handler(text='Check my balance', state=Operations.ChooseOperationState)
async def checking_my_balance(message: types.Message):
    global balance
    await dp.current_state().reset_state()
    await message.answer(f"Your balance is: {balance}\nIf you wanna choose another operation, begin logging in again by typing /use_atm")


@dp.message_handler(text='Cash withdrawal', state=Operations.ChooseOperationState)
async def cash_withdrawal(message: types.Message):
    await Operations.GettingMoneyState.set()
    await message.answer('Okay. Now give me the amout of money you want to get.')


@dp.message_handler(content_types=['text'], state=Operations.GettingMoneyState)
async def getting_money(message: types.Message):
    global balance
    if int(message.text) < balance or int(message.text) == balance:
        on_card = balance - int(message.text)
        balance = on_card
        await dp.current_state().reset_state()
        await message.answer(f'Here is your cash. Your balance is: {balance}\nThank you for cooperation')
    else:
        await message.answer("Sorry, but here is not enough money.\nPlease, choose less money.")





if __name__ == '__main__':
    executor.start_polling(dp)