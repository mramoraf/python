# b = 'bebebebebebebebebebebebebebebebebeb'
# print(b)
# print(b.count('be'))

# s = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n
#      Aliquam malesuada, est vitae suscipit vestibulum,'''

# amountof = int(input("enter the number:  "))
# if amountof > len(s):
#     print("wrong input")
# else:
#     new_string = s[amountof:]
#     print(new_string)


# s = "Im learning strings in Python. Some new methods got now"
# sentences = s.split('. ')
# sentences.pop(-1)
# print(sentences[0])
# print(sentences[1])
# print(sentences)


# words = input().split()
# print(len(words))


# OR

# a = input("enter")
# print(f'Symbols - {len(a)}')
# b = a.split()
# print(b)
# print(f'Symbols - {len(b)}')

# sentences = ["Im learning strings in Python", "Some new methods got now"]

# text = '. '.join(sentences)
# print(text)

# clean = '   spacious;   '.strip()
# print(clean)

# dog_text = "All dogs bark like dogs"
# print(dog_text)
# cat_text = dog_text.replace('dogs', 'cats')
# print(cat_text)

# map = {
#     ord('з'): 'z', 
#     ord('ю'): 'u',
#     ord('а'): 'A'
# }
# translate = 'зюа'.translate(map)
# print(translate)

# s = 'My name %s. Im %d years.' %('Oleg', 14)
# print(s)

# s = 'My name {0}. Im {1} years.'.format('Oleg', 14)

# name = 'Oleg'
# age = 14
# s = f'My name {name}. Im {age} years'
# print(s)

# print('pi: {:0.6}'.format(3.1415926))

# print('"{}" "{:+}" "{:-}" "{: }"'.format(1, 2, -3, 4))

# print("|{:<10}|{:-^10}|{:>10}|".format('left', 'center', 'right'))

# delimiter = '-' * 80
# goods = [['orange', 6, 150], ['lemon', 8, 90], ['Patato', 123, 445]]
# total_sum = 0
# number = 0 
# print(delimiter)
# print("|{:^5}|{:<40}|{:>15}|{:>15}|".format('#', "goods", "amount of", "price"))
# print(delimiter)

# for good in goods:
#     name = good[0]
#     amount = good[1]
#     money = good[2]
#     number += 1
#     total_sum += money
#     print("|{:^5}|{:<40}|{:>15}|{:>15}|".format(number, name, amount, money))

# print(delimiter)
# print("|{:<62}|{:>15}|".format("Overall", total_sum))
# print(delimiter)

                                                                                        #HOMEWORK

# name = input("Enter ur name: ")
# count = 0

# for char in name:
#     amount_of = name.count(char)
#     if amount_of > count:
#          count = amount_of
#          m = char

# print(f'letter: {m}')
# print(f'amount of this letters: {amount_of}')





# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# x = input("Enter smth: ")
# for char in x:
#     if char in numbers:
#         result = x.replace(char, ' ')
#         x = result

# print(result)






























# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# text = input()
# for i in text:
#     if i in numbers:
#         result = text.replace(i, '')

# print(result)







        




