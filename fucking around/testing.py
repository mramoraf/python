# if callback_query.data == 'Джон Уік 4 (16+)':
    #     await bot.send_photo(callback_query.message.chat.id, FILMS[callback_query.data]["photo"])
    #     film_url = FILMS[callback_query.data]['site_url']
    #     film_rating = FILMS[callback_query.data]['rating']
    #     film_description = FILMS[callback_query.data]['description']
    #     message = f'<b>Film url:</b> {film_url} \n <b>About:</b> {film_description}\n\n<b>Rate:</b> {film_rating}'
    #     await bot.send_message(callback_query.message.chat.id, message, parse_mode = 'html')
    # elif callback_query.data == 'Підземелля і дракони (12+)':
    #     await bot.send_photo(callback_query.message.chat.id, FILMS[callback_query.data]["photo"])
    #     film_url = FILMS[callback_query.data]['site_url']
    #     film_rating = FILMS[callback_query.data]['rating']
    #     film_description = FILMS[callback_query.data]['description']
    #     message = f'<b>Film url:</b> {film_url} \n <b>About:</b> {film_description}\n\n<b>Rate:</b> {film_rating}'
    #     await bot.send_message(callback_query.message.chat.id, message, parse_mode = 'html')
    # elif callback_query.data == 'Екзорцист Ватикану (16+)':
    #     await bot.send_photo(callback_query.message.chat.id, FILMS[callback_query.data]["photo"])
    #     film_url = FILMS[callback_query.data]['site_url']
    #     film_rating = FILMS[callback_query.data]['rating']
    #     film_description = FILMS[callback_query.data]['description']
    #     message = f'<b>Film url:</b> {film_url} \n <b>About:</b> {film_description}\n\n<b>Rate:</b> {film_rating}'
    #     await bot.send_message(callback_query.message.chat.id, message, parse_mode = 'html')
    # elif callback_query.data == 'Зірки і цукор (0+)':
    #     await bot.send_photo(callback_query.message.chat.id, FILMS[callback_query.data]['photo'])
    #     film_url = FILMS[callback_query.data]['site_url']
    #     film_rating = FILMS[callback_query.data]['rating']
    #     film_description = FILMS[callback_query.data]['description']
    #     message = f'<b>Film url:</b> {film_url}\n <b>About:</b> {film_description}\n\n<b>Rate:</b> {film_rating}'
    #     await bot.send_message(callback_query.message.chat.id, message, parse_mode='html')
    # elif callback_query.data == 'Ренфілд (18+)':
    #     await bot.send_photo(callback_query.message.chat.id, FILMS[callback_query.data]['photo'])
    #     film_url = FILMS[callback_query.data]['site_url']
    #     film_description = FILMS[callback_query.data]['description']
    #     film_rating = FILMS[callback_query.data]['rating']
    #     message = f'<b>Film url:</b> {film_url}\n<b>About:</b> {film_description}\n\n<b>Rate:</b> {film_rating}'
    #     await bot.send_message(callback_query.message.chat.id, message, parse_mode='html')
    # elif callback_query.data == 'Люксембург, Люксембург (16+)':
    #     await bot.send_photo(callback_query.message.chat.id, FILMS[callback_query.data]['photo'])
    #     film_url = FILMS[callback_query.data]['site_url']
    #     film_description = FILMS[callback_query.data]['description']
    #     film_rating = FILMS[callback_query.data]['rating']
    #     message = f'<b>Film url:</b> {film_url}\n<b>About:</b>{film_description}\n\n<b>Rate:</b>{film_rating}'
    #     await bot.send_message(callback_query.message.chat.id, message, parse_mode = 'html')












# @dp.message_handler()
# async def echo(message: types.Message):
#     user_info = {
#         'name': message.from_user.first_name,
#         'surname' : message.from_user.last_name,
#         'username': message.from_user.username,
#         'user_id': message.from_user.id
#     }
#     await message.answer(f'First name: {user_info["name"]}\nLast name: {user_info["surname"]}\nUsername: {user_info["username"]}\nUser id: {user_info["user_id"]}')
#     await message.answer(message.text)









