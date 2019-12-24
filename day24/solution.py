from collections import defaultdict
from copy import deepcopy


def solve(filename):
    levels = defaultdict(set)
    with open(filename) as f:
        levels[0] = {(x, y) for y, line in enumerate(f) for x, char in enumerate(line) if char == "#"}
    for i in range(200):
        loop = deepcopy(levels)
        for lvl in range(-(i + 1), i + 2):
            for x in range(5):
                for y in range(5):
                    if x == y == 2:
                        continue
                    if (x, y) not in loop[lvl] and 1 <= surrounding_bugs(x, y, lvl, levels) <= 2:
                        loop[lvl].add((x, y))
                    elif (x, y) in loop[lvl] and surrounding_bugs(x, y, lvl, levels) != 1:
                        loop[lvl].remove((x, y))
        levels.update(loop)

        # for k, v in sorted(levels.items()):
        #     if v:
        #         print("Level", k)
        #         for y in range(5):
        #             for x in range(5):
        #                 if (x, y) in v:
        #                     print("#", end="")
        #                 else:
        #                     print(".", end="")
        #             print()
        #         print()
        # print("---------------")
        # print()

    return sum(len(lvl) for (_, lvl) in levels.items())


def surrounding_bugs(x, y, level, levels):
    return sum((nx, ny) in levels[level + lvl_diff] for (nx, ny, lvl_diff) in surrounding_positions(x, y))


def surrounding_positions(x, y):
    res = set(filter(lambda t: 0 <= t[0] < 5 and 0 <= t[1] < 5, {(x, y + 1, 0), (x, y - 1, 0), (x - 1, y, 0), (x + 1, y, 0)})) - {(2, 2, 0)}
    if x == 0:
        res.add((1, 2, -1))
    elif x == 4:
        res.add((3, 2, -1))
    elif (x, y) == (2, 1):
        res |= {(x, 0, 1) for x in range(5)}
    elif (x, y) == (1, 2):
        res |= {(0, y, 1) for y in range(5)}
    elif (x, y) == (2, 3):
        res |= {(x, 4, 1) for x in range(5)}
    elif (x, y) == (3, 2):
        res |= {(4, y, 1) for y in range(5)}
    if y == 0:
        res.add((2, 1, -1))
    elif y == 4:
        res.add((2, 3, -1))
    return res


if __name__ == "__main__":
    print(solve("input.txt"))



