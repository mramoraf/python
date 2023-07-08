from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



check_balance = KeyboardButton(text='Check my balance')
cash_withdrawal = KeyboardButton(text='Cash withdrawal')


operations_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(check_balance, cash_withdrawal)