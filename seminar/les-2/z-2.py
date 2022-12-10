# 2) Решить следующую задачу:Вывести на экран таблицу умножения на заданное число.

a=int(input("ВВедите число: "))

for i in range(10):
    print(f"{a}*{i}={a*i}")
    i= i+1



# вариант 2 таблицы умножения:
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(end="")
# for k in range(c, d + 1):
#     print("\t", k, end="")
# print()
# for i in range(a, b+1):
#     print(i, "", end="")
#     for j in range(c, d+1):
#         print("\t", end="")
#         print(i * j, end="")
#     print()
