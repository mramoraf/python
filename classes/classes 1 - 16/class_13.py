# prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23}
# print(3 in prime_numbers)


# user = {
#     'name' : 'Bill',
#     'surname' : 'Bosh',
#     'age' : 22
# }

# if 'age' in user:
#     print('User', user['name'], 'age', user['age'])
# else:
#     print('user', user['name'], 'surname', user['surname'])



# password = input('Enter your password: ')
# if len(password) < 8:
#     print('Its too short')
# else:
#     print('ok')


# alphabet = "qwertyuiopasdfghjklzxcvbnm"
# for i in alphabet:
#     print(i)


# cities = {
#     'Київ'    : 0, 
#     'Вінниця' : 240, 
#     'Харків'  : 470, 
#     'Ужгород' : 808, 
#     'Львів'   : 540, 
#     'Житомир' : 120, 
#     'Одеса'   : 430
#     }

# distance = 0
# city = ''
# for key, value in cities.items():
#     if value > distance:
#         distance = value
#         city = key

# print(city, distance)



# post_ukr = {'Київ', 'Фастів', 'Ірпінь', 'Боярка'}

# post_new = {'Київ', 'Фастів', 'Кагарлик', 'Узин', 'Ірпінь', 'Гатне', 'Боярка', 'Гостомель'}

# city = input('Enter your city: ')
# if city in post_ukr and city in post_new:
#     print('Choose one of the companies: nova poshta or ukrposta')
# elif city in post_ukr:
#     print('We can send it by ukrposta')
# elif city in post_new:
#     print('we can send it by nova poshta')
# else:
#     print("we can't send it to your city")







# clients = [
#     ['White House', 'Іванов', 3],
#     ['Shelter', 'Іванова', 5], 
#     ['Верховина', 'Іванова', 5], 
#     ['Буковель', 'Іванова', 5]

# ]


# hotels = dict()

# for voucher in clients:
#     voucher_hotel = voucher[0]
#     voucher_clients = voucher[2]

#     if hotels.get(voucher_hotel, 0) == 0:
#         hotels[voucher_hotel] = voucher_clients
#     else:
#         # hotel_clients = hotels[voucher_hotel]
#         # hotels[voucher_hotel] = hotel_clients + voucher_clients

#         hotels[voucher_hotel] += voucher_clients


# for hotel, clients in hotels.items():
#     print(f'in {hotel} currently live {clients} clients')