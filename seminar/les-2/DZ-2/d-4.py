# 4) Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа при просмотре слева направо упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет


a1= a = int(input(f"Введите многозначное число:  \n"))
b=0
while a1 > 0:
    digit = a1 % 10
    a1 = a1 // 10
    b = b * 10
    b = b + digit

while b>9:
  if (b/10%10)<= (b%10):
    print(f"Число {a} при просмотре слева на право не упорядочено по возрастанию ")
    break
  b = b//10
else: print(f"Число {a} при просмотре слева на право упорядочено по возрастанию ")