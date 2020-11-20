"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
start_number_seq = 2
finish_number_seq = 99
start_number = 2
finish_number = 9
for i in range(start_number, finish_number + 1):
    count = 0
    for j in range(start_number_seq, finish_number_seq + 1):
        if j % i == 0:
            count += 1
    print(f'В диапозоне от 2 до 99 чисел, кратных {i}, {count}')