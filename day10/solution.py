import math
import numpy as np


def unit_vector(vector):
    return vector / math.sqrt(vector[0]**2 + vector[1]**2)


def angle_between(v1, v2):
    v2_u = unit_vector(v2)
    res = np.arccos(np.dot(v1, v2_u))
    if v2[0] < 0:
        return 8 - res
    return res


def read(filename):
    with open(filename) as f:
        width = 0
        height = 0
        asteroids = []
        for row in f:
            width = len(row)
            for j in range(len(row)):
                if row[j] == "#":
                    asteroids.append((j, height))
            height += 1
    return asteroids, width, height


def solve1(filename):
    asteroids, width, height = read(filename)
    max_count = 0
    for asteroid in asteroids:
        can_see = asteroids[:]
        for x, y in can_see:
            if x == asteroid[0] and y == asteroid[1]:
                continue
            cur_x, cur_y = asteroid
            diff_x, diff_y = x - cur_x, y - cur_y
            d = max(1, math.gcd(abs(diff_x), abs(diff_y)))
            scaled_diff_x, scaled_diff_y = diff_x // d, diff_y // d
            cur_x += scaled_diff_x
            cur_y += scaled_diff_y
            while 0 <= cur_x < width and 0 <= cur_y < height:
                a = (cur_x, cur_y)
                if a in can_see and a != (x, y):
                    can_see.remove(a)
                cur_x += scaled_diff_x
                cur_y += scaled_diff_y
        if len(can_see) > max_count:
            max_count = len(can_see)
    return max_count - 1


def solve2(filename):
    asteroids, width, height = read(filename)

    max_asteroid = None
    max_can_see = []
    for asteroid in asteroids:
        can_see = asteroids[:]
        for x, y in can_see:
            if x == asteroid[0] and y == asteroid[1]:
                continue
            cur_x, cur_y = asteroid
            diff_x, diff_y = x - cur_x, y - cur_y
            d = max(1, math.gcd(abs(diff_x), abs(diff_y)))
            scaled_diff_x, scaled_diff_y = diff_x // d, diff_y // d
            cur_x += scaled_diff_x
            cur_y += scaled_diff_y
            to_keep = None
            while 0 <= cur_x < width and 0 <= cur_y < height:
                a = (cur_x, cur_y)
                if a in can_see and a != (x, y):
                    can_see.remove(a)
                # if a in can_see:
                #     if to_keep is None:
                #         to_keep = a
                #     else:
                #         can_see.remove(a)
                cur_x += scaled_diff_x
                cur_y += scaled_diff_y
        if len(can_see) > len(max_can_see):
            max_asteroid = asteroid
            max_can_see = can_see

    center = max_asteroid
    max_can_see.remove(center)
    print(len(max_can_see))
    max_can_see.sort(key=lambda z: angle_between(np.array([0, 1]), np.array([z[0] - center[0], center[1] - z[1]])))
    return max_can_see


if __name__ == "__main__":
    asteroids = solve2("test5.txt")
    for y in range(20):
        for x in range(20):
            if (x, y) == (11, 13):
                print("  *  ", end="")
            elif (x, y) in asteroids:
                res = str(asteroids.index((x, y)))
                print(" " + res + (4 - len(res)) * " ", end="")
            else:
                print("  .  ", end="")
        print()
    # print(solve2("test5.txt"[199]))
