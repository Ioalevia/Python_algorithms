'''Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).'''
'''https://drive.google.com/file/d/1qv83w5DEom8xpp5VsKlwM6bw11ldu1mo/view?usp=sharing'''
a = int(input('Число: '))

def count(a, odd = 0, even = 0):
    if a >= 10:
        if a % 2 == 0:
            even += 1
            return count(a // 10, odd, even)
        else:
            odd += 1
            return count(a // 10, odd, even)
    else:
        if a % 2 == 0:
            even += 1
            return f'Количество нечетных цифр: {odd}, Количество четных цифр: {even}.'
        else:
            odd += 1
            return f'Количество нечетных цифр: {odd}, Количество четных цифр: {even}.'

result = count(a)
print(result)