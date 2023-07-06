import logging
from aiogram import Bot, Dispatcher, executor, types
# from keyboards import lightsall, redkb, yellowkb, greenkb, traffic_off_kb

from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from steps import Registration



import pandas as pd
import numpy as np




logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(commands='start')
async def start_the_process(message: types.Message):
    await message.answer(text='Hi! I am bot for registration.\n'
                         'Type /registration and begin such an exciting registration!!')
    



@dp.message_handler(commands='registration')
async def begin_registering(message: types.Message):
    await Registration.StateOn.set()
    await message.answer(text="Let's begin the registration!!!!\n"
                         'First of all give me your name.' )




@dp.message_handler(content_types=["text"], state=Registration.StateOn)
async def name(message: types.Message):

    # user_name = [message.text]
    # users_data = pd.DataFrame(list(zip(user_name)), columns = ['name'])

    # with pd.ExcelWriter('TELEGRAM BOTS\\ragistration Bot\\data.xlsx', 'a') as data:
    #     users_data.to_excel(data, index=None)
    
    


    user_name = message.text
    with open('TELEGRAM BOTS\\ragistration Bot\\data.txt', 'a') as data:
        data.write(f'{user_name}          ')

    await Registration.StateName.set()
    await message.answer(text='Yeah. I registered your name.\n'
                         'Now I need your phone number.')




@dp.message_handler(content_types=["text"], state=Registration.StateName)
async def phone_number(message: types.Message):
    number = message.text
    with open('TELEGRAM BOTS\\ragistration Bot\\data.txt', 'a') as data:
        data.write(f'{number}          ')
    await Registration.StatePhone.set()
    await message.answer(text='Cool!! Now I finally have your phone number\n'
                         'So the last step: I wanna ask you to send me your email.')
    


@dp.message_handler(content_types=['text'], state=Registration.StatePhone)
async def email(message: types.Message):
    user_email = message.text
    with open('TELEGRAM BOTS\\ragistration Bot\\data.txt', 'a') as data:
        data.write(f'{user_email}\n')
    await dp.current_state().reset_state()
    await message.answer(text='Congratulations!! You finished the registration\n'
                         'If you wanna make it again type /registration')










if __name__ == '__main__':
    executor.start_polling(dp)
