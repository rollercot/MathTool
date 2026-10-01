# Импорт библиотек (sys читать ком. строку math считать)
import sys
from calc import equation

MAX_VALUE = 10000
text1_str = '     mathtool - решение уравнений вида A*x^2 + B*x + C = 0\n' \
    '\n' \
    '     Использование\n' \
    '\n' \
    '     python mathtool.py                              Вывод справки\n' \
    '     python mathtool.py --help                       Вывод справки\n' \
    '     python mathtool.py solve                        Ввод коэффициентов с клавиатуры\n' \
    '     python mathtool.py solve -a 1 -b -3 -c 2        Решение с заданными коэффциентами\n' \
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

#проверка диапазона и решение через модуль 
try:
    equation.check_coefficients({"A": a, "B": b, "C": c})
    kind, d, roots = equation.solve()
except ValueError as error:
    print(f"Ошибка: {error}", file=sys.stderr)
    sys.exit(1)

#Вывод результата
if kind == "линейное":
    print("Уравнение линейное")
else:
    print("Уравнение квадратное")

if d is not None:
    print(f"D = {d}")

if not roots:
    print("Действительных корней нет")
elif len(roots) == 1:
    print(f"x = {roots[0]:.3f}")
else:
    print(f"x1 = {roots[0]:.3f}")
    print(f"x2 = {roots[1]:.3f}")
