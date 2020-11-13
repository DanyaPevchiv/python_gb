"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random
min_number = int(input('Введите нижнюю границу ряда чисел, с которых можно выбирать случайные числа: '))
max_number = int(input('Введите верхнюю границу ряда чисел, с которых можно выбирать случайные числа: '))
n = int(input('Сколько будет всего чисел в массиве: '))
array = [random.randint(min_number, max_number) for _ in range(n)]
#print(array)
#print('-' * 20)
min_n = 0
max_n = 0
for i in range(len(array)):
    if array[i] < array[min_n]:
        min_n = i
    if array[i] > array[max_n]:
        max_n = i
array[min_n], array[max_n]= array[max_n], array[min_n]
print(array)
