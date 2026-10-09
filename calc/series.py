#Суммирование числовых рядов
MAX_TERMS = 10000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100000


#Знак n-го слагаемого: +1 для нечётных, -1 для чётных
def sign(n):
    if n % 2 == 0:
        return -1
    return 1


#Слагаемое ряда sqplus: 1/(n^2 + 1) со знаком
def term_sqplus(n):
    return sign(n) / (n * n + 1)


#Слагаемое ряда third: 1/(3n) со знаком
def term_third(n):
    return sign(n) / (3 * n)


def term_ncube(n):
    """Слагаемое ряда ncube: n / (n^3 + n - 1) со знаком."""
    return sign(n) / (n ** 3 - 12)

#       Таблица рядов
# Ключ — имя из командной строки.
# Значение — пара (функция слагаемого, текст формулы).

FORMULAS = {
    "sqplus": (term_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
    "third":  (term_third,  "S = 1/3 - 1/6 + 1/9 - 1/12 + ..."),
    "ncube": (term_ncube, "S = 1/(1^3+0) - 2/(2^3+1) + 3/(3^3+2) - ..."),
}


#       Циклы суммирования


#Сумма первых count слагаемых. term(n) даёт n-е слагаемое
def sum_by_terms(term, count):
    result = 0
    for n in range(1, count + 1):
        result += term(n)
    return result


#Сумма ряда до достижения точности eps

def sum_by_eps(term, eps):
    result = 0
    n = 0
    while True:
        n += 1
        value = term(n)
        result += value
        if abs(value) < eps:
            return result, n
        #Valueerror если достигнут лимит повторений
        if n >= MAX_ITERATIONS:
            raise ValueError("точность не достигнута")