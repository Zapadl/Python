# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input("Введите число от 1 до 7: "))
if (day==1):
    print("1 -> нет")
elif (day==2) :
    print("2 -> нет")
elif (day == 3):
    print("3 -> нет")
elif (day==4) :
    print("4 -> нет")
elif (day==5):
    print("5 -> нет")
elif (day==6 ):
    print("6 -> да")
elif (day == 7):
    print("7-> да")
else :
    print("Данного дня недели не существует")