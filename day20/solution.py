from collections import deque, defaultdict


def read(filename):
    with open(filename) as f:
        coords = defaultdict(str)
        y = 0
        for row in f:
            x = 0
            for c in row.strip('\n'):
                if c != ' ':
                    coords[(x, y)] = c
                x += 1
            y += 1
    return coords


def solve(filename):
    coords = read(filename)
    max_x, max_y = max(coords.keys(), key=lambda t: t[0] if coords[t] == "." else -1)[0], max(coords.keys(), key=lambda t: t[1] if coords[t] == "." else -1)[1]
    labels = dict()
    for x in range(max_x + 3):
        for y in range(max_y + 3):
            if coords[(x, y)].isupper():
                if coords[(x, y + 1)].isupper():
                    if coords[(x, y + 2)] == ".":
                        labels[(x, y + 2)] = coords[(x, y)] + coords[(x, y + 1)]
                    else:
                        labels[(x, y - 1)] = coords[(x, y)] + coords[(x, y + 1)]
                elif coords[(x + 1, y)].isupper():
                    if coords[(x + 2, y)] == ".":
                        labels[(x + 2, y)] = coords[(x, y)] + coords[(x + 1, y)]
                    else:
                        labels[(x - 1, y)] = coords[(x, y)] + coords[(x + 1, y)]

    return bfs([k for k in labels.keys() if labels[k] == "AA"][0], coords, labels, max_x, max_y)


def bfs(t, coords, labels, max_x, max_y):
    x, y = t
    q = deque()
    q.append((x, y, 1))
    discovered = set()
    while q:
        # print(discovered)
        x, y, length = q.popleft()
        for new_x, new_y in surrounding_positions(x, y, labels, max_x, max_y):
            if (new_x, new_y) not in discovered:
                discovered.add((new_x, new_y))
                if (new_x, new_y) in labels and labels[(new_x, new_y)] == "ZZ":
                    return length
                if coords[(new_x, new_y)] == ".":
                    q.append((new_x, new_y, length + 1))


def surrounding_positions(x, y, labels, max_x, max_y):
    res = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]
    if (x, y) in labels and labels[(x, y)] != "AA":
        jmp_x, jmp_y = [t for t in labels.keys() if labels[t] == labels[(x, y)] and (x != t[0] or y != t[1])][0]
        # print(x, y, jmp_x, jmp_y)
        res = list(filter(lambda t: 2 <= t[0] <= max_x and 2 <= t[1] <= max_y, res))
        res.append((jmp_x, jmp_y))
    return res


if __name__ == "__main__":
    print(solve("input.txt"))
