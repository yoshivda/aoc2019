prog = []
orig_prog = []
base = 0
inputs = []
outputs = []
output = -1


def solve1(filename):
    global prog
    global orig_prog
    global inputs
    global base
    with open(filename) as f:
        orig_prog = list(map(int, f.readline().split(",")))

    length = len(orig_prog)

    for x in range(50):
        for y in range(50):
            inputs = [x, y]
            i = 0
            base = 0
            prog = orig_prog.copy()
            while 0 <= i < length:
                i = calc(i)
    return sum(outputs)


def solve2(filename):
    global inputs
    global base
    global orig_prog
    with open(filename) as f:
        orig_prog = list(map(int, f.readline().split(",")))

    x = 0
    y = 99
    while not ray(x + 99, y - 99):
        # print(x, y)
        y += 1
        while not ray(x, y):
            x += 1

    return x * 10_000 + y - 99


def ray(x, y):
    global inputs
    global base
    global prog

    inputs = [x, y]
    i = 0
    base = 0
    length = len(orig_prog)
    prog = orig_prog.copy()

    while 0 <= i < length:
        i = calc(i)
    return output == 1


def calc(i):
    global prog
    global base
    global output
    op = prog[i] % 100
    mode1 = prog[i] % 1000 // 100
    mode2 = prog[i] % 10000 // 1000
    mode3 = prog[i] % 100000 // 10000

    try:
        if op == 1:
            prog[get_index(i + 3, mode3)] = get_value(i + 1, mode1) + get_value(i + 2, mode2)
            return i + 4
        elif op == 2:
            prog[get_index(i + 3, mode3)] = get_value(i + 1, mode1) * get_value(i + 2, mode2)
            return i + 4
        elif op == 3:
            prog[get_index(i + 1, mode1)] = 0
            # data = int(input("Please provide input\n"))
            data = inputs.pop(0)
            prog[get_index(i + 1, mode1)] = data
            return i + 2
        elif op == 4:
            # print(get_value(i + 1, mode1))
            outputs.append(get_value(i + 1, mode1))
            output = get_value(i + 1, mode1)
            return -1
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
                prog[get_index(i + 3, mode3)] = 1
            else:
                prog[get_index(i + 3, mode3)] = 0
            return i + 4
        elif op == 8:
            if get_value(i + 1, mode1) == get_value(i + 2, mode2):
                prog[get_index(i + 3, mode3)] = 1
            else:
                prog[get_index(i + 3, mode3)] = 0
            return i + 4
        elif op == 9:
            base += get_value(i + 1, mode1)
            return i + 2
        else:
            return -1
    except IndexError:
        prog += [0] * 1000
        return calc(i)


def get_index(i, mode):
    global prog
    try:
        if mode == 0:
            return prog[i]
        elif mode == 1:
            return i
        elif mode == 2:
            return base + prog[i]
    except IndexError:
        prog += [0] * 1000
        return get_index(i, mode)


def get_value(i, mode):
    return prog[get_index(i, mode)]


if __name__ == "__main__":
    print(solve2("input.txt"))



