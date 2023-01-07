# Сделать программу расписание - делаем расписание занятий\тренировок или что-то своё.
# Для хранения информации используем текстовые файлы (сохраняем, перезаписываем в них и т.д.) , бесконечный цикл, функции и прочий функционал.
# Программа будет, как консольный бот, который будет нас спрашивать что и как нужно сделать - вывести, показать, перезаписать , добавить событие в определенный день недели


# что я хочу получить:
# кабинет 1 - 1А - Алгебра
# кабинет 2 - 2Б - Физика
# кабинет 3 - 3В - Информатика
# кабинет 4 -
# кабинет 5 -

kabinet = {1: "кабинет -1", 2: "кабинет -2", 3: "кабинет -3", 4: "кабинет -4", 5: "кабинет -5"}

predmet = {1: "Алгебра", 2: "Физика", 3: "Биология", 4: "Информатика", 5: "Физика", 6: "Химия", 7: "Литература",
           8: "Геометрия", 9: "Труд", 10: "Изображение"}

klass = {1: "1А", 2: "2Б", 3: "3В"}

day = {1: "Пн.txt", 2: "Вт.txt", 3: "Ср.txt", 4: "Чт.txt", 5: "Пт.txt", 6: "Сб.txt", 7: "Вс.txt"}

# change_day = int(input("Введите день недели который вас интересует( от 1 до 7)"))
# while change_day < 1 or change_day > 7:
#     change_day = int(input("Такого дня недели не существует. Введите день недели( от 1 до 7)\n Введите цифру: "))
# # Печатаем весь день:
# with open(day[change_day], "r", encoding="utf-8") as my_day:
#     print(my_day.readlines())
later =" "
while later !="":
    change_day = int(input("Введите день недели который вас интересует( от 1 до 7)"))
    while change_day < 1 or change_day > 7:
        change_day = int(input("Такого дня недели не существует. Введите день недели( от 1 до 7)\n Введите цифру: "))
    # Печатаем весь день:
    with open(day[change_day], "r", encoding="utf-8") as my_day:
        print(my_day.readlines())

    change_items = int(input(
        "Что вы хотите сделать с этим  днем?   \n 1. Изменить \n 2. Добавить Класс/Урок/Мероприятие\n Введите цифру: "))

    if change_items == 1:
        with open(day[change_day], "r+", encoding="utf-8") as read_day:
            later = ""
            while later == "":
                print(kabinet.items())
                line_kabinet = int(input("Введите цифру соотвествующего кабинет: "))
                print(klass.items())
                line_klass = int(input("Введите цифру соотвествующего класс:  "))
                print(predmet.items())
                line_predmet = int(input("Введите цифру соотвествующего предмета: "))
                st = read_day.readlines()[line_kabinet]
                text = (f"{kabinet.setdefault(line_kabinet)} - {klass.setdefault(line_klass)} - {predmet.setdefault(line_predmet)}")
                new_read_day = read_day.replace(st,text)
                read_day=new_read_day

                # read_day.writelines(f"{kabinet.setdefault(line_kabinet)} - {klass.setdefault(line_klass)} - {predmet.setdefault(line_predmet)}")
                later = input("Enter - перезаписать другое значение, любой символ возврат в меню")

    #
    #
    #        если добавить меропритие:
    #                 выберите свободный кабинет
    #                     что за мероприятие там будет проходить?
    #                         записываем информацию
    # #
    #
#
#
#
#
