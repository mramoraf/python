import logging
from aiogram import Bot, Dispatcher, executor, types
from keyboards import lightsall, redkb, yellowkb, greenkb, traffic_off_kb

from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from steps import Trafficlights


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(commands='start')
async def start_process(message: types.Message):
    await message.answer('Hi I am a bot with statemachines')


@dp.message_handler(commands='traffic_light_on')
async def traffic_light_on(message: types.Message):
    await Trafficlights.StateOn.set()
    await message.answer('You turned on the traffic light 🚦\n'
                         'Now you can choose any of this lights: ',
                         reply_markup=lightsall)





@dp.message_handler(text='Red 🔴', state=Trafficlights.StateOn)
async def traffic_red(message: types.Message):
    await Trafficlights.StateRed.set()
    await message.answer('You turned on the red light 🔴\n'
                         'Now you can turn on the yellow one: ',
                         reply_markup=yellowkb)
    


@dp.message_handler(text='Yellow 🟡', state=Trafficlights.StateRed)
async def traffic_yellow(message: types.Message):
    await Trafficlights.StateYellow.set() 
    await message.answer('You turned on the yellow light 🟡\n'
                         'Now you can turn on the green one: ',
                         reply_markup=greenkb)
    


@dp.message_handler(text='Green 🟢', state=Trafficlights.StateYellow)
async def traffic_green(message: types.Message):
    await Trafficlights.StateGreeen.set()
    await message.answer('You turned on the green light 🟢\n'
                         'Now you can switch off the traffic light',
                         reply_markup=traffic_off_kb)
    

@dp.message_handler(text='switch off', state=Trafficlights.StateGreeen)
async def traffic_switch_off(message: types.Message):
    await dp.current_state().reset_state()
    await message.answer('You switched off the traffic light.\n'
                         'If you wanna switch it on again, type /traffic_light_on')









if __name__ == '__main__':
    executor.start_polling(dp)