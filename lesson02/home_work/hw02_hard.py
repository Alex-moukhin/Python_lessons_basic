# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

equation = 'y = -12x + 11111140.2121'
x = 2.5
equation = equation.split(' ')
equation[2] = equation[2].split('x')
equation[0] = float(equation[2][0])*x + float(equation[4])
print(equation[0])

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

date = date.split('.')
day = date[0]
month = date[1]
year = date[2]

# 1. функция определения дней в месяце
def day_in_month(month):
    month_31 = [1,3,5,7,8,10,12]
    month_30 = [4,6,9,11]
    month_29 = [2]
    if month in month_31:
        return '31'
    elif month in month_30:
        return '30'
    elif month in month_29:
        return '29'
    else:
        return 'Номер месяца указан не верно'
    
# 2. Проверяем верно ли указан формат даты: дни - 2 числа, месяц - 2 числа, год - 4 числа.
if len(day) == 2 and len(month) == 2 and len(year) == 4:
# 3. Проверяем попадает ли год в верный диапазон
    if int(year) > 1 and int(year) < 9999: 
# 4. четыре проверки месяца и даты, для определения кол-ва дней в месяце
        if day_in_month(int(month)) == '30':
            if int(day) > 0 and int(day) <=30:
                print(f'Формат даты {day}' '.' f'{month}' '.' f'{year} ' 'указан верно')
            else:
                print('Колличество дней не соответстует месяцу')
        elif day_in_month(int(month)) == '31':
            if int(day) > 0 and int(day) <=31:
                print(f'Формат даты {day}' '.' f'{month}' '.' f'{year} ' 'указан верно')
            else:
                print('Колличество дней не соответстует месяцу')
        elif day_in_month(int(month)) == '29':
            if int(day) > 0 and int(day) <=29:
                print(f'Формат даты {day}' '.' f'{month}' '.' f'{year} ' 'указан верно')
            else:
# закрываем проверку по дням
                print('Колличество дней не соответстует месяцу')    
# закрываем проверку по месяцам
        else:
            print('Номер месяца указан не верно')
# закрываем проверку по году
    else:
        print('Год указан не верно')
# закрываем проверку форматов
else:
    print('Неверный формат даты')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
