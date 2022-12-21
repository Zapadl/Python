# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)


import random
length = int(input("Введите длину массива: "))
height = int(input("Введите высоту массива: "))

massiv =[]

massiv = []
average_lines = []
for i in range(height):
    massiv.append(list())
    summ = 0
    for j in range(length):
        massiv[i].append(random.randint(0, 99))
        summ += massiv[i][j]
    average_lines.append(summ // length)
    print(f'{massiv[i]} - Среднее арифметичсекое строки {average_lines[i]}')