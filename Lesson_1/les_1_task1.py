#https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=les_1.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1c9-KZeLOlQGvYuJYgGAk1S13DxXUtjhp%26export%3Ddownload
"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""
a = int(input('Введите трехзначное число: '))
c = (a % 10) + (a // 100) + (a % 100 // 10)
q = (a % 10) * (a // 100) * (a % 100 // 10)
print(f'Сумма цифр трехзначного числа равна {c}')
print(f'Произведение цифр трехзначного числа равно {q}')