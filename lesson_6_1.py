import sys
from collections import deque
from collections import defaultdict


def show_size(x, level=0):
    size_par = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={size_par}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                size_par = size_par + sys.getsizeof(key)
                show_size(value, level + 1)
                size_par = size_par + sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
                size_par = size_par + sys.getsizeof(item)
    return size_par


def func_1(n, a=0, b=0, c=1):
    while a < n:
        b = b + c
        c = c / (-2)
        a += 1
    sum_member = sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(c) + sys.getsizeof(n)
    print('Память: {} байт'.format(sum_member))
    return b


def func_2(n, a=0, c=1):
    b = deque()
    while a < n:
        b.append(c)
        c = c / (-2)
        a += 1
    sum_member = sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(c)
    print('Память: {} байт'.format(sum_member))
    return sum(b)


def func_3(n, a=0, c=1):
    b = []
    while a < n:
        b.append(c)
        c = c / (-2)
        a += 1
    sum_member = sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(c) + sys.getsizeof(n)
    print('Память: {} байт'.format(sum_member))
    return sum(b)


def func_4(n, a=0):
    for i in range(n):
        a += 1 / (-2) ** i
    sum_member = sys.getsizeof(a) + sys.getsizeof(n) + sys.getsizeof(i)
    print('Память: {} байт'.format(sum_member))
    return a


def func_5(n, a=0):
    b = range(0, n)
    for i in b:
        a += 1 / (-2) ** i
    sum_member = sys.getsizeof(a) + sys.getsizeof(n) + sys.getsizeof(b) + sys.getsizeof(i)
    print('Память: {} байт'.format(sum_member))
    return a


def func_6(n, a=0):
    b = {i for i in range(n)}
    for i in b:
        a += 1 / (-2) ** i
    sum_member = sys.getsizeof(a) + sys.getsizeof(n) + sys.getsizeof(b) + sys.getsizeof(i)
    print('Память: {} байт'.format(sum_member))
    return a


def func_7(n, a=0, c=1):
    b = defaultdict(int)
    while a < n:
        b[c] = c
        c = c / (-2)
        a += 1
    sum_member = sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(c) + sys.getsizeof(n)
    print('Память: {} байт'.format(sum_member))
    return sum(b.values())


def func_8(n, a=0, c=1):
    b = {}
    while a < n:
        b[c] = c
        c = c / (-2)
        a += 1
    sum_member = sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(c) + sys.getsizeof(n)
    print('Память: {} байт'.format(sum_member))
    return sum(b.values())


result_1 = func_1(1000)  # Память: 76 байт
result_2 = func_2(1000)  # Память: 9124 байт
result_3 = func_3(1000)  # Память: 8936 байт
result_4 = func_4(1000)  # Память: 80 байт
result_5 = func_5(1000)  # Память: 128 байт
result_6 = func_6(1000)  # Память: 33064 байт
result_7 = func_7(1000)  # Память: 37048 байт
result_8 = func_8(1000)  # Память: 37040 байт
print(f'Сумма: {result_1}.')    # Сумма: 0.6666666666666667.
print(f'Сумма: {result_2}.')    # Сумма: 0.6666666666666667.
print(f'Сумма: {result_3}.')    # Сумма: 0.6666666666666667.
print(f'Сумма: {result_4}.')    # Сумма: 0.6666666666666667.
print(f'Сумма: {result_5}.')    # Сумма: 0.6666666666666667.
print(f'Сумма: {result_6}.')    # Сумма: 0.6666666666666667.
print(f'Сумма: {result_7}.')    # Сумма: 0.6666666666666667.
print(f'Сумма: {result_8}.')    # Сумма: 0.6666666666666667.


'''
Версия Python 3.9
64-разрядная операционная система, процессор x64
Варианты 1, 4, 5. Минимальное количество памяти. Размер памяти не менялся вне зависимости от n.
Даже при получении на вход значения в 1000000, затраты памяти не менялись.
Различия в затратах памяти в вариантах 1, 4 и 5 минимальны. Вариант 4 победил ввиду наименьшего количества переменных.
В вариантах 2 и 3 сравнил затраты памяти при использовании list и deque. Разница в затратах памяти несущественна,
но затраты памяти тем больще, чем выше число на входе.
Вариант 6. Использование множества set. Затраты памяти выше, чем при использовании словаря.
В вариантах 7 и 8 сравнил dict и defaultdict. Разница в затратах памяти даже меньше, чем в вариантах 2 и 3.

Окончательная победа за вариантом 4. Переменные не "наращивают" объем, а изменяются,
занимая минимальное количество памяти.
'''