# Импорт библиотек (sys читать ком. строку math считать)
import sys
import math

MAX_VALUE = 10000
text1_str = '     mathtool - решение уравнений вида A*x^2 + B*x + C = 0\n' \
    '\n' \
    '     Использование\n' \
    '\n' \
    '     python mathtool.py                              Вывод справки\n' \
    '     python mathtool.py --help                       Вывод справки\n' \
    '     python mathtool.py solve                        Ввод коэффицентов с клавиатуры\n' \
    '     python mathtool.py solve -a 1 -b -3 -c 2        Решение с заданными коэффцентами\n' \
    '\n' \
    'Коэффициенты A, B, C - целые числа и по модулю не превышают 10000'
# Вывод справки
if len(sys.argv) == 1:
    print(text1_str)
    sys.exit(0)

if sys.argv[1] == "--help":
    if len(sys.argv) == 2:
        print(text1_str)
        sys.exit(0)
    else:
        print("Ошибка: неверный набор параметров", file=sys.stderr)
        sys.exit(1)

if sys.argv[1] != "solve":
    print("Ошибка: неизвестная команда", file=sys.stderr)
    sys.exit(1)

# Получение данных от пользователя
if len(sys.argv) == 2:
    # Если прийдет mathtool solve
    a_str =input("Введите A:")
    b_str =input("Введите B:")
    c_str =input("Введите C:")

elif len(sys.argv) ==8:
    # Если прийдет mathtool solve -a 1 -b -3 -c 2
    if sys.argv[2] != "-a" or sys.argv[4] != "-b" or sys.argv[6] != "-c":
       print("Ошибка: неизвестный параметр", file=sys.stderr)
       sys.exit(1)
    a_str = sys.argv[3]
    b_str = sys.argv[5]
    c_str = sys.argv[7]
else:
    print("Ошибка: неверный набор параметров", file=sys.stderr)
    sys.exit(1)

# Перевод строки в число
try:
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)
except ValueError:
    print("Ошибка: коэффициент не является целым числом", file= sys.stderr)
    sys.exit(1)
# Проверка чтобы числа были в диапозоне 10000
if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
    print("Ошибка: значение вне диапaзона", file=sys.stderr)
    sys.exit(1)

# Математический блок 
if a == 0:
    if b != 0:
        print("Уравнение линейное")
        x = -c / b
        print (f"x = {int(x)}")
    else:
        print("Ошибка: это не уравнение", file=sys.stderr)
        sys.exit(1)
else:
    print("Уравнение квадратное")
    D = b * b - 4 * a * c
    print(f"D = {D}")
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"x1 = {x1:.3f}")
        print(f"x2 = {x2:.3f}")
    elif D == 0:
        x = -b / (2*a)
        print(f"x = {x}")
    else:
        print("Действительных корней нет")
