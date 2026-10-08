import math

MIN_STEPS = 1
MAX_STEPS = 100000


#Подинтегральные функции
def F_ratio(x):
    return x / (x + 1)


def F_root(x):
    """F(x) = sqrt(x^2 + 1)."""
    return math.sqrt(x * x + 1)


#       Таблица функций
# Значение — кортеж:
#   (функция, текст формулы, нижняя граница, верхняя граница, замкнут_ли_промежуток)

FUNCTIONS = {
    "ratio": (F_ratio, "F(x) = x / (x + 1)", 0, 20, True),
    "root":  (F_root,  "F(x) = sqrt(x^2 + 1)", -5, 5, False),
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