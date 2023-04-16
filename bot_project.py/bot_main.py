from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage


TOKEN = '6199979785:AAG58z8ljkovI8AkvFhvlqHGf5t8hLDl8dU'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

ADMONS = [1338535362]


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Hello! I am a planner bot. Using the commands below you can schedule your day or make a to-do list!📃')







































if __name__ == '__main__':
    executor.start_polling(dp)
