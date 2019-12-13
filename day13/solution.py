prog = []
base = 0
output_mode = 0
tiles = dict()
x = y = 0


def solve1(filename):
    global prog
    with open(filename) as f:
        prog = list(map(int, f.readline().split(",")))
    i = 0
    length = len(prog)
    while 0 <= i < length:
        i = calc(i)
    return sum(v == 2 for v in tiles.values())


def calc(i):
    global prog
    global base
    global x
    global y
    global output_mode
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
            data = int(input("Please provide input\n"))
            prog[get_index(i + 1, mode1)] = data
            return i + 2
        elif op == 4:
            if output_mode == 0:
                x = get_value(i + 1, mode1)
            elif output_mode == 1:
                y = get_value(i + 1, mode1)
            elif output_mode == 2:
                tiles[(x, y)] = get_value(i + 1, mode1)
            output_mode = (output_mode + 1) % 3
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
    print(solve1("input.txt"))



