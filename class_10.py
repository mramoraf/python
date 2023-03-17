# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[1:-1:2])
# print(numbers[0:-1:2])
# print(numbers[2:-1:3])


'''
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

a[-1]          # last item in the array
a[-2:]         # last two items in the array
a[:-2]         # everything except the last two items
a[::-1]        # reversed string
'''

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(numbers[0:6])
# print(numbers[6:])
# print(numbers[:6])

# a = numbers.copy
# b = numbers[:]

# print(numbers[-2:])
# print(numbers[:-2])
# print(numbers[::-1])

# s = 'Ivan Ivanov'
# # print(s[:4])
# # print(s[5:])

# delimiter = ' '
# space = s.find(delimiter)
# print(space)

# name = s[0:space]
# last_name = s[space + 1:]
# print(name)
# print(last_name)


# phones = ['+38(067) 999-99-99', '+38(066) 999-99-99', '+38(067) 888-88-88', '+38(068) 777-77-77']

# kiivstar = ['067', '098', '068']
# count = 0
# for element in phones:
#     operator_code = element[4:7]
#     if operator_code in kiivstar:
#         count += 1

# print(count)

                                                                                                                   #МНОЖИНИ

# a = set('hello')
# print(a)

# b = {1, 2, 3, 4}
# print(b)

# operators_code = {'066', '098', '068', '067', '095'}
# print(operators_code)

# s = set('066', '098', '068', '067', '095')
# print(s)



                                                                                                                     #METHODS OF SETS

# numbers = {1, 2, 3}
# numbers.add(4)
# print(numbers)

# numbers = {1, 2, 3}
# numbers.remove(3)
# print(numbers)
# numbers.remove(6)

# numbers = {1, 2, 3}
# numbers.discard(5)
# print(numbers)

# goods = {'bananas', 'tomatoes', 'apples'}
# print(goods)
# goods.add('cucumber')
# print(goods)
# goods.discard('peach')
# print(goods)
# goods.remove('apples')
# print(goods)


# a = set('hello')
# b = set('hi there!')

# print(a)
# print(b)

# print(a ^ b)

# print(a | b)
# print(a.union(b))

# print(a & b)
# print(a.intersection(b))

# customers_A = {'Ivanov', 'Petrov', 'Sidorov'}
# customers_B = {'Ivanova', 'Petrova', 'Sidorov'}

# customers_AB = customers_A & customers_B
# print(customers_AB)
# all_customers = customers_A | customers_B
# print(all_customers)

# print(sorted(all_customers))



                                                                                                   #HOMEWORK

sentence = input().split()
