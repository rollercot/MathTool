from Calc import series
import argparse


#Разбор параметров командной строки
def build_parser():
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="mathtool - программа для расчета уравнений и числовых последовательностей",
        allow_abbrev=False,
    )
    sub = parser.add_subparsers(dest="command")

    #               solve
    p = sub.add_parser("solve", help="Решение уравнения A*x^2 + B*x + C = 0", allow_abbrev=False)
    p.add_argument("-a", type=int, help="Коэффициент A")
    p.add_argument("-b", type=int, help="Коэффициент B")
    p.add_argument("-c", type=int, help="Коэффициент C")

    #               stats
    p = sub.add_parser("stats", help="Показатели последовательности", allow_abbrev=False)
    p.add_argument("--input", type=str, help="Имя файла с числами")

    #               series
    p = sub.add_parser("series", help="Сумма ряда", allow_abbrev=False)
    p.add_argument("--func", type=str, required=True,choices=sorted(series.FORMULAS),help="Имя ряда")
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--terms", type=int, help="Количество слагаемых")
    group.add_argument("--eps", type=float, help="Точность")

    #               inregrate
    p = sub.add_parser("integrate", help="Численное интегрирование", allow_abbrev=False)
    p.add_argument("--func", type=str, required=True, help="Имя функции")
    p.add_argument("--from", dest="start", type=float, required=True, help="Нижний предел")
    p.add_argument("--to", type=float, required=True, help="Верхний предел")
    p.add_argument("--steps", type=int, required=True, help="Число шагов")


    return parser