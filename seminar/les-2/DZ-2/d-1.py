# 1) Вводим с клавиатуры целое число X и У.
# Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3

x=int(input("Введите число Х: "))
y=int(input("Введите число Y: "))

while x>y:
    if y%2==0 and y%3 ==0:print(y)
    y += 1

while x<y:
    if x % 2==0 and x % 3 == 0: print(x)
    x += 1
#
# x, y = y, x #




    # x,y =int(input("Введите число Х: ")), int(input("Введите число Y: "))
# if y>x:
    x,y = y,x
#
# # for i in range(x,y):
# #     if i%2==0 and i%3==0:
# #         print(i)



