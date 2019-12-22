from collections import deque
states = dict()


def read(filename):
    with open(filename) as f:
        coords = dict()
        y = 0
        for row in f:
            x = 0
            for c in row.strip():
                coords[(x, y)] = c
                x += 1
            y += 1
    return coords


def solve(filename):
    global states
    states = dict()
    coords = read(filename)
    max_x, max_y = max(coords.keys(), key=lambda t: t[0])[0], max(coords.keys(), key=lambda t: t[1])[1]
    keys = [(x, y) for x in range(max_x + 1) for y in range(max_y + 1) if coords[(x, y)].islower()]
    origs = [(x, y) for x in range(max_x + 1) for y in range(max_y + 1) if coords[(x, y)] in "@!$%"]
    paths = {coords[p]: bfs_keys(p, coords, max_x, max_y) for p in keys + origs}
    res = total_steps(frozenset({"!", "@", "$", "%"}), frozenset(), paths, len(keys))
    print(len(states))
    return res


def total_steps(positions, keys, paths, no_keys):
    if (positions, keys) in states:
        return states[(positions, keys)]
    if len(keys) == no_keys:
        return 0
    res = min((total_steps(frozenset((positions - {p}) | {key}), frozenset(keys | {key}), paths, no_keys) + paths[p][key][0]
               for p in positions for key in paths[p].keys()
               if all(x in keys for x in paths[p][key][1]) and key not in keys), default=(987654321, 0, 0))
    states[(positions, keys)] = res
    return res


def bfs_keys(t, coords, max_x, max_y):
    x, y = t
    q = deque()
    q.append((x, y, 0, set()))
    discovered = {(x, y)}
    paths = dict()
    while q:
        x, y, length, reqs = q.popleft()
        for new_x, new_y in surrounding_positions(x, y, max_x, max_y):
            char = coords[(new_x, new_y)]
            if char != "#":
                if (new_x, new_y) not in discovered:
                    discovered.add((new_x, new_y))
                    if char.islower():
                        paths[char] = (length + 1, reqs)
                    elif char.isupper():
                        reqs.add(char.lower())
                    q.append((new_x, new_y, length + 1, reqs.copy()))
    return paths


def surrounding_positions(x, y, max_x, max_y):
    res = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]
    res = list(filter(lambda t: 0 <= t[0] <= max_x and 0 <= t[1] <= max_y, res))
    return res


if __name__ == "__main__":
    print(solve("input2.txt"))
