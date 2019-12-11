prog = []
base = 0
direction = 0
color_mode = True
x = y = 0
painted_panels = {(0, 0): 1}


def solve(filename):
    global prog
    with open(filename) as f:
        prog = list(map(int, f.readline().split(",")))
    i = 0
    length = len(prog)
    while 0 <= i < length:
        i = calc(i)
    max_x, max_y = max(map(lambda t: t[0], painted_panels.keys())), max(map(lambda t: t[1], painted_panels.keys()))
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in painted_panels and painted_panels[(x, y)] == 1:
                print("█", end="")
            else:
                print(" ", end="")
        print()


def calc(i):
    global prog
    global base
    global direction
    global x
    global y
    global color_mode
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
            if (x, y) in painted_panels:
                data = painted_panels[(x, y)]
            else:
                data = 0
            prog[get_index(i + 1, mode1)] = data
            return i + 2
        elif op == 4:
            if color_mode:
                painted_panels[(x, y)] = get_value(i + 1, mode1)
            else:
                direction = (direction + get_value(i + 1, mode1) * 2 - 1) % 4

                if direction == 0:
                    y -= 1
                elif direction == 1:
                    x += 1
                elif direction == 2:
                    y += 1
                else:
                    x -= 1
            color_mode = not color_mode

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
    print(solve("input.txt"))
