import os
import keyboard
from datetime import datetime as dt

class Nomatch(Exception):
    pass

class LenNoMatch(Nomatch):
    pass

key = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
fam_name = ''
init = ''
date = ''
EOI = 'Ошибка ввода. '

def letter_encoder(letter, decoding):
    result = str(decoding.find(letter) + 1)
    if len(result) == 1:
        result = '0' + result
    return result

def exc_check(queue, key):
    e = 0
    for lett in queue:
        if not lett.lower() in key:
            print(EOI + 'Недопустимый символ: "{0:s}"'.format(lett))
            e += 1
    if e != 0:
        raise Nomatch

while True:
    fam_name = input('Введите ТРИ первых буквы фамилии испытуемого: \n')
    if len(fam_name) != 3:
        print(EOI + 'Требуются ТРИ первых буквы фамилии испытуемого.')
        continue
    try:
        exc_check(fam_name, key)
    except Nomatch:
        continue
    break

while True:
    init = input('Введите ИО (инициалы) испытуемого без пробелов и точек: \n')
    if len(init) != 2:
        print(EOI + 'Требуются ДВЕ буквы (Имя, Отчество).')
        continue
    try:
        exc_check(init, key)
    except Nomatch:
        continue
    break

while True:
    try:
        date = input('Введите день и месяц рождения испытуемого в формате ддмм: \n')
        temp = int(date)
        if len(date) != 4:
            raise LenNoMatch
    except ValueError:
        print(EOI + 'Введите целое четырёхзначное ЧИСЛО без пробелов и точек.')
        continue
    except LenNoMatch:
        print(EOI + 'Требуется ЧЕТЫРЕ цифры без пробелов и точек.')
        continue
    else: # Изёвая проверка корректности даты. Можно строже.
        if int(date[0:2]) < 1 or int(date[0:2]) > 31:
            print(EOI + 'Число месяца должо быть в диапазоне [1, 31].')
            continue
        if int(date[2:]) < 1 or int(date[2:]) > 12:
            print(EOI + 'Месяц должен быть в диапазоне [1, 12].')
            continue
    break

encoded_id = ''
for i in fam_name + init:
    encoded_id += letter_encoder(i, key)
encoded_id += date + '0' # Обсудить механизм для оценки последнего значения.

print('Вы ввели фамилию: {!r}'.format(fam_name.upper()))
print('Вы ввели инициалы: {!r}'.format(init.upper()))
print('Вы ввели дату рождения: {!r}'.format(date))
print('ID испытуемого согласно скрипту: {:s} \n '.format(encoded_id))
print('Нажмите пробел для продолжения.')
keyboard.wait('space')
print('\n')
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

start_time = dt.today()

os.chdir('C:/Users/Kirill/Desktop/Flanker_task/Logs/name_gen')
with open('name_list.log', 'a', encoding='utf-8') as f:
    f.write('\n' + encoded_id + '\t' + str(visit) + '\t' + start_time.strftime("%d_%m_%Y\t%H_%M_%S"))
os.system('C:/Users/Kirill/Desktop/Flanker_task/Flanker_task.exp')