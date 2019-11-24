import os
import keyboard
from datetime import datetime as dt


class NoMatch(Exception):
    pass


class LenNoMatch(NoMatch):
    pass


KEY = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
EOI = 'Ошибка ввода. '


def letter_encoder(letter, decoding):
    result = str(decoding.find(letter) + 1)
    if len(result) == 1:
        result = '0' + result
    return result


def exc_check(sequence, key):
    e = 0
    for letter in sequence:
        if not letter.lower() in key:
            print(EOI + 'Недопустимый символ: "{0:s}"'.format(letter))
            e += 1
    if e != 0:
        raise NoMatch


def full_name_input():
    while True:
        fam_name = input('Введите ТРИ первых буквы фамилии испытуемого: \n').lower()
        if len(fam_name) != 3:
            print(EOI + 'Требуются ТРИ первых буквы фамилии испытуемого.')
            continue
        try:
            exc_check(fam_name, KEY)
        except NoMatch:
            continue
        break

    while True:
        init = input('Введите ИО (инициалы) испытуемого без пробелов и точек: \n').lower()
        if len(init) != 2:
            print(EOI + 'Требуются ДВЕ буквы (Имя, Отчество).')
            continue
        try:
            exc_check(init, KEY)
        except NoMatch:
            continue
        break

    return fam_name, init


def dob_input():
    date = "----"
    while True:
        try:
            date = input('Введите день и месяц рождения испытуемого в формате ддмм: \n')
            if len(date) != 4:
                raise LenNoMatch
        except ValueError:
            print(EOI + 'Введите целое четырёхзначное ЧИСЛО без пробелов и точек.')
            continue
        except LenNoMatch:
            print(EOI + 'Требуется ЧЕТЫРЕ цифры без пробелов и точек.')
            continue
        else:  # Изёвая проверка корректности даты. Можно строже.
            if int(date[0:2]) < 1 or int(date[0:2]) > 31:
                print(EOI + 'Число месяца должо быть в диапазоне [1, 31].')
                continue
            if int(date[2:]) < 1 or int(date[2:]) > 12:
                print(EOI + 'Месяц должен быть в диапазоне [1, 12].')
                continue
        break

    return date


def report():
    encoded_id = ''
    init, fam_name = full_name_input()
    date = dob_input()
    for i in init + fam_name:
        encoded_id += letter_encoder(i, KEY)
    encoded_id += date + '0'  # Обсудить механизм для оценки последнего значения.

    print('Вы ввели фамилию: {!r}'.format(fam_name.upper()))
    print('Вы ввели инициалы: {!r}'.format(init.upper()))
    print('Вы ввели дату рождения: {!r}'.format(date))
    print('ID испытуемого согласно скрипту: {:s} \n '.format(encoded_id))
    print('Нажмите пробел для продолжения.')
    keyboard.wait('space')
    print('\n')

    return encoded_id


def visit_input():
    visit = 0
    while True:
        try:
            visit = int(input('Введите номер визита (от 1 до 3): \n'))
            if visit < 1 or visit > 3:
                print(EOI + 'Номер визита должен быть в диапазоне [1, 3]')
                continue
        except ValueError:
            print(EOI + 'Введите ЧИСЛО от 1 до 3.')
            continue
        break
    return visit


def main():
    encoded_id = report()
    visit = visit_input()
    os.chdir('C:/Users/Kirill/Desktop/Flanker_task/Logs/name_gen')
    start_time = dt.today()
    with open('name_list.log', 'a', encoding='utf-8') as f:
        f.write('\n' + encoded_id + '\t' + str(visit) + '\t' + start_time.strftime("%d_%m_%Y\t%H_%M_%S"))
    os.system('C:/Users/Kirill/Desktop/Flanker_task/Flanker_task.exp')


if __name__ == '__main__':
    main()
