# import logging

# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.dispatcher import FSMContext
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher.filters.builtin import CommandStart



# import os
# from dotenv import load_dotenv


# load_dotenv()

# TOKEN = os.getenv('TOKEN')

# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot, storage=MemoryStorage())



# @dp.message_handler(CommandStart())
# async def start(message:types.Message):
#     await message.answer(text='Hi, Im echo bot')



# @dp.message_handler(text='hello')
# async def greetings(message:types.Message):
#     name = message.from_user.full_name
#     await message.answer(f'Hello {name}.\nMy name Geralt.')



# @dp.message_handler(text='Погода')
# async def weather(message:types.Message):
#     await message.answer('Погода сьогодні дуже приємна, чи не так?')




# @dp.message_handler(commands=['info'])
# async def user_info(message: types.Message):
#     first_name = message.from_user.first_name
#     last_name = message.from_user.last_name
#     username = message.from_user.username
#     telegram_id = message.from_id
#     lang = message.from_user.language_code

#     await message.answer(f'ID: {telegram_id}\nFIRST NAME: {first_name}\nLAST_NAME: {last_name}\nUSENAME: @{username}\nLANGUAGE: {lang}')



# @dp.message_handler(content_types=types.ContentTypes.STICKER)
# async def echo_sticher(message: types.Message):
#     await message.answer_sticker(message.sticker.file_id)














# @dp.message_handler(content_types='text')
# async def echo(message: types.Message):
#     await message.answer(text=f'PC: {message.text}')










# if __name__ == '__main__': 
#     executor.start_polling(dp)
