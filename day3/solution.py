

def solve(filename):
    with open(filename) as f:
        wire1ops = f.readline()
        wire2ops = f.readline()
        wire1 = coordinates(wire1ops)
        wire2 = coordinates(wire2ops)
        cross = wire1.intersection(wire2)
        cross.remove((0, 0))
        return min(map(lambda x: abs(x[0]) + abs(x[1]), cross))


def coordinates(ops):
    res = set()
    x = y = 0
    ops = ops.split(",")
    for op in ops:
        dir = op[0]
        num = int(op[1:])
        if dir == "U":
            res = res.union({(x, y + i) for i in range(num)})
            y += num
        elif dir == "R":
            res = res.union({(x + i, y) for i in range(num)})
            x += num
        elif dir == "D":
            res = res.union({(x, y - i) for i in range(num)})
            y -= num
        elif dir == "L":
            res = res.union({(x - i, y) for i in range(num)})
            x -= num

    return res


if __name__ == "__main__":
    print(solve("input.txt"))
