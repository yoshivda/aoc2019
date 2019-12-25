from itertools import combinations


prog = []
base = 0
outputs = []
input_index = 0
char = 0
# inputs = list(map(list, ["NOT A T", "NOT B J", "OR T J", "NOT C T", "OR T J", "AND D J", "WALK"]))
inputs = list(map(list, ["north", "east", "south", "west"]))
inpt = ""
walk_ops = []
items = set()
item_combs = set()
process_items = []
processing = False
current_items = []


def solve(filename):
    global prog
    global walk_ops
    global items
    global item_combs
    with open("walk.txt") as f:
        walk_ops = [line.strip() for line in f]
    with open("items.txt") as f:
        items = {line.strip() for line in f}
    for i in range(1, len(items) + 1):
        item_combs |= set(combinations(items, i))
    for t in item_combs:
        process_items.extend([f"take {i}" for i in t])
        process_items.append("break")
        process_items.extend([f"drop {i}" for i in t])
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
    global inpt
    global inputs
    global process_items
    global processing
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
            if inpt == "":
                if processing and process_items:
                    val = process_items.pop(0)
                    if val == "break":
                        val = "north"
                        input("Trying next")
                        print('Items:', current_items)
                    elif val.startswith("take"):
                        current_items.append("".join(val.split()[1:]))
                    elif val.startswith("drop"):
                        current_items.remove("".join(val.split()[1:]))
                elif walk_ops:
                    val = walk_ops.pop(0)
                else:
                    val = input()
                if val.isdigit():
                    inpt = inputs[int(val)]
                elif val == "try":
                    processing = True
                else:
                    inpt = val
            if input_index >= len(inpt):
                data = 10
                inpt = ""
                input_index = 0
            elif input_index < len(inpt):
                data = ord(inpt[input_index])
                input_index += 1
            # data = int("".join([f"{ord(c)}" for c in inp + "\n"]))
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
