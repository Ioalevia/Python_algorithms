'''Определить, какое число в массиве встречается чаще всего.'''

import random

list = [random.randint(1, 101) for i in range(100)]
print(list)
count = 0
num = 0
for i in range(1,100):
    a = 0
    for item in list:
        if item == i:
            a = a + 1
    if a > count:
        count = a
        num = i
print(f'{num} встречается {count} раз.')