'''Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.'''

from collections import defaultdict
from collections import deque

companies = defaultdict(int)
good_companies = deque()
bad_companies = deque()
companies_number = int(input("Количество предприятий: "))
count = 0
all_money = 0

while count < companies_number:
    company_name = input("Название предприятия: ")
    month = 1
    money = 0
    while month <= 4:
        money += int(input(f'Прибыль за {month} квартал: '))
        month += 1
    companies[company_name] = money
    count += 1
    all_money += money

year_middle = all_money / companies_number

for name, cash in companies.items():
    if cash >= year_middle:
        good_companies.append(name)
    else:
        bad_companies.append(name)

print(f'Средняя прибыль всех предпрпятий: {year_middle}')
print(f'Предприятия с плохой прибылью: { ", ".join(bad_companies)}')
print(f'Предприятия с хорошей прибылью: { ", ".join(good_companies)}')