"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random
min_number = int(input('Введите нижнюю границу ряда чисел, с которых можно выбирать случайные числа: '))
max_number = int(input('Введите верхнюю границу ряда чисел, с которых можно выбирать случайные числа: '))
n = int(input('Сколько будет всего чисел в массиве: '))
array = [random.randint(min_number, max_number) for _ in range(n)]
#print(array)
mosty = 1
num = array[0]
for i in range(len(array)):
    all_n = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            all_n += 1
    if all_n > mosty:
        mosty = all_n
if mosty == 1:
    print(f'Все элементы различны')
else:
    print(f'Наибольшее количество раз встречается число {num} ({mosty} раз(а))')
