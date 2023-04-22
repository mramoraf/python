# import random

# my_list = [ 66, 8, 30, 2, 2, 2]
# sum = 0
# for element in my_list:
#     sum += number
# print(sum(my_list))
# product = 1
# for factor in my_list:
#     product *= factor
# print(product)


# max = 0
# for element in my_list:
#     if element > max:
#         max = element
# print(max(my_list))


# lowest = 1
# for element in my_list:
#     if element < lowest:
#         lowest = element
# print(min(my_list))


# my_list = ['abc', 'xyz', 'aba', '1221']
# count = 0
# for element in my_list:
#     if len(element) >= 2 and element[0] ==element[-1]:
#         print(element)
#         count += 1
# print(count)


# list1 = list(input("enter ur list: "))
# list2 = list(input("enter ur 2nd list: "))
# print(type(list1))

# list1 = [3, 6, 8, 23]
# list2 = [4, 7, 9, 23, 45]

# result = False

# for element1 in list1:
#     for element2 in list2:
#         if element1 == element2: 
#             result = True
#             break
# print(result)


# colour_list = ['blue', 'green', 'red', 'grey', 'yellow']
# print(colour_list)
# colour_list.pop(4)
# colour_list.pop(1)
# print(colour_list)


# mylist = [7, 8, 120, 25, 44, 20, 27]

# for element in mylist:
#     if element % 2 != 0:
#         mylist.remove(element)
    
# print(mylist)


# while True:
#     name = input("eneter your name:")
#     if name:
#         break
#     else:
#         print("the name wasn't entered")


# random_number = random.randint(0, 5)
 
# while True:
#     guess = int(input("try to guess: "))
#     if random_number == guess:
#         print("You are right!")
#         break
#     else:
#         print("Try again!")


# name = input("Enter your name: ")
# last_name = input("Enter your last name: ")
# numberofletters = 0
# numberofletters2 = 0
# sum = 0

# for x in name:
#     numberofletters += 1
# print(f'in your name {numberofletters} letters')

# for y in last_name:
#     numberofletters2 += 1
# print(f'in your last name {numberofletters2} letters')

# print(f'sum of letters of your name and last name is {numberofletters + numberofletters2}')



# my_list = [1, 2, 6, 3, 12, 7, 5, 11, [3, 4, 7, 3, 1, 3, 6, 8, 0]]
# for element in my_list:
#     if type(element) == list:
#         element.sort()

# tmp = my_list[-1]
# my_list.pop(-1)

# my_list.sort()
# my_list.extend([tmp])


# print(my_list)



# continents = ['South America', 'North America', 'Antarctica']
# continents2 = ['Eurasia', 'Africa', 'Australia' ]

# continents.extend(continents2)

# continents.sort()
# print(continents)



# names = [['Andriy', 'Starashko'], ['Livia', 'Alfoldi'], ['Agnes', 'Hofer'], ['Andriy', 'Petrenko'], ['Andriy', 'Pashenko']]
# count = 0
# for student in names:
#     if student[0] == 'Andriy':
#         count += 1
# print(f'{count} students have name Andriy')


