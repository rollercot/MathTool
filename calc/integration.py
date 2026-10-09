import math
from calc import equation
MIN_STEPS = 1
MAX_STEPS = 100000

_,_,x = equation.solve(-1,1,1)
#Подинтегральные функции
def F_ratio(x):
    return x / (x + 1)


def F_root(x):
    """F(x) = sqrt(x^2 + 1)."""
    return math.sqrt(x * x + 1)


def F_test(x):
    """F(x) = 1/√(3x + 2)"""
    return -x ** 2 + x +1


#       Таблица функций
# Значение — кортеж:
#   (функция, текст формулы, нижняя граница, верхняя граница, замкнут_ли_промежуток)

FUNCTIONS = {
    "ratio": (F_ratio, "F(x) = x / (x + 1)", 0, 20, True),
    "root":  (F_root,  "F(x) = sqrt(x^2 + 1)", -5, 5, False),
    "test":   (F_test, "F(x) = 1/√(3x + 2)", x[0], x[1],True)
}


#       Интегрирование
#Значение интеграла функции f на [a, b] за steps шагов
def integrate(f, a, b, steps):
    dx = (b - a) / steps
    result = 0
    for i in range(steps):
        x = a + i * dx
        result += f(x) * dx
    return result