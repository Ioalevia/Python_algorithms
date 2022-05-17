'''Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].'''

from collections import deque

hex_number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
first_number = deque(input("Первое число: ").upper())
second_number = deque(input("Второе число: ").upper())
result = deque()
dop_number = 0

if len(first_number) < len(second_number):
    first_number, second_number = second_number, first_number

while len(first_number) > 0:
    if len(second_number) > 0:
        sum_num = hex_number[first_number.pop()] + hex_number[second_number.pop()] + dop_number
    else:
        sum_num = hex_number[first_number.pop()] + dop_number
    dop_number = 0
    if sum_num < 16:
        result.appendleft(hex_number[sum_num])
    else:
        result.appendleft(hex_number[sum_num - 16])
        dop_number = 1

if dop_number > 0:
    result.appendleft('1')

print(result)