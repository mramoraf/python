from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

news = ReplyKeyboardMarkup(
    keyboard=[
        
           [KeyboardButton(text='European news'),KeyboardButton(text='Economical news')] 
        
    ],
   
    resize_keyboard=True,
    one_time_keyboard=True
 
)



choise = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text='1', callback_data='1'), 
            InlineKeyboardButton(text='2', callback_data='2'),
            
        ],
        [
            InlineKeyboardButton(text='Finish', callback_data='0')
        ]

    ]
)