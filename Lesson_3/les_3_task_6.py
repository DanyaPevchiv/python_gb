"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random
min_number = int(input('Введите нижнюю границу ряда чисел, с которых можно выбирать случайные числа: '))
max_number = int(input('Введите верхнюю границу ряда чисел, с которых можно выбирать случайные числа: '))
n = int(input('Сколько будет всего чисел в массиве: '))
array = [random.randint(min_number, max_number) for _ in range(n)]
print(array)
index_min = 0
index_max = 0
for i in range(len(array)):
    if array[i] < array[index_min]:
        index_min = i
    elif array[i] > array[index_max]:
        index_max = i
if index_min > index_max:
    array[index_max], array[index_min] = array[index_min], array[index_max]
s_m = 0
for i in range(index_min + 1, index_max):
    s_m += array[i]
print(s_m)

