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
    # doors = {coords[(x, y)]: (x, y) for x in range(max_x + 1) for y in range(max_y + 1) if coords[(x, y)].isupper()}
    orig = [(x, y) for x in range(max_x + 1) for y in range(max_y + 1) if coords[(x, y)] == "@"]
    paths = {coords[p]: bfs_keys(p, coords, max_x, max_y) for p in keys + orig}
    print(paths)
    return total_steps("@", frozenset(), paths, len(keys))


def total_steps(char, keys, paths, no_keys):
    if (char, keys) in states:
        return states[(char, keys)]
    if len(keys) == no_keys:
        return 0
    res = min((total_steps(key, frozenset(keys | {key}), paths, no_keys) + paths[char][key][0] for key in paths[char].keys()
              if all(x in keys for x in paths[char][key][1]) and key not in keys), default=1000000)
    states[(char, keys)] = res
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
                        # continue
                    elif char.isupper():
                        reqs.add(char.lower())
                    q.append((new_x, new_y, length + 1, reqs.copy()))
    return paths


def surrounding_positions(x, y, max_x, max_y):
    res = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]
    res = list(filter(lambda t: 0 <= t[0] <= max_x and 0 <= t[1] <= max_y, res))
    return res


if __name__ == "__main__":
    print(solve("input.txt"))
