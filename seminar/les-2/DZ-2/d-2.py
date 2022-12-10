# 2) Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.




max = 0
dmax= 0
length= int(input("Сколько чисел будем вводить? "))
for i in range(length):
      a=int(input("ВВедите число: "))
      if a>dmax and a>max:
        dmax=max
        b=a
        max=b
      else:
        c=a
        dmax=c
print()
print(f"Максимальное число {max}")
print(f"Второе максимальное число {dmax}")
