# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

a =(input("ВВедите число, чтоб узнать дробное оно или нет? \n"))

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

if isfloat(a):
    print(f"{a} это дробное число")
else:
    print(f"{a} это не число")
