import logging
from weather import parse_weather
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.builtin import CommandStart
import requests



import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(CommandStart())
async def start(message:types.Message):
    await message.answer(text="Hi, I'm weather bot\nType a city you would like to know the weather in.")
    








@dp.message_handler(content_types='text')
async def choose_city(message:types.Message):
    weather_info = parse_weather(city=message.text )
    
    min_temp = round(weather_info['main']['temp_min'] - 273, 2)
    max_temp = round(weather_info['main']['temp_max'] - 273, 2)
    temperature = round(weather_info['main']['temp'] - 273, 2)
    wind_speed = round(weather_info['wind']['speed'] * 3.6, 2)
    my_message = f'Weather in {message.text}\nMin temperature: {min_temp}\nMax temperature: {max_temp}\nTemperature: {temperature}\nWind speed: {wind_speed}'
    await message.answer(text=my_message)
    # await message.answer(text=f'City - {city}\nTemperature - ')















if __name__ == '__main__': 
    executor.start_polling(dp)
    
