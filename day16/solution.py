def solve1(filename):
    with open(filename) as f:
        num = list(map(int, f.readline().strip()))
    orig_pattern = [0, 1, 0, -1]
    for _ in range(100):
        out = []
        for i in range(1, len(num) + 1):
            pattern = [orig_pattern[0]] * i + [orig_pattern[1]] * i + [orig_pattern[2]] * i + [orig_pattern[3]] * i
            res = 0
            for j in range(len(num)):
                res += num[j] * pattern[(j + 1) % len(pattern)]
                # print(f"{num[j]}*{pattern[(j + 1) % len(pattern)]} + ", end = "")
            out.append(abs(res) % 10)
            # print("=", abs(res) % 10)
        num = out
    return list(map(str, out))


def solve2(filename):
    with open(filename) as f:
        row = f.readline().strip()
        offset = int(row[:7])
        num = (list(map(int, row)) * 10_000)[offset:]

    for _ in range(100):
        old = 0
        res = []
        for i in list(reversed(num)):
            c = (i + old) % 10
            res.append(c)
            old = c
        num = list(reversed(res))
    return int("".join(map(str, num[:8])))


if __name__ == "__main__":
    # print("".join(solve1("input.txt")[:8]))
    print(solve2("input.txt"))
