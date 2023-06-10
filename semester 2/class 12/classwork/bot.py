from aiogram import types, Dispatcher, Bot, executor
from keyboards.inline import first, social_networks
import logging
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards.default import colors, request_contact


logging.basicConfig(level=logging.INFO)





bot = Bot('6071969222:AAGnfS3N9P2Hh2aUJKv84t2H1bUvs-3Q2kc')
dp = Dispatcher(bot, storage=MemoryStorage())




@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(text='Hello!')


@dp.message_handler(text='I wanna press button')
async def echo(message: types.Message):
    await message.answer(text='Press this button!', reply_markup=first)



# @dp.callback_query_handler(text='one')
# async def second_step(callback: types.CallbackQuery):
#     await callback.message.answer("You've already pressed")




@dp.callback_query_handler()
async def second_step(callback: types.CallbackQuery):
    if callback.data == 'one':
        await callback.message.answer("it is 1")
    elif callback.data == 'two':
        await callback.message.answer("It's gonna be 8")
    elif callback.data == 'three':
        await callback.message.answer('It will be 27')





@dp.message_handler(commands='choose_color')
async def choode_color(message: types.Message):
    await message.answer('Choose your color.', reply_markup=colors)




@dp.message_handler(commands='give_info')
async def get_contact(message: types.Message):
    await message.answer('Gimme your information', reply_markup=request_contact)




@dp.message_handler(content_types=types.ContentType.CONTACT)
async def use_contact_info(message: types.Message):
    if message.contact.user_id != message.from_id:
        await message.answer('That is not your number.')
    else:
        await message.answer(f"Hello, {message.contact.phone_number}")




@dp.message_handler(commands='socials')
async def get_socials(message: types.Message):
    await message.answer('Available socials', reply_markup=social_networks)




if __name__ == '__main__':
    executor.start_polling(dp)
