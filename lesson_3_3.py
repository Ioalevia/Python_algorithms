'''В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''

import random

list = [random.randint(1, 101) for i in range(10)]
print(list)
min = list[0]
max = list[0]
for i in list:
    if i > max:
        max = i
    elif i < min:
        min = i
min_target = list.index(min)
max_target = list.index(max)
list[min_target], list[max_target] = list[max_target], list[min_target]
print(list)