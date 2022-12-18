# 3.12 Вводим с клаиватуры строку. Необходимо вывести строку,
# где развернём подстроку между первой и последней буквой "о" из исходной строки. Если она только одна или её нет -
# то сообщить, что буква "о" - одна или не встречается.




# изменить строку к одному регистру
# проверить есть ли "o" в строке,
# получить индексы нахождения
# найти самые отдаленные "О" от друг друга
# развернуть символы

def reverse_string_select(text: str, letter):
    start = text.find(letter)
    end = text.rfind(letter)
    if start == -1: return (f'Здесь  нет букв "{letter}"')
    elif start == end: return (f'Здесь только одна буква  "{letter}"')
    else: return text[0:start] + text[end:start:-1] + text[end:len(text)]

text = input('ВВедите ваш текст: ')
print(reverse_string_select(text.lower(), 'o'))
