prog = []


def solve(filename):
    global prog
    with open(filename) as f:
        for row in f:
            prog = list(map(int, row.split(",")))
    i = 0
    while 0 <= i < len(prog):
        i = calc(i)
    return prog


def calc(i):
    global prog
    # print(f"Calc: {i}")
    op = prog[i] % 100
    mode1 = prog[i] % 1000 // 100
    mode2 = prog[i] % 10000 // 1000

    if op == 1:
        prog[prog[i + 3]] = get_value(i + 1, mode1) + get_value(i + 2, mode2)
        return i + 4
    elif op == 2:
        prog[prog[i + 3]] = get_value(i + 1, mode1) * get_value(i + 2, mode2)
        return i + 4
    elif op == 3:
        data = int(input())
        prog[prog[i + 1]] = data
        return i + 2
    elif op == 4:
        print(get_value(i + 1, mode1))
        return i + 2
    elif op == 5:
        if get_value(i + 1, mode1) != 0:
            return get_value(i + 2, mode2)
        else:
            return i + 3
    elif op == 6:
        if get_value(i + 1, mode1) == 0:
            return get_value(i + 2, mode2)
        else:
            return i + 3
    elif op == 7:
        if get_value(i + 1, mode1) < get_value(i + 2, mode2):
            prog[prog[i + 3]] = 1
        else:
            prog[prog[i + 3]] = 0
        return i + 4
    elif op == 8:
        if get_value(i + 1, mode1) == get_value(i + 2, mode2):
            prog[prog[i + 3]] = 1
        else:
            prog[prog[i + 3]] = 0
        return i + 4
    else:
        return -1


def get_value(i, mode):
    global prog
    # print(f"Mode: {mode}")
    if mode == 0:
        return prog[prog[i]]
    elif mode == 1:
        return prog[i]


if __name__ == "__main__":
    print(solve("input.txt"))
