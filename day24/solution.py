def solve(filename):
    with open(filename) as f:
        bugs = {(x, y) for y, line in enumerate(f) for x, char in enumerate(line) if char == "#"}
    states = set()
    while frozenset(bugs) not in states:
        for y in range(5):
            for x in range(5):
                if (x, y) in bugs:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()
        states.add(frozenset(bugs))
        new_bugs = bugs.copy()
        for x in range(5):
            for y in range(5):
                if (x, y) not in bugs and 1 <= surrounding_bugs(x, y, bugs) <= 2:
                    new_bugs.add((x, y))
                elif (x, y) in bugs and surrounding_bugs(x, y, bugs) != 1:
                    new_bugs.remove((x, y))
        bugs = new_bugs
    for y in range(5):
        for x in range(5):
            if (x, y) in bugs:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()
    return sum(2 ** (y * 5 + x) for x, y in bugs)


def surrounding_bugs(x, y, bugs):
    return sum(t in bugs for t in surrounding_positions(x, y))


def surrounding_positions(x, y):
    return set(filter(lambda t: 0 <= t[0] < 5 and 0 <= t[1] < 5, {(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)}))


if __name__ == "__main__":
    print(solve("input.txt"))



