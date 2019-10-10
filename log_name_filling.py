import os
import keyboard

class Nomatch(Exception):
    pass

class LenNoMatch(Nomatch):
    pass

code = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
fam_name = ''
init = ''
date = ''

def letter_encoder(letter, decoding):
    result = str(decoding.find(letter) + 1)
    if len(result) == 1:
        result = '0' + result
    return result

def exc_check(queue, code):
    e = 0
    for lett in queue:
        if not lett.lower() in code:
            print('Ошибка ввода. Недопустимый символ: "{0:s}"'.format(lett))
            e += 1
    if e != 0:
        raise Nomatch

while True:
    fam_name = input('Введите ТРИ первых буквы фамилии испытуемого: \n')
    if len(fam_name) != 3:
        print('Ошибка ввода. Требуются ТРИ первых буквы фамилии испытуемого.')
        continue
    try:
        exc_check(fam_name, code)
    except Nomatch:
        continue
    break

while True:
    init = input('Введите ИО (инициалы) испытуемого без пробелов и точек: \n')
    if len(init) != 2:
        print('Ошибка ввода. Требуются ДВЕ буквы (Имя, Отчество).')
        continue
    try:
        exc_check(init, code)
    except Nomatch:
        continue
    break

while True:
    try:
        date = input('Ведите день и месяц рождения испытуемого в формате ддмм: \n')
        temp = int(date)
        if len(date) != 4:
            raise LenNoMatch
    except ValueError:
        print('Ошибка ввода. Введите целое четырёхзначное ЧИСЛО без пробелов и точек.')
        continue
    except LenNoMatch:
        print('Ошибка ввода. Требуется ЧЕТЫРЕ цифры без пробелов и точек.')
        continue
    else:
        if int(date[0:2]) < 1 or int(date[0:2]) > 31:
            print('Ошибка ввода. День месяца должен быть в диапазоне [1, 31]')
            continue
        if int(date[2:]) < 1 or int(date[2:]) > 12:
            print('Ошибка ввода. Месяц должен быть в диапазоне [1, 12]')
            continue
    break

encoded_id = ''
for i in fam_name + init:
    encoded_id += letter_encoder(i, code)
encoded_id += date + '0' # Обсудить механизм для оценки последнего значения.

print('Вы ввели фамилию: {!r}'.format(fam_name.upper()))
print('Вы ввели инициалы: {!r}'.format(init.upper()))
print('Вы ввели дату рождения: {!r}'.format(date))
print('ID испытуемого согласно скрипту: {:s} \n '.format(encoded_id))
print('Нажмите пробел для продолжения')
keyboard.wait('space')

os.chdir('C:/Users/Kirill/Desktop/Flanker_task/Logs/name_gen')
with open('name_list.log', 'a', encoding='utf-8') as f:
    f.write('\n' + encoded_id)
os.system('C:/Users/Kirill/Desktop/Flanker_task/Flanker_task.exp')