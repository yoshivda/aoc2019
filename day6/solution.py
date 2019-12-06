def read(filename):
    orbits = dict()
    planets = set()
    with open(filename) as f:
        for row in f:
            row = row.strip()
            a, b = row.split(")")
            planets.add(a)
            planets.add(b)
            orbits[b] = a
    return orbits, planets


def solve1(filename):
    orbits, planets = read(filename)
    return sum(calc_orbits(orbits, p) for p in planets)


def solve2(filename):
    orbits, _ = read(filename)
    trace_you = trace_orbits(orbits, "YOU")
    trace_san = trace_orbits(orbits, "SAN")
    min_steps = 1000000000
    for i in range(len(trace_you)):
        for j in range(len(trace_san)):
            if trace_you[i] == trace_san[j] and i + j < min_steps:
                min_steps = i + j
    return min_steps - 2


amount_orbits = {"COM": 0}


def calc_orbits(orbits, p):
    if p in amount_orbits:
        return amount_orbits[p]
    else:
        return 1 + calc_orbits(orbits, orbits[p])


def trace_orbits(orbits, p):
    if p == "COM":
        return []
    return [p] + trace_orbits(orbits, orbits[p])


if __name__ == "__main__":
    print(solve2("input.txt"))
