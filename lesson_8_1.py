"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
"""

from hashlib import sha1


def substrings(s):
    len_s = len(s)
    string_set = set()
    for a in range(1, len_s):
        for b in range(len_s - a + 1):
            string_set.add(sha1(s[b:b + a].encode('utf-8')).hexdigest())
    return string_set


string = input("Строка: ")
print(f'Количество подстрок: {len(substrings(string))}')
