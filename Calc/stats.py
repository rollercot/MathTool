#Числовая последовательность
import math

MAX_COUNT = 20
MAX_ABS = 10000

#Проверка чисел: длина конечность диапазон
def check_values(values):
    if len(values) == 0:
        raise ValueError("последовательность пуста")
    if len(values) > MAX_COUNT:
        raise ValueError(f"чисел больше {MAX_COUNT}")
    for value in values:
        if not math.isfinite(value):
            raise ValueError(f"значение {value} не является конечным")
        if abs(value) > MAX_ABS:
            raise ValueError(f"значение {value} вне допустимого диапазона")


#Сумма чисел последовательности
def total(values):
    result = 0
    for value in values:
        result += value
    return result


#Среднее арифметическое
def mean(values):
    return total(values) / len(values)


#Сумма квадратов
def sum_squares(values):
    result = 0
    for value in values:
        result += value ** 2
    return result


#Среднее квадратическое
def rms(values):
    return math.sqrt(sum_squares(values) / len(values))


#Сумма квадратов отклонений от среднего
def sum_squared_deviations(values):
    average = mean(values)
    result = 0
    for value in values:
        result += (value - average) ** 2
    return result


#Дисперсия: сумма квадратов отклонений / N
def variance(values):
    return sum_squared_deviations(values) / len(values)


#СКО: корень из дисперсии
def std_dev(values):
    return math.sqrt(variance(values))


#Стандартное отклонение (по N-1). None, если чисел меньше двух
def sample_std(values):
    if len(values) < 2:
        return None
    return math.sqrt(sum_squared_deviations(values) / (len(values) - 1))


#Наименьшее число
def minimum(values):
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result


#Наибольшее число
def maximum(values):
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result


#Количество положительных чисел
def count_positive(values):
    result = 0
    for value in values:
        if value > 0:
            result += 1
    return result


#Количество отрицательных чисел
def count_negative(values):
    result = 0
    for value in values:
        if value < 0:
            result += 1
    return result


#       Таблица показателей
# Каждая строка: (подпись, функция, формат)

REPORT = [
    ("Количество",     len,                     "d"),
    ("Сумма",          total,                   ".3f"),
    ("Ср. арифм.",     mean,                    ".3f"),
    ("Сумма кв.",      sum_squares,             ".3f"),
    ("Ср. кв.",        rms,                     ".3f"),
    ("Дисперсия",      variance,                ".3f"),
    ("СКО",            std_dev,                 ".3f"),
    ("Станд. откл.",   sample_std,              ".3f"),
    ("Наименьшее",     minimum,                 ".3f"),
    ("Наибольшее",     maximum,                 ".3f"),
    ("Положительных",  count_positive,          "d"),
    ("Отрицательных",  count_negative,          "d"),
]