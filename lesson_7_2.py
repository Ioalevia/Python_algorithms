import random

s_list = [random.uniform(0, 49.9999999999) for i in range(10)]
print(f'До сортировки: {s_list}')


def sorting(sort_list):

    if len(sort_list) < 2:
        return sort_list

    left = sorting(sort_list[:len(sort_list) // 2])
    right = sorting(sort_list[len(sort_list) // 2:])
    result = []
    l_num = 0
    r_num = 0

    while l_num < len(left) or r_num < len(right):
        if l_num >= len(left):
            result.append(right[r_num])
            r_num += 1
        elif r_num >= len(right):
            result.append(left[l_num])
            l_num += 1
        elif left[l_num] < right[r_num]:
            result.append(left[l_num])
            l_num += 1
        else:
            result.append(right[r_num])
            r_num += 1
    return result


sorted_list = sorting(s_list)
print(f'После сортировки: {sorted_list}')