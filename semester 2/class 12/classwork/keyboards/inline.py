from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




first = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text='1³', callback_data='one'),
        InlineKeyboardButton(text='2³', callback_data = 'two'),
        InlineKeyboardButton(text='3³', callback_data='three')
        ],
        [
            InlineKeyboardButton(text='💀BIG AGRESSIVE BUTTON', callback_data='0')
        ],
         [
        InlineKeyboardButton(text='4', callback_data='four'),
        InlineKeyboardButton(text='5', callback_data = 'five'),
        InlineKeyboardButton(text='6', callback_data='six')
        ]
    ]
)




social_networks = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Facebook', url='https://facebook.com')
        ],
        [
            InlineKeyboardButton(text='Instagram', url='https://instagram.com')
        ],
        [
            InlineKeyboardButton(text='Twitter', url='https://twitter.com')
        ]

    ]
)