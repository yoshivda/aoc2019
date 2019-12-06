def solve(filename):
    orbits = dict()
    planets = set()
    with open(filename) as f:
        for row in f:
            row = row.strip()
            a, b = row.split(")")
            planets.add(a)
            planets.add(b)
            orbits[b] = a
    return sum(calc_orbits(orbits, p) for p in planets)


amount_orbits = {"COM": 0}


def calc_orbits(orbits, p):
    if p in amount_orbits:
        return amount_orbits[p]
    else:
        return 1 + calc_orbits(orbits, orbits[p])


if __name__ == "__main__":
    print(solve("input.txt"))
