# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.

import random
spisok=[]
for i in range(30):
      spisok.append(random.randint(0, 99))
print(spisok)

def spisok_sort(spisok):
    for i in range(len(spisok) - 1):
        m = i
        j = i + 1
        while j < len(spisok):
            if spisok[j] < spisok[m]:
                m = j
            j = j + 1
        spisok[i], spisok[m] = spisok[m], spisok[i]

spisok_sort(spisok)
print(spisok)