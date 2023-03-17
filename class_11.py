                                                                                                            # МНОЖИНИ
# a = {1, 2, 3, 5}
# b = {6, 7, 4, 9, 5, 2}

# print(a | b)                      # ОБ'ЄДНАННЯ
# print(a.union(b))

# print(a & b)                      # ПЕРЕСЕЧЕНИЕ
# print(a.intersection(b))

# print(a - b)                      #РІЗНИЦЯ
# print(a.difference(b))

# print(a ^ b)                        #СИМЕТРИЧНА РІЗНИЦЯ
# print(a.symmetric_difference(b))




# s = {1, 2, 3}
# m = {1, 2, 3, 4, 5}

# print(s.issubset(m))


# numbers = int(input("enter smth:"))

# print(type(numbers), numbers)

# n = str(numbers)

# print(type(n), n)
 
# k = n[::-1]
# print(k)

# pre_result = list(k)

# print(type(pre_result), pre_result)

# for i in range(0, len(pre_result)):
#     pre_result[i] = int(pre_result[i])
    
# print(pre_result)

# result = [int(i) for i in pre_result]
# print(result)

# print([int(i) for i in list(str(numbers)[::-1])])


# f = []
# for i in range(7):
#     f.append(i)
# print(f)


#Or


# f = [i for i in range(5)]
# print(f)
  


                                                                                  #HW

# my_string = "my awesome string"
# count = 0
# # while True:
#     space = my_string.find(' ')
#     first_word = my_string[0:space]
#     letters = len(first_word)
#     if letters > count:
#         count = letters
#         the_longest_word = first_word
#     my_string[space:]



# print(letters, the_longest_word)



# old_string = "my awesome string "
# space = old_string.find(' ')
# if space == -1:
#     print(old_string)
# else:
#     word = old_string[:space]
#     print(word)
#     while True:
#          new_string = old_string[space+1:]
#          print(new_string)
#          new_space = new_string.find(' ')
#          if new_space == -1:
#             word = new_string
            
#          print(new_space)
#          new_word = new_string[:space]
#          print(new_word)
#          old_string = new_string

#          if





# old_string = "my awesome string "
# space = old_string.find(' ')
# if space == -1:
#     print(old_string)
# else: 
#     word = old_string[:space]

#     while True:
#         new_space = old_string.find(' ', space +1)
#         new_word = old_string[space+1: new_space]
#         if len(word) < len(new_word):
#             word = new_word
#             if len(old_string[space+1 : en])
#             break


# print(word, len(word))











# old_string = 'Hello every booooooody'

# space = old_string.find(' ')
# #print(f'Space - {space}')

# if space == -1:
#     print('The longest word is', old_string)
# else:
#     word = old_string[:space]

    
#     while True:
#         new_space = old_string.find(' ', space+1)
#         new_word = old_string[space+1:new_space]
#         if len(word) < len(new_word):
#             word = new_word
#             print(old_string[space+1:])
#             new_string = old_string[space+1:]
#         if len(new_string.split()) == 0:
#             break
#         space = new_space
#         old_string = old_string[space+1:]
# print(word)





string = input() + ' '
space = string.find(' ')
word = string[:space]
new_string = string[space+1:]

print(string.count(' '))
for i in range(string.count(' ')):
    space = new_string.find(' ')
    if len(new_string[:space]) >= len(word):
        word = new_string[:space]
    new_string = new_string[space+1:]

print(f'the longest word is: {word}')







