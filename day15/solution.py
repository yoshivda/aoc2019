from collections import deque


def solve(filename):
    with open(filename) as f:
        prog = list(map(int, f.readline().split(",")))
    discovered = {(0, 0): 1}
    q = deque()
    q.append(((0, 0), 0, prog, 0, 0))
    o_pos = None
    while len(q) > 0:
        # print([(x, y) for ((x, y), _, _, _, _) in q])
        pos, i_orig, prog_orig, base_orig, path = q.popleft()
        for in_value, new_pos in surrounding_positions(pos).items():
            if new_pos not in discovered:
                i, res, prog, base = calc(i_orig, prog_orig, base_orig, in_value)
                discovered[new_pos] = res
                if res == 2:
                    o_pos = new_pos
                if res >= 1:
                    q.append((new_pos, i, prog, base, path + 1))

    print(discovered)
    max_x, max_y = max(map(lambda t: t[0], discovered)), max(map(lambda t: t[1], discovered))
    min_x, min_y = min(map(lambda t: t[0], discovered)), min(map(lambda t: t[1], discovered))
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if x == y == 0:
                print("S", end="")
            elif (x, y) in discovered:
                if discovered[(x, y)] == 0:
                    print("#", end="")
                elif discovered[(x, y)] == 2:
                    print("O", end="")
                else:
                    print(".", end="")
            else:
                print(" ", end="")
        print()

    cnt = 0
    oxigen = {o_pos}
    while not all(k in oxigen for k in discovered.keys() if discovered[k] == 1):
        cnt += 1
        for p in oxigen.copy():
            for _, n in surrounding_positions(p).items():
                if discovered[n] > 0 and n not in oxigen:
                    oxigen.add(n)
    return cnt


def surrounding_positions(t):
    x, y = t
    return {1: (x, y + 1), 2: (x, y - 1), 3: (x - 1, y), 4: (x + 1, y)}


def calc(i, prog, base, in_value):
    prog = prog[:]

    while i < len(prog):
        op = prog[i] % 100
        mode1 = prog[i] % 1000 // 100
        mode2 = prog[i] % 10000 // 1000
        mode3 = prog[i] % 100000 // 10000
        try:
            if op == 1:
                prog[get_index(i + 3, mode3, prog, base)] = get_value(i + 1, mode1, prog, base) + get_value(i + 2, mode2, prog, base)
                i += 4
            elif op == 2:
                prog[get_index(i + 3, mode3, prog, base)] = get_value(i + 1, mode1, prog, base) * get_value(i + 2, mode2, prog, base)
                i += 4
            elif op == 3:
                data = in_value
                prog[get_index(i + 1, mode1, prog, base)] = data
                i += 2
            elif op == 4:
                # print(get_value(i + 1, mode1, prog, base))
                return i + 2, get_value(i + 1, mode1, prog, base), prog, base
            elif op == 5:
                if get_value(i + 1, mode1, prog, base) != 0:
                    i = get_value(i + 2, mode2, prog, base)
                else:
                    i += 3
            elif op == 6:
                if get_value(i + 1, mode1, prog, base) == 0:
                    i = get_value(i + 2, mode2, prog, base)
                else:
                    i += 3
            elif op == 7:
                if get_value(i + 1, mode1, prog, base) < get_value(i + 2, mode2, prog, base):
                    prog[get_index(i + 3, mode3, prog, base)] = 1
                else:
                    prog[get_index(i + 3, mode3, prog, base)] = 0
                i += 4
            elif op == 8:
                if get_value(i + 1, mode1, prog, base) == get_value(i + 2, mode2, prog, base):
                    prog[get_index(i + 3, mode3, prog, base)] = 1
                else:
                    prog[get_index(i + 3, mode3, prog, base)] = 0
                i += 4
            elif op == 9:
                base += get_value(i + 1, mode1, prog, base)
                i += 2
            else:
                print("Woops!")
                return -1
        except IndexError:
            prog += [0] * 1000


def get_index(i, mode, prog, base):
    try:
        if mode == 0:
            return prog[i]
        elif mode == 1:
            return i
        elif mode == 2:
            return base + prog[i]
    except IndexError:
        prog += [0] * 1000
        return get_index(i, mode, prog, base)


def get_value(i, mode, prog, base):
    return prog[get_index(i, mode, prog, base)]


if __name__ == "__main__":
    print(solve("input.txt"))



