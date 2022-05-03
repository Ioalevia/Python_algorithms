'''В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.'''

list1 = list(range(2, 10))
list2 = list(range(2, 100))
list3 = {}
for i in list1:
    list3[i] = []
    for b in list2:
        if b % i == 0:
            list3[i].append(b)
    print(f'{i} - {list3[i]}')