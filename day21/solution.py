prog = []
base = 0
outputs = []
input_index = 0
char = 0
# inputs = list(map(list, ["NOT A T", "NOT B J", "OR T J", "NOT C T", "OR T J", "AND D J", "WALK"]))
inputs = list(map(list, ["OR A J", "AND B J", "AND C J", "NOT J J", "AND D J", "OR E T", "OR H T", "AND T J", "RUN"]))


def solve(filename):
    global prog
    with open(filename) as f:
        prog = list(map(int, f.readline().split(",")))
    i = 0
    length = len(prog)
    while 0 <= i < length:
        i = calc(i)


def calc(i):
    global prog
    global base
    global char
    global input_index
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
            # if input_index == len(inputs):
            #     data = ord('n')
            #     input_index += 1
            if input_index > len(inputs):
                data = 10
            elif char < len(inputs[input_index]):
                data = ord(inputs[input_index][char])
                char += 1
            else:
                data = 10
                char = 0
                input_index += 1
            # print(data, chr(data))
            prog[get_index(i + 1, mode1)] = data
            return i + 2
        elif op == 4:
            res = get_value(i + 1, mode1)
            if res < 128:
                print(chr(get_value(i + 1, mode1)), end="")
            else:
                print(res)
            outputs.append(get_value(i + 1, mode1))
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
        prog += [0] * 10000
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
