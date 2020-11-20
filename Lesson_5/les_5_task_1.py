"""
1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""
from collections import namedtuple
this_company = namedtuple('company', ['name_p', 'salary_p', 'salary'])
all_p = int(input('Введите количество предприятий: '))
it_salary = 0
all_cp = set()
for _ in range(1, all_p + 1):
    salary = 0
    salary_p = []
    name_p = input('Введите название предприятия: ')
    for j in range(4):
        salary_one = int(input(f'Введите прибыль за {j+1} квартал: '))
        salary_p.append(salary_one)
        salary += salary_one
    it_salary += salary
    all_company = this_company(name_p=name_p, salary_p=tuple(salary_p), salary=salary)
    all_cp.add(all_company)
print(f'Средняя прибыль за год для всех предприятий {it_salary / all_p}')
print(10 * '-')
print(f'У этих предприятий прибвль выше среднего: ')
for all_company in all_cp:
    if all_company.salary > it_salary / all_p:
        print(all_company.name_p)
print(f'У этих предприятий прибыль меньше среднего: ')
for all_company in all_cp:
    if all_company.salary < it_salary / all_p:
        print(all_company.name_p)


