from aiogram.types import ReplyKeyboardMarkup,  KeyboardButton


red = KeyboardButton(text='Red 🔴')
yellow = KeyboardButton(text='Yellow 🟡')
green = KeyboardButton(text='Green 🟢')
traffic_off = KeyboardButton(text='switch off')

lightsall = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(red, yellow, green)
redkb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(red)
yellowkb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(yellow)
greenkb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(green)
traffic_off_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(traffic_off)