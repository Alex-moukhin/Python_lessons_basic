# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копиюазанного файла")
    print("rm <file_name> - удаляет указанный файл(запросить подтверждение операции")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def cp_file():
    if not f_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    path = os.path.realpath(f_name)
    try:
        with open(path, 'r', encoding='UTF-8') as f:
            li_lines = f.readlines()
        f.close()
    except FileNotFoundError:
        print('Не удается найти файл')
    n_path = path[:len(path) - len(f_name)] + str(path[:]).split('.')[0] + '_copy.' + str(path[-6:]).split('.')[1]
    print(n_path)
    c_file = open(n_path, 'w', encoding='UTF-8')
    for val in li_lines:
        c_file.write(val)
    c_file.close()
    print('файл {} скопирован'.format(f_name))


def rm_file():
    if not f_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    path = os.path.realpath(f_name)
    try:
        os.remove(f_name)
        print('файл {} удален'.format(f_name))
    except FileNotFoundError:
        print('Не удается найти файл')


def cd():
    if not p_name:
        print("Необходимо указать путь вторым параметром")
        return
    path = p_name
    try:
        os.chdir(path)
        print('директория изменена {} '.format(p_name))
    except FileNotFoundError:
        print('Не удается найти путь')


def ls():
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp_file,
    "rm": rm_file,
    "cd": cd,
    "ls": ls
    }

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    f_name = sys.argv[2]
except IndexError:
    f_name = None

try:
    p_name = sys.argv[2]
except IndexError:
    p_name = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")