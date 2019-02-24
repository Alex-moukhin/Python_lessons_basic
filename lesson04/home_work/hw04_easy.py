# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

from random import randint

def lists(a, n):
    b = []
    result = []
    for i in range(a, n):
        b.append(randint(a, n))
    for val in b:
        val = val**2
        result.append(val)
    return (f'Список случайных чисел: {b} Список квадратов случайных чисел: {result}')
lists = lists(4, 20)
lists

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# формируем лист с названием фруктов
with open('fruits.txt',encoding='utf-8') as inp_ut:
# записываем строки из файла в line
    line = inp_ut.readlines()
# убираем пробелы в строках
    line = list(filter(lambda x: x!='\n', line))
# убираем артефакт \n из всех слов
    line = [line.rstrip() for line in line]

# итоговый словарь
fruits_return = []
# словари с фркутами 1 и 2
fruits_list_1 = line[50:55]
fruits_list_2 = line[52:57]
print(f'Список фруктов 1: {fruits_list_1}')
print(f'Список фруктов 2: {fruits_list_2}')
# алгоритм определения 
for fruits in fruits_list_1:
    for fruits2 in fruits_list_2:
        if fruits == fruits2:
            fruits_return.append(fruits)
print(f'Список фруктов, которые есть в списке 1 и 2: {fruits_return}')

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


from random import randint
# исходные данные
a = 5
n = a+10
b = []
result = []
# формируем список случайных чисел
for i in range(a, n):
    b.append(randint(a, n))
print(f'Дан список из {n-a} случайных чисел: {b}')
# выполняем проверку по условиям задачи
for val in b:
    if val%3==0 and val>0 and val%4!=0:
        result.append(val)
print(f'Из данного списка {len(result)} удовлетворяет условиям (кратно трем, больше 0 и не кратно 4): {result}')
