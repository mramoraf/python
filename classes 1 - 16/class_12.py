# a = dict()
# print(type(a))

# a = {}
# print(type(a))


# months = {
#     1: 'January',
#     2: 'February',
#     3: 'March',
#     4: 'April',
#     5: 'May'
# }
# # print(months)

# currency = {
#     'USD' : 39.46,
#     'EUR' : 39.03,
#     'GBP' : 43.84
# }

# print(currency)

# print(currency.get('EUR'))

# print(currency.get('PLN', 'current currency doesnt exist'))

# print(currency['USD'])

# months[6] = 'June'
# months[7] = 'July'
# months[8] = 'August'
# months[9] = 'September'

# print(len(months), months)

# a = months.pop(3, 'this moths doesnt exist')

# months.pop(1)



# months.clear()

# print(months)


# months.update({10: 'October', 11: 'November'})
# months.update({12: 'December'})

# print(months)


# monthes ={
#     1:  'січень',
#     2:  'лютий',
#     3:  'березень',
#     4:  'квітень',
#     5:  'травень',
#     6:  'червень',
#     7:  'липень',
#     8:  'серпень',
#     9:  'вересень',
#     10: 'жовтень',
#     11: 'листтопад',
#     12: 'грудень'
# }

# report_date = '21.11.2022'

# month = int(report_date[3:5])

# month_name = monthes.get(month)

# print('Report from', month_name)


# currencies = {
#     'USD' : 39.46,
#     'EUR' : 39.03,
#     'GBP' : 43.84
# }

# currencies['PLN'] = 8.18
# currencies['USD'] = 39
# currencies['EUR'] = 41
# currencies['GBP'] = 44
# currencies['CNY'] = 5.3
# currencies['HUF'] = 0.1
# currencies['CZK'] = 1.6

# currency = input('Enter the currency u would like to exchange: ')


# print(currencies.keys())
# # print(currencies.values())

# if currency not in currencies.keys():
#     print('we dont support such currency')
# else:
#     amount = float(input('How much money u wold like to exchange: '))
#     result = round(amount*currencies[currency], 2)
#     print('Here is your {} UAN'.format(result))




# numbers = {
#     'one': 1,
#     'two': 2,
#     'three': 3
# }


# for i in numbers:
#     print(i)

# for i in numbers.keys():
#     print(i)


# for i in numbers.values():
#     print(i)

# print(numbers.items())

# for key, value in numbers.items():
#     print(key, value)


# for key in numbers.keys():
#     numbers[key] = numbers[key]*2

# print(numbers)



# transport = {
#     'AA1111AA': 'Іванов Іван',
#     'IVANOV'  : 'Іванов Іван',
#     'AA0007AA': 'Семенов Андрій',
#     'AA007AA' : 'Іванов Іван',
#     'AВ1111AВ': 'Вінниця Водоканал',
#     'AІ1010КК': 'Семенов Андрій',
# }

# transport['II6767AO'] = 'Petrenko Petro'
# transport['CA8888CE'] = 'Ivanov Oleksiy'

# car_plate = input('Enter the plate to find car owner: ')

# car_owner = transport.get(car_plate, 'Not found')
# print('Car owner of plate {} is {}'.format(car_plate, car_owner))


# car_owners = dict()

# for owner in transport.values():
#     if car_owners.get(owner, 0) == 0:
#         car_owners[owner] = 1
#     else:
#         auto_count = car_owners[owner]
#         auto_count += 1
#         car_owners[owner] = auto_count

# for owner, auto_count in car_owners.items():
#     if auto_count > 1:
#         print(f'Owner {owner} has {auto_count} cars')




                                                                                                                    #HW


# TASK 1


# students = {
#     'Gorobets' : 3,
#     'Ivanov' : 4,
#     'Petrenko' : 2,
#     'Semenov' : 5,
#     'Garmash' : 5,
#     'Shikulo' : 3
# }

# best_grades = dict()

# for key, value in students.items():
#     if value >= 4:
#         best_grades[key] = value

    
# print(best_grades)






#TASK 2

# cities = {
#     'Budapest' : 9,
#     'Madrid' : 5,
#     'Kyiv' : 3,
#     'Amsterdam' : 6,
#     'Berlin' : 4
# }

# sum = 0
# count = len(cities)

# for i in cities.values():
#     sum += i

# average = sum/count
# print(f'the average temperature is {average}')






