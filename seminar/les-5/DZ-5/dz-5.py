from numpy import zeros
from random import randint

print('Задайте размеры игрового поля : ')
x, y = int(input()), int(input())
map = zeros([x, y])
print(f'Игровое поле: \n{map}')
x1, y1 = randint(0, x - 1), randint(0, y - 1)
map[x1][y1] = 1
gamer_map = zeros([x, y])
print()


def player(x1, y1):
    print('Ваш ход \n Введите номер строки ')
    row = int(input()) - 1
    print('Номер столбца ')
    column = int(input()) - 1
    if row == x1 and column == y1:
        print('Убил!')
        return False
    elif row + 1 > x or column + 1 > y:
        print('Координаты вне поля')
        return True
    else:
        print('Мимо')
        return True




while True:
    if not player(x1, x1):
        print('You win')
        break
