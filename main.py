def question1(*args: int) -> int:
    """Решение задания 1"""
    return sum(args) // len(args)


def question2(x: int, y: int) -> int:
    """Решение задания 2"""
    return x // y, x % y


def question3(r: int, x: float) -> float|int:
    """Решение задания 3"""
    if r < 0:
        raise Exception("Первый аргумент должен быть больше или равен нулю.")
    if r:
        return round(x, r)
    else:
        return int(x)


def question4(x: int) -> int:
    """Решение задания 4"""
    return int(str(abs(x))[::-1])


def question5(x: int) -> int:
    """Решение задания 5"""
    if 32 < x.__sizeof__():
        return 0
    return qestion4(x)


if __name__ == '__main__':
    print('\n Задание 1:', question1(52, 56, 60))
    print('\n Задание 2:', question2(9, 2))
    print('\n Задание 3:', question3(2, 14.721))
    print('\n Задание 4:', question4(123))
    print('\n Задание 5:', question5(1245163476234786782))
