# 3.3 Вводим любое слово\словочетание - определить, является ли оно палиндромом
# Задача с палиндромом.

string = input('Введите слово: ')
string =string.lower()
newString = ''

for i in range(len(string)-1, -1, -1):
    newString += string[i]

if string == newString:
    print('Это палиндром!')
else:
    print('Это не палиндром!')