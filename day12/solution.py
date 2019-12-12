import re
from math import gcd


class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.x_vel = 0
        self.y_vel = 0
        self.z_vel = 0

    def apply_velocity(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.z += self.z_vel

    def __repr__(self):
        return f"pos=<x={self.x}, y={self.y}, z={self.z}>, vel=<x={self.x_vel}, y={self.y_vel}, z={self.z_vel}>"
    
    @staticmethod
    def gravity(m1, m2):
        if m1.x > m2.x:
            m1.x_vel -= 1
            m2.x_vel += 1
        elif m1.x < m2.x:
            m1.x_vel += 1
            m2.x_vel -= 1
        if m1.y > m2.y:
            m1.y_vel -= 1
            m2.y_vel += 1
        elif m1.y < m2.y:
            m1.y_vel += 1
            m2.y_vel -= 1
        if m1.z > m2.z:
            m1.z_vel -= 1
            m2.z_vel += 1
        elif m1.z < m2.z:
            m1.z_vel += 1
            m2.z_vel -= 1


def read(filename):
    with open(filename) as f:
        moons = []
        for line in f:
            line = list(map(int, re.findall(r"[-0-9]+", line)))
            moons.append(Moon(line[0], line[1], line[2]))
    return moons


def solve1(filename, steps):
    moons = read(filename)

    print(f"After 0 steps:")
    for moon in moons:
        print(moon)

    for i in range(1, steps + 1):
        print(f"After {i} steps:")
        for j, m1 in enumerate(moons):
            for m2 in moons[j+1:]:
                if m1 is not m2:
                    Moon.gravity(m1, m2)
        for moon in moons:
            moon.apply_velocity()
            print(moon)

    return sum((abs(m.x) + abs(m.y) + abs(m.z)) * (abs(m.x_vel) + abs(m.y_vel) + abs(m.z_vel)) for m in moons)


def calc_period(moons, coord):
    moons = moons[:]
    init_state = tuple(coord(m) for m in moons)

    i = 0
    while True:
        i += 1
        for j, m1 in enumerate(moons):
            for m2 in moons[j+1:]:
                Moon.gravity(m1, m2)
        for moon in moons:
            moon.apply_velocity()
        if tuple(coord(m) for m in moons) == init_state:
            return i


def lcm2(a, b):
    return (a * b) // gcd(a, b)


def lcm3(a, b, c):
    return lcm2(lcm2(a, b), c)


def solve2(filename):
    moons = read(filename)
    x = calc_period(moons, lambda m: (m.x, m.x_vel))
    y = calc_period(moons, lambda m: (m.y, m.y_vel))
    z = calc_period(moons, lambda m: (m.z, m.z_vel))
    print(x + y + z)
    return lcm3(x, y, z)


if __name__ == "__main__":
    print(solve2("input.txt"))
