# 3) Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых

zarplata=int(input("введите вашу зарплату? "))
p25=0
p10=0
p3=0
p1=0
print(f"Ваша зарплата в размере {zarplata} будет выдана купюрами:")
while zarplata >24:
    zarplata=zarplata-25
    p25=p25+1
    # print(f"25 -{zarplata}")
while zarplata > 9:
    zarplata = zarplata - 10
    p10 = p10 + 1
    # print(f"10 - {zarplata}")
while zarplata > 2:
    zarplata = zarplata - 3
    p3 = p3 + 1
    # print(f"3 - {zarplata}")
while zarplata > 0:
    zarplata = zarplata - 1
    p3 = p3 + 1
    # print(f"1 - {zarplata}")


print(f"{p25} купюр номиналом 25")
print(f"{p10} купюр номиналом 10")
print(f"{p3} купюр номиналом 3")
print(f"{p1} купюр номиналом 1")