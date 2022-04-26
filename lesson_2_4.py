'''Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.'''
'''https://drive.google.com/file/d/1qv83w5DEom8xpp5VsKlwM6bw11ldu1mo/view?usp=sharing'''
n = int(input('Количество элементов: '))

def func(n, a = 0):
    if n == 0:
        return 0
    if n == 1:
        a += 1 / (-2) ** (n - 1)
        return a
    if n > 1:
        a += 1 / (-2) ** (n - 1)
        return func(n - 1, a)

result = func(n)
print(f'Сумма: {result}.')