# text = 'lorem impsum dolor sit amet'
# chars_counter = dict()

# for char in text:
#     if char != ' ':
#         if char not in chars_counter:
#             chars_counter[char] = text.count(char)

# print(chars_counter)


# counter_list = sorted(list(chars_counter.items()), key = lambda x:x[1] )
# counter_list.reverse()
   

# OR


# counter_list = list(chars_counter.items())
# for i in range(len(counter_list)-1):
#     for element in range(len(counter_list)-i):
#         if counter_list[element][1] > counter_list[element+1][1]:
#             counter_list[element], counter_list[element+1] = counter_list[element+1], counter_list[element]


# counter_list.reverse()
# print(counter_list)


# for element in counter_list[:3]:
#     print(f'{element[0]} - {element[1]}')

# f = lambda x: x **2

# def f(x):
#     return x ** 2

# print(f(9))








# x = 50
# def func():
#     x = 2
#     print('Changing local x on', x)

# func()
# print(x)


# x = 50
# a = 1
# def func():
#     global x, a
#     print('Now x is', x)
#     x = 2
#     print('Changing local x on', x)

# func()
# print(x)


# def func(a, b=2, c=3):
#     print(f'a = {a}, b ={b}, c = {c}')

# func(5, c=7)

# def say(message, times=1):
#     message = message + ' '
#     print(message * times)

# say('Hello')
# say('World', 5)


# def total(a=5, *numbers, **phone_book):
#     print(f'a = {a}')
#     for single_item in numbers:
#         print(f'Single item - {single_item}')

#     for first_part, second_part in phone_book.items():
#         print(first_part, second_part)


# total(10, 1,2,3,4,5, Jack = 233, Alice = 2332, John=1111 )






# subscribers_news = []
# subscribers_whats_new = []
# subscribers_ads = []


# def subscribe(email, is_news = True, is_whats_new = True, is_adds = True):
#     global subscribers_ads, subscribers_whats_new, subscribers_news
#     if is_news:
#         subscribers_news.append(email)
#     if is_whats_new:
#         subscribers_whats_new.append(email)
#     if is_adds:
#         subscribers_ads.append(email)
         

# def get_subscribers(subscribers_list, list_name):
#     delimeter = '-' * 25
#     print(f'Distribution {list_name} has {len(subscribers_list) } users')

#     for user in subscribers_list:
#         print(user)
#         print(delimeter)
#         print( )


# subscribe('test@gmail.com')
# subscribe('ivanov@ukr.net', True, False, True)
# subscribe('ivanova@ukr.net', False, True, True)

# get_subscribers(subscribers_news, 'News')
# get_subscribers(subscribers_ads, 'Adds')
# get_subscribers(subscribers_whats_new, 'Whats new')