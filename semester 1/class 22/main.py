# bytes = b'Hello'
# print(bytes[1])

# OR

# bytes_str_utf16 = 'Hello World'.encode(encoding='utf-16')
# bytes_str_utf8 = 'Hello World'.encode()
# print(list(bytes_str_utf16))
# print(list(bytes_str_utf8)) 
# print(list(bytes_str))



# numbers = [0, 128, 255]
# bytes_numbers = bytes(numbers)
# # print(bytes_numbers)


# for i in numbers:
#     print(hex(i))




# symbol = 'a'
# print(ord(symbol))

# symbol_bytes = 97
# print(chr(symbol_bytes))



# check = ['🐔','🥚']
# check.sort()
# print(check)

# a = '🥚'.encode()
# b = '🐔'.encode()
# print(a > b)



with open('class 22//data.bin', 'wb') as file:
    file.write(b'Hello World')
