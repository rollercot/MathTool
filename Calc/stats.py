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