

def solve(filename):
    with open(filename) as f:
        wire1ops = f.readline()
        wire2ops = f.readline()
        wire1coords, wire1steps = coordinates(wire1ops)
        wire2coords, wire2steps = coordinates(wire2ops)
        cross = wire1coords.intersection(wire2coords)
        if (0, 0) in cross:
            cross.remove((0, 0))
        return min(map(lambda x: wire1steps[x] + wire2steps[x], cross))


def coordinates(ops):
    coords = set()
    stepsdict = dict()
    steps = 0
    x = y = 0
    ops = ops.split(",")
    for op in ops:
        dir = op[0]
        num = int(op[1:])
        if dir == "U":
            for _ in range(num):
                y += 1
                steps += 1
                coords.add((x, y))
                if (x, y) in stepsdict:
                    stepsdict[(x, y)] = min(steps, stepsdict[(x, y)])
                else:
                    stepsdict[(x, y)] = steps
        elif dir == "R":
            for _ in range(num):
                x += 1
                steps += 1
                coords.add((x, y))
                if (x, y) in stepsdict:
                    stepsdict[(x, y)] = min(steps, stepsdict[(x, y)])
                else:
                    stepsdict[(x, y)] = steps
        elif dir == "D":
            for _ in range(num):
                y -= 1
                steps += 1
                coords.add((x, y))
                if (x, y) in stepsdict:
                    stepsdict[(x, y)] = min(steps, stepsdict[(x, y)])
                else:
                    stepsdict[(x, y)] = steps
        elif dir == "L":
            for _ in range(num):
                x -= 1
                steps += 1
                coords.add((x, y))
                if (x, y) in stepsdict:
                    stepsdict[(x, y)] = min(steps, stepsdict[(x, y)])
                else:
                    stepsdict[(x, y)] = steps

    return coords, stepsdict


if __name__ == "__main__":
    print(solve("input.txt"))
