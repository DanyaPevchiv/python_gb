"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""
n = int(input('Сумму какого количества чисел из ряда нужно подсчитать: '))
sum_n = 0
item = 1
for _ in range(n):
    sum_n += item
    item /= -2
print(sum_n)