import sys
import cli
from Calc import equation
from Calc import stats


#Обработка команды solve
def handle_solve(args):
    if args.a is None and args.b is None and args.c is None:
        # Ни одного параметра — ввод с клавиатуры
        try:
            a = int(input("Введите A: "))
            b = int(input("Введите B: "))
            c = int(input("Введите C: "))
        except ValueError:
            raise ValueError("коэффициент не является целым числом")
    elif args.a is not None and args.b is not None and args.c is not None:
        # Все три параметра заданы — берём из args
        a, b, c = args.a, args.b, args.c
    else:
        # Задана только часть — ошибка
        raise ValueError("укажите все три коэффициента либо ни одного")

    # Проверка диапазона и решение
    equation.check_coefficients({"A": a, "B": b, "C": c})
    kind, d, roots = equation.solve(a, b, c)

    # Вывод результата
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

    return 0


# Stats
def handle_stats(args):
    # Выбор источника: файл или стандартный ввод
    if args.input is not None:
        source = open(args.input, encoding="utf-8-sig")
    else:
        source = sys.stdin

    # Чтение чисел
    values = []
    try:
        for line in source:
            for word in line.split():
                try:
                    values.append(float(word))
                except ValueError:
                    raise ValueError(f"{word} не является числом")
    finally:
        if args.input is not None:
            source.close()

    # Проверки — в модуле
    stats.check_values(values)

    for label, function, form in stats.REPORT:
        value = function(values)
        if value is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{label}: {value:{form}}")

    return 0


#Заглушка
def handle_series(args):
    print("series: команда ещё не реализована", file=sys.stderr)
    return 1


#Заглушка
def handle_integrate(args):
    print("integrate: команда ещё не реализована", file=sys.stderr)
    return 1


HANDLERS = {
    "solve": handle_solve,
    "stats": handle_stats,
    "series": handle_series,
    "integrate": handle_integrate,
}


#Разбор параметров и выбор обработчика
def main(argv):
    parser = cli.build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    try:
        return HANDLERS[args.command](args)
    except (ValueError, OSError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))