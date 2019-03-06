# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os, re, sys, shutil
# Скрипт создания дирректорий

def make_dir(dir_num):
    a = 1
    b = dir_num + a
    dir_name =[]
    for i in range(a,b):
        dirs = 'dir_'+str(i)
        os.makedirs(dirs)
        dir_name.append(dirs)
    return print(f'Папки удачно созданы: {dir_name}')
# запуск скрипта:
#make_dir(5)

# скрипт удаления созданных папок
def dir_del(dirs):
    dirs = ' '.join(dirs)
    dirs_string = re.findall(r'\w\w\w_\d', dirs)
    if dirs_string == []:
        print('В текущей дирректории нет папок формата dir_n')
    else:
        for i in dirs_string:
            os.rmdir(i)
        print(f'Папки удачно удалены: {dirs_string}')

# запуск скрипта
#dirs = os.listdir()
#dir_del(dirs)



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
# СкриптЖ
def show_dirs(data):
    dir_list = []
    for i in data:
        if os.path.isdir(i) == True:
            dir_list.append(i)
    return print(f'Список папок в данной дирректории: {dir_list}')

# запуск скриптаЖ
#data = os.listdir()
#show_dir(data)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(file_way):
    file_way_string = file_way.split('/')
    file = file_way_string[-1]
    new_file = 'new_' + file
    shutil.copy(file, new_file)
    return print(f'Файл удачно скопирован: {new_file}')

#file_way = sys.argv[0]
#copy_file(file_way)

