import math


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


def solve(filename):
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
        print(asteroid, len(can_see))

    return max_count - 1


if __name__ == "__main__":
    print(solve("input.txt"))
