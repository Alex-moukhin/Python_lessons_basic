# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

'''
не хватило врвмени ((( 
'''

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import re
# составляем лист из файла workers
data_workers = []
workers = open('workers.txt', 'r', encoding='utf-8')
for line in workers:
    data_workers.append(re.findall(r'[А-я]+[_]?[А-я]+|[0-9]+', line))
workers.close()
# удаялем заголовок таблицы
del data_workers[0]

# составляем лист из файла hours
hours = open('hours_of.txt', 'r', encoding='utf-8')
data_hours = []
for line in hours:
    data_hours.append(re.findall(r'[А-я]+[_]?[А-я]+|[0-9]+', line))
hours.close()
# удаялем заголовок таблицы
del data_hours[0]

# создаем файл, куда будем записывать результат
result_salary = open('result_salary.txt', 'w', encoding='utf-8')
result_salary.write('Имя Фамилия Заработанная плата')
'''
Алгоритм расчета:
1. Добавляем переменные, в которые записываем имя и фамилию
2. Проводим сравнение в двух листах и сопоставляем строчки с данными
3. Добавляем переменные, обозначая данные из разных файлов
4. Прописываем алгоритм расчета зарпалаты согласно заданию
5. Записываем результат расчета зарплат в файл

'''
for i in data_workers:
    name_workers = i[0]
    surname_workers= i[1]
    for n in data_hours:
        name_in_data_hours = n[0]
        surname_in_data_hours = n[1]
        if name_workers == name_in_data_hours and surname_workers == surname_in_data_hours:
            salary = int(i[2])
            hours_norm = int(i[4])
            hours_fact = int(n[2])
            work = hours_fact - hours_norm
            if work > 0:
                price = salary + (2 * (salary / hours_norm) * (hours_work - hours_norm))
            else:
                price = salary + (salary / hours_norm) * (hours_work - hours_norm)
            # записываем в файл квитанции
            person_data = '{0} {1} {2:.2f}\n'.format(name_workers,
                                                  surname_workers,
                                                  price)
            result_salary.write(person_data)
            print(person_data.strip())
result_salary.close()
print('Зарплатная ведомость сформирована в файле - result_salary.txt')


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

fruits_dict = dict()
with open('fruits.txt',encoding='utf-8') as inp_ut: 
# записываем строки из файла в line
    line = inp_ut.readlines()
# убираем пробелы в строках
    line = list(filter(lambda x: x!='\n', line))
    for normal_line in line:
# записываем словарь со списом названий файлов и значениями, соответствующий первым буквам слов
        file_name = 'fruits_{}'.format(normal_line[0].upper())
        fruits_dict[file_name] = fruits_dict.get(file_name,'')+normal_line
    
# цикл записи файла
for i in fruits_dict:
# записываем в переменную формат названия файла
    name = '{}.txt'.format(i)
# открываем файл на зпись
    with open(name,'w') as out:
# записываем значения из словаря в файл
        out.write(fruits_dict[i])
print('Формирование файлов по именам фруктов закончено!')
