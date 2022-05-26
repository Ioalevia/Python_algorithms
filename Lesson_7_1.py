import random

s_list = [random.randint(-100, 99) for i in range(10)]
print(f'До сортировки: {s_list}')


def sorting(sort_list):
    for a in range(len(sort_list) - 1):
        for b in range(len(sort_list) - 1 - a):
            if sort_list[b] < sort_list[b + 1]:
                sort_list[b], sort_list[b + 1] = sort_list[b + 1], sort_list[b]
    return sort_list


sorted_list = sorting(s_list)
print(f'После сортировки: {sorted_list}')