import logging
from aiogram import Bot, Dispatcher, executor, types
from keyboards import request_contact

from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from steps import Flow


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())





@dp.message_handler(commands='start')
async def start_the_process(message: types.Message):
    await message.answer(text='Hi I am a bot with state machines. For registration - share your conntact.', reply_markup=request_contact)



@dp.message_handler(commands='start', state=Flow.RegisterState)
async def start_the_process(message: types.Message):
    await message.answer('You have already registered.')



@dp.message_handler(content_types=['text'], state=Flow.NameState)
async def name_sharing(message: types.Message):
    await Flow.RegisterState.set()
    await message.answer(f'{message.text}, thank you.')




@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def registration(message: types.Message):
    if message.from_id != message.contact.user_id:
        await message.answer('You gave not your contacts')
    else:

        full_name = message.contact.full_name
        phone = message.contact.phone_number
        await Flow.NameState.set()

        await message.answer(f'{full_name}Now I need your name.\nYour phone number: {phone}')




if __name__ == '__main__':
    executor.start_polling(dp)