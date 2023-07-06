from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from films import films



film_choice = InlineKeyboardMarkup( ) 
for film in films:
    button = InlineKeyboardButton(text=film, callback_data=film)
    film_choice.add(button)



# [InlineKeyboardButton(text='Джон Уік 4 (16+)', callback_data='Джон Уік 4 (16+)'), InlineKeyboardButton(text='Зірки і цукор (0+)', callback_data='Зірки і цукор (0+)')],
# [InlineKeyboardButton(text='Підземелля і дракони (12+)', callback_data='Підземелля і дракони (12+)'), InlineKeyboardButton(text='Ренфілд (18+)', callback_data='Ренфілд (18+)')],
# [InlineKeyboardButton(text='Екзорцист Ватикану (16+)', callback_data='Екзорцист Ватикану (16+)'), InlineKeyboardButton(text='Люксембург, Люксембург (16+)', callback_data = 'Люксембург, Люксембург (16+)')]
