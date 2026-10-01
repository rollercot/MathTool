
#Решение уравнений типа A*x^2+B*x+C = 0.

import math

MAX_VALUE = 10000 

#Проверка что коэффициент не больше MAX_VALUE   
def check_coefficients(coefficients):
    for name, value in coefficients.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(F"Коэффициент {name} вне допустимного диапазаона")


#Решение уравнения
def solve(a, b, c):
    if a == 0:
        if b == 0:
            raise ValueError("это не уравнение, неизвестное отсутсвует")
        return "линейное", None, [-c / b]

    d = b * b - 4 * a * c
    if d > 0 : 
        return "Квадратное", d, [(-b + math.sqrt()) / (2 * a),(-b - math.sqrt(d)) / (2 * a)]
    if d == 0:
        return "Квадратное". d , [-b / (2 * a)]
    return "квадратное", d, []

