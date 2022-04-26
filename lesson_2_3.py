'''Сформировать из введенного числа обратное по порядку входящих в него цифр
и вывести на экран.
Например, если введено число 3486, надо вывести 6843.'''
'''https://drive.google.com/file/d/1qv83w5DEom8xpp5VsKlwM6bw11ldu1mo/view?usp=sharing'''
a = int(input('Число: '))

def inverse(a, b=0):
    if a % 10 != 0 or a // 10 != 0:
        b = b * 10 + a % 10
        return inverse(a // 10, b)
    else:
        return b + a

result = inverse(a)
print(f'Результат: {result}.')
