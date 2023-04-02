file = open('class 20\\homework\\hw.txt', 'a+')
while True:
    name = input('enter your name: ')
    if name == 'q':
        break
    file.write(f'{name}, ')
    



file.close()