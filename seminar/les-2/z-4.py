# 4) Решить следующую задачу,, выводящиена экран "электронный таймер".
# Ставим таймер - часы, минуты, секунды.
# После отсчета срабатывает будильник


# Подключаем нужный модуль
import time

hour1 = int(input('hour = '))
min1 = int(input('min = '))
sec1 = int(input('sec = '))
sec_all = hour1*60*60 + min1 * 60 + sec1
for i in range(sec_all, 0, -1):
time.sleep(1)
print('all')






# print("О чём вам напомнить?")
# text = str(input())
# print("Через сколько минут?")
# local_time = float(input())
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)