from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards import *

from parse_news import parse_economical_news, parse_european_news


import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(commands='start')
async def start_process(message: types.Message ):
    await message.answer('Hi! In order to check the news, press the button: ', reply_markup=news)




@dp.message_handler()
async def get_news(message: types.Message, state: FSMContext):
    if message.text == 'European news':
        await message.answer('The news were gotten. Choose with the button:', reply_markup=choise)
        await state.set_state('read_european_news')
    elif message.text == 'Economical news':
        await message.answer('The news were gotten. Choose with the button:', reply_markup=choise)
        await state.set_state('read_economical_news')




@dp.callback_query_handler(state='*', text='0')
async def end_reading(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('You finished reading the news. To read them again - type /start')
    await state.finish()




@dp.callback_query_handler(state='read_european_news')
async def read_european_news(callback: types.CallbackQuery, state: FSMContext):
    news = parse_european_news()
    if callback.data == '1':
        title = news[0]['title']
        article = news[0]['text']
        link = news[0]['link']
        await callback.message.answer(
            f'<b>{title}</b>\n'
            f'{article}\n'
            f'Sourse: {link}\n'
            f'Would you like to read anything else?', reply_markup=choise, parse_mode='html'
        )
    elif callback.data == '2':
        title = news[1]['title']
        article = news[1]['text']
        link = news[1]['link']
        await callback.message.answer(
            f'<b>{title}</b>\n'
            f'{article}\n'
            f'Sourse: {link}\n'
            f'Would you like to read anything else?', reply_markup=choise, parse_mode='html'
        )
    


@dp.callback_query_handler(state='read_economical_news')
async def read_economical_news(callback: types.CallbackQuery):
    news = parse_economical_news()
    if callback.data == '1':
        title = news[0]['title']
        article = news[0]['text']
        link = news[0]['link']
        await callback.message.answer(
            f'<b>{title}</b>\n'
            f'{article}\n'
            f'Sourse: {link}\n'
            f'Would you like to read anything else?', reply_markup=choise, parse_mode='html'
        )
    elif callback.data == '2':
        title = news[1]['title']
        article = news[1]['text']
        link = news[1]['link']
        await callback.message.answer(
            f'<b>{title}</b>\n'
            f'{article}\n'
            f'Sourse: {link}\n'
            f'Would you like to read anything else?', reply_markup=choise, parse_mode='html'
        )






if __name__ == '__main__':
    executor.start_polling(dp)