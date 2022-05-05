'''Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.'''

from timeit import timeit
import cProfile

'''Решето Эратосфена'''
def sieve(q):
    n = 15 * q
    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    while 0 in a:
        a.remove(0)
    return a[q - 1]

'''Не Решето Эратосфена'''
def prime(q):
    n = q * 15
    a = []
    for i in range(2, n+1):
        for j in a:
            if i % j == 0:
                break
        else:
            a.append(i)
    return a[q-1]

result = sieve(1000)
print(f'Число: {result}.')
result_2 = prime(1000)
print(f'Число: {result_2}.')

print(timeit('sieve(1000)', number=10, globals=globals()))
print(timeit('prime(1000)', number=10, globals=globals()))
cProfile.run('sieve(1000)')
cProfile.run('prime(1000)')

'''Вывод: Решето Эратосфена работает медленнее иных алгоритмов в несколько раз.
Размер массива расчитывал из расчета в 15 раз больше поряддкового номера искомого числа. Понимаю, что не оптимально,
но до иного решения пока не додумался.'''