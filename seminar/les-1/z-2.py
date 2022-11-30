# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#
# Примеры:
#
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

num1 = int(input("Введите число 1: "))
num2 = int(input("Введите число 2: "))
num3 = int(input("Введите число 3: "))
num4 = int(input("Введите число 4: "))
num5 = int(input("Введите число 5: "))

max_1=num1
if max_1 <num1:
    max_1= num2
if max_1 <num3:
    max_1= num3
if max_1 <num4:
    max_1= num4
if max_1 <num5:
    max_1= num5
print(f"{max_1}")