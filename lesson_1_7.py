'''https://drive.google.com/file/d/17xz4OmK66R6JW_4VLco3vMikJeAAGbCO/view?usp=sharing'''

a = int(input('Первый отрезок равен: '))
b = int(input('Второй отрезок равен: '))
c = int(input('Третий отрезок равен: '))

if a + b > c and a + c > b and b + c > a:
    if a == b or b == c or a == c:
        if a == b and b == c:
            print('Треугольник равносторонний.')
        else:
            print('Треугольник равнобедренный.')
    else:
        print('Треугольник разносторонний.')
else:
    print('Нельзя составить треугольник.')