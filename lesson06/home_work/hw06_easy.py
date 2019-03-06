# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
# фунция для определения длинны линии
        def line(top1, top2):
            return math.sqrt((top1[0]-top2[0])**2 + (top1[1]-top2[1])**2)
#определяем длинны гранией треугольника
        self.ab = line(self.a, self.b)
        self.bc = line(self.b, self.c)
        self.ca = line(self.c, self.a)
# определение площади треугольника
    def triangle_s(self):
        p = (self.ab + self.bc + self.ca)/2
        return math.sqrt(p*(p-self.ab)*(p-self.bc)*(p-self.ca))
# определение высоты треугольника

    def triangle_h(self):
        return self.triangle_s()*2/self.ca
# определяем периметр
    def triangle_p(self):
        return self.ab + self.bc + self.ca

# Ввоодим координаты
trin = Triangle((25, 15), (18, 22), (32, 56))
print(f'Площадь треугольника равна {round(trin.triangle_s())}')
print(f'Высота треугольника равна {round(trin.triangle_h())}')
print(f'Периметр треугольника равен {round(trin.triangle_p())}')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
# фунция для определения длинны линии
        def line(top1, top2):
            return math.sqrt((top1[0] - top2[0]) ** 2 + (top1[1] - top2[1]) ** 2)

# определяем диагонали для проверки на равнобедренную тропецию
        self.ac = line(self.a, self.c)
        self.bd = line(self.b, self.d)
# определяем длинну гранией
        self.ab = line(self.a, self.b)
        self.bc = line(self.b, self.c)
        self.cd = line(self.c, self.d)
        self.da = line(self.d, self.a)
# расчет высоты трапеции
        self.h = math.sqrt(self.ab**2 - ((self.da-self.bc)**2/4))
# расчет площади чере высоту
        self.s = (self.h*(self.da-self.bc))/2
# проверка - является ли это равнобедренной трапецией
    def check(self):
        if self.ac != self.bd:
            return 'Это не равнобедренная тропеция'
        else:
            return True
# определяем грани
    def face(self):
        return (f'Грань AB = {round(self.ab)}, грань BC = {round(self.bc)}, '
                f'грань CD = {round(self.cd)}, грань DA = {round(self.da)}')

    def p(self):
        return self.ab + self.bc + self.cd +self.da


trap = Trapeze((10, 20), (20, 40), (30, 40), (40, 20))
if trap.check() == True:
    print(trap.face())
    print(f'Периметр трапеции равен: {(round(trap.p()))}')
    print(f'Площадь трапеции равна {round(trap.s)}')
else:
    print('Это не равнобедренная тропеция')
