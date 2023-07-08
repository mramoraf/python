from aiogram.types import ReplyKeyboardMarkup,  KeyboardButton

request_contact = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton(request_contact=True, text='Share my contact'))
