from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import lists

TOKEN = '6199979785:AAG58z8ljkovI8AkvFhvlqHGf5t8hLDl8dU'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

ADMONS = [1338535362]


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Hello! I am a planner bot. Using the commands below you can schedule your day or make a to-do list!📃')


@dp.message_handler(commands='new_item')
async def set_new_item(message=types.Message):
    listed_items = []
    await message.answer('Okay, now write down name of your item for your list.')
    new_item = message.text
    listed_items.append(new_item)
    await message.answer(text='Awesome! The new item successfully added.')





@dp.message_handler(commands='show_my_list')
async def show_my_list(message=types.Message):
    global listed_items 
    await print(listed_items)





































if __name__ == '__main__':
    executor.start_polling(dp)
