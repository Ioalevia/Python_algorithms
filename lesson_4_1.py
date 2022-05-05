'''Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
трех уроков. '''
'''Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с 
клавиатуры. '''

from timeit import timeit
import cProfile


def func(n, a=0):
    if n == 0:
        return 0
    if n == 1:
        a += 1 / (-2) ** (n - 1)
        return a
    if n > 1:
        a += 1 / (-2) ** (n - 1)
        return func(n - 1, a)


def func_2(n, a=0, b=0, c=1):
    while a < n:
        b = b + c
        c = c / (-2)
        a += 1
    return b


def func_3(n, a=0, c=1):
    b = []
    while a < n:
        b.append(c)
        c = c / (-2)
        a += 1
    return sum(b)


def func_4(n, a=0, b=[], c=1):
    while a < n:
        b.append(c)
        c = c / (-2)
        a += 1
    return sum(b)


def func_5(n, a=0):
    for i in range(n):
        a += 1 / (-2) ** i
    return a


result = func(500)
result_2 = func_2(500)
result_3 = func_3(500)
result_4 = func_4(500)
result_5 = func_5(500)
print(f'Сумма: {result}.')
print(f'Сумма: {result_2}.')
print(f'Сумма: {result_3}.')
print(f'Сумма: {result_4}.')
print(f'Сумма: {result_5}.')

print(timeit('func(500)', number=500, globals=globals()))
print(timeit('func_2(500)', number=500, globals=globals()))
print(timeit('func_3(500)', number=500, globals=globals()))
print(timeit('func_4(500)', number=500, globals=globals()))
print(timeit('func_5(500)', number=500, globals=globals()))
cProfile.run('func(500)')
cProfile.run('func_2(500)')
cProfile.run('func_3(500)')
cProfile.run('func_4(500)')
cProfile.run('func_5(500)')

'''
Сумма: 0.6666666666666666.
Сумма: 0.6666666666666667.
Сумма: 0.6666666666666667.
Сумма: 0.6666666666666667.
Сумма: 0.6666666666666667.
0.205468
0.017402100000000004
0.024419499999999983
0.25972309999999993
0.16028920000000002
         503 function calls (4 primitive calls) in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
    500/1    0.001    0.000    0.001    0.001 lesson_4_1.py:5(func)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson_4_1.py:15(func_2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         505 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson_4_1.py:22(func_3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
      500    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         505 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 lesson_4_1.py:30(func_4)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.001    0.001    0.001    0.001 {built-in method builtins.sum}
      500    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson_4_1.py:37(func_5)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



Process finished with exit code 0
'''
'''Вывод: func_2 показала семя самой эффективной. Наименьшее количество вызовов, используемой памяти.
Отсутствие лишнего кода. Так же заинтересовала разница в выполнении func_3 и func_4.
Изменение расположения переменной увеличило время выполнения в 10 раз.'''
