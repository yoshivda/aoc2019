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
                        if y == 0:
                            labels[(x, y + 2)] = (coords[(x, y)] + coords[(x, y + 1)], -1)
                        else:
                            labels[(x, y + 2)] = (coords[(x, y)] + coords[(x, y + 1)], 1)
                    else:
                        if y == max_y + 1:
                            labels[(x, y - 1)] = (coords[(x, y)] + coords[(x, y + 1)], -1)
                        else:
                            labels[(x, y - 1)] = (coords[(x, y)] + coords[(x, y + 1)], 1)
                elif coords[(x + 1, y)].isupper():
                    if coords[(x + 2, y)] == ".":
                        if x == 0:
                            labels[(x + 2, y)] = (coords[(x, y)] + coords[(x + 1, y)], -1)
                        else:
                            labels[(x + 2, y)] = (coords[(x, y)] + coords[(x + 1, y)], 1)
                    else:
                        if x == max_x + 1:
                            labels[(x - 1, y)] = (coords[(x, y)] + coords[(x + 1, y)], -1)
                        else:
                            labels[(x - 1, y)] = (coords[(x, y)] + coords[(x + 1, y)], 1)

    return bfs([k for k in labels.keys() if labels[k][0] == "AA"][0], coords, labels, max_x, max_y)


def bfs(t, coords, labels, max_x, max_y):
    # print(labels)
    x, y = t
    q = deque()
    q.append((x, y, 1, 0))
    discovered = {(x, y, 0)}
    while q:
        x, y, length, lvl = q.popleft()
        for new_x, new_y, lvl_change in surrounding_positions(x, y, labels, max_x, max_y, lvl):
            if coords[(new_x, new_y)] == ".":
                new_lvl = lvl + lvl_change
                # if lvl_change != 0:
                #     print(labels[(new_x, new_y)][0], new_lvl, x, y)
                if (new_x, new_y, new_lvl) not in discovered:
                    # print(new_x, new_y, new_lvl)
                    discovered.add((new_x, new_y, new_lvl))
                    if (new_x, new_y) in labels and labels[(new_x, new_y)][0] == "ZZ":
                        print(new_lvl)
                    if (new_x, new_y) in labels and labels[(new_x, new_y)][0] == "ZZ" and new_lvl == 0:
                        return length
                    if coords[(new_x, new_y)] == ".":
                        q.append((new_x, new_y, length + 1, new_lvl))


def surrounding_positions(x, y, labels, max_x, max_y, lvl):
    res = [(x, y + 1, 0), (x, y - 1, 0), (x - 1, y, 0), (x + 1, y, 0)]
    if (x, y) in labels and labels[(x, y)][0] not in ("AA", "ZZ"):
        jmp_x, jmp_y = [t for t in labels.keys() if labels[t][0] == labels[(x, y)][0] and (x != t[0] or y != t[1])][0]
        lvl_change = labels[(x, y)][1]
        # print(x, y, jmp_x, jmp_y, lvl_change)
        if lvl_change < 0 and lvl == 0:
            return res
        res.append((jmp_x, jmp_y, lvl_change))
    res = list(filter(lambda t: 2 <= t[0] <= max_x and 2 <= t[1] <= max_y, res))
    return res


if __name__ == "__main__":
    print(solve("input.txt"))
