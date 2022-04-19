'''https://drive.google.com/file/d/1vV77qvVQeZrt98DjNTZhiLhsuO3UYLK8/view?usp=sharing'''

a = int(input('Введите трехзначное число: '))
b = (a // 100) + ((a % 100) // 10) + (a % 10)
c = (a // 100) * ((a % 100) // 10) * (a % 10)
print(f'Число- {a}. Сумма цифр числа- {b}. Произведение цифр числа- {c}')