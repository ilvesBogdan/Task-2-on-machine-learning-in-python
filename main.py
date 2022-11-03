def qestion1(*args: int) -> int:
    """Решение задания 1"""
    return sum(args) // len(args)


def qestion2(x: int, y: int) -> int:
    """Решение задания 2"""
    return x // y, x % y


def qestion3(r: int, x: float) -> float|int:
    """Решение задания 3"""
    if r < 0:
        raise Exception("Первый аргумент должен быть больше или равен нулю.")
    if r:
        return round(x, r)
    else:
        return int(x)


def qestion4(x: int) -> int:
    """Решение задания 4"""
    return int(str(x)[::-1])


def qestion5(x: int) -> int:
    """Решение задания 5"""
    if 32 < x.__sizeof__():
        return 0
    return qestion4(x)


if __name__ == '__main__':
    print('\n Задание 1:', qestion1(52, 56, 60))
    print('\n Задание 2:', qestion2(9, 2))
    print('\n Задание 3:', qestion3(2, 14.721))
    print('\n Задание 4:', qestion4(123))
    print('\n Задание 5:', qestion5(1245163476234786782))
