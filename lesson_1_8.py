'''https://drive.google.com/file/d/1gHhbdm7Czs888QR7UYLlwg82ZvnC19o0/view?usp=sharing'''

a = int (input('Введите год: '))
if a %4 ==0:
    if a % 100 != 0 or a % 400 == 0:
        print('Высокосный год')
    else:
        print('Невысокосный год')
else:
    print('Невысокосный год')