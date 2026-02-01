from typing import Callable

class NoCorrectTime(Exception): pass

def S(func: Callable) -> Callable:
    def wrapper(*args) -> None:
        u0, u, t = args
        a = func(*args)
        s = u0 * t + (a * t ** 2) / 2
        print(f"{s=}")
    return wrapper

@S
def _1(u0: float, u: float, t: float) -> float:
    if t < 0:
        raise NoCorrectTime("Время должно быть больше 0")

    try:
        a = (u - u0) / t
    except TypeError as e:
        print(e)
        print("Переменные должны быть числами")
    except ZeroDivisionError as e:
        print(e)
        print("Время должно быть больше 0")
    else:
        print(f"{a=}")
        return a

def _2():
    winner = {
        "8": [0, []],
        "9": [0, []],
        "10": [0, []],
        "11": [0, []]

    }

    max_algebra = [0, []]
    max_geometry = [0, []]
    with open(file="111.txt") as f:
        for line in f:
            line = line.strip()
            line = line.split()
            secondname, firstname, klass, algebra, geometry = line
            algebra, geometry = int(algebra), int(geometry)
            summary_score = algebra + geometry
            if winner[klass][0] == summary_score:
                winner[klass][1].append(' '.join((secondname, firstname, summary_score)))
            elif winner[klass][0] < summary_score:
                winner[klass][0] = summary_score
                winner[klass][1].clear()
                winner[klass][1].append(' '.join((secondname, firstname)))

            if max_algebra[0] == algebra:
                max_algebra.append(' '.join((secondname, firstname, klass)))
            elif max_algebra[0] < algebra:
                max_algebra[0] = algebra
                max_algebra[1].clear()
                max_algebra[1].append(' '.join((secondname, firstname, klass)))

            if max_geometry[0] == geometry:
                max_geometry.append(' '.join((secondname, firstname, klass)))
            elif max_geometry[0] < geometry:
                max_geometry[0] = geometry
                max_geometry[1].clear()
                max_geometry[1].append(' '.join((secondname, firstname, klass)))

    print(f"{winner=}")
    print(f"{max_algebra=}")
    print(f"{max_geometry=}")

def main():
    _1(1, 10, 1)
    _2()

if __name__ == "__main__":
    main()
