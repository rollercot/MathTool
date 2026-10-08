
#Решение уравнений типа A*x^2+B*x+C = 0.

import math

MAX_VALUE = 10000 

#Проверка что коэффициент не больше MAX_VALUE   
def check_coefficients(coefficients):
    for name, value in coefficients.items():
        if abs(value) >  MAX_VALUE:
            raise ValueError(f"Коэффициент {name} вне допустимого диапазона")


#Решение самого уравнения 
def solve (a,b,c):
    if a == 0:
        if b == 0:
            raise ValueError("Это не уравнение, неизвестное отсутвует")
        return "линейное", None, [-c / b]

    d = b * b - 4 * a * c 
    
    if d > 0:
        return "квадратное", d, [
            (-b + math.sqrt(d)) / (2 * a),
            (-b - math.sqrt(d)) / (2 * a),
    ]
    if d == 0:
        return "квадратное", d, [-b / (2 * a)]
    return "квадратное", d, []
