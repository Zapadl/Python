
# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#
# *Примеры:*
#
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# N = int(input('Введите число N = '))
#
# List = list(range(-N, N+1))
# print(List)

number = int(input('input your integer here: \t'))
if number>0:
for i in range(-number,number+1,1):
print(i)
elif number==0:
print(0)
else:
for i in range(-number,number-1,-1):
print(i)