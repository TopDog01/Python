# Задача. Решение в группах. Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа не должна быть линейной

from csv import DictWriter, DictReader
from os.path import exists


class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_data():
    flag = False
    while not flag:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Слишком короткое имя")
            last_name = input("Введите фамилию: ")
            if len(last_name) < 5:
                raise NameError("Слишком короткая фамилия")
            phone = input("Введите номер телефона: ")
            if len(phone) < 11:
                raise NameError("Номер телефона должен быть не менее 11 символов")
        except NameError as err:
            print(err)
        else:
            flag = True

    return [first_name, last_name, phone]


def create_file(filename):
    with open(filename, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)


def write_file(filename, lst):
    res = read_file(filename)
    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res.append(obj)
    standard_write(filename, res)


def row_search(filename):
    last_name = input("Введите фамилию: ")
    res = read_file(filename)
    for row in res:
        if last_name == row['Фамилия']:
            return row
    return "Запись не найдена"


def delete_row(filename):
    row_number = int(input("Введите номер строки: "))
    res = read_file(filename)
    res.pop(row_number - 1)
    standard_write(filename, res)


def standard_write(filename, res):
    with open(filename, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)


def change_row(filename):
    row_number = int(input("Введите номер строки: "))
    res = read_file(filename)
    data = get_data()
    res[row_number - 1]["Имя"] = data[0]
    res[row_number - 1]["Фамилия"] = data[1]
    res[row_number - 1]["Телефон"] = data[2]
    standard_write(filename, res)

def copy_row(src_filename, dest_filename):
    row_number = int(input("Введите номер строки для копирования: "))
    res = read_file(src_filename)
    row = res[row_number - 1]

    if not exists(dest_filename):
        create_file(dest_filename)

    dest_data = read_file(dest_filename)
    dest_data.append(row)
    standard_write(dest_filename, dest_data)

filename = 'phone.csv'
filename2 = 'phone2.csv'


def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":
            break
        elif command == "w":
            if not exists(filename):
                create_file(filename)
            write_file(filename, get_data())
        elif command == "r":
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            print(read_file(filename))
        elif command == "f":
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            print(row_search(filename))
        elif command == "d":
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            delete_row(filename)
        elif command == "c":
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            change_row(filename)
        elif command == "copy":
            if not exists(filename):
                print("Файл не существует. Создайте его.")
                continue
            copy_row(filename, filename2)



main()