import random

m = 5
s_list = [random.randint(0, 100) for i in range(2 * m + 1)]
print(f'До сортировки: {s_list}')


def median_1(sort_list, m):
    step = int(len(sort_list) / 1.247)
    swap = 1
    while step > 1 or swap > 0:
        swap = 0
        i = 0
        while i + step < len(sort_list):
            if sort_list[i] > sort_list[i + step]:
                sort_list[i], sort_list[i + step] = sort_list[i + step], sort_list[i]
                swap += 1
            i += 1
        if step > 1:
            step = int(step / 1.247)
    return sort_list[m]


def median_2(sort_list, m):
        i = 1
        while i < len(sort_list):
            if sort_list[i - 1] <= sort_list[i]:
                i += 1
            else:
                sort_list[i - 1], sort_list[i] = sort_list[i], sort_list[i - 1]
                if i > 1:
                    i -= 1
        return sort_list[m]

sorted_list_1 = median_1(s_list, m)
print(f'Сортировка расческой. Медиана: {sorted_list_1}')
sorted_list_2 = median_2(s_list, m)
print(f'Сортировка гномья. Медиана: {sorted_list_2}')