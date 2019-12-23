import re


def solve(filename):
    cards = list(range(10007))
    with open(filename) as f:
        for row in f:
            if row.startswith("deal into"):
                cards.reverse()
            else:
                num = list(map(int, re.findall(r"[-0-9]+", row)))[0]
                if row.startswith("cut"):
                    cards = cut(cards, num)
                else:
                    cards = deal_inc(cards, num)
    return cards


def solve2(filename):
    position = 2020
    size = 119315717514047
    iterations = 101741582076661
    offset = 0
    increment = 1
    with open(filename) as f:
        for row in f.readlines():
            if row.startswith("deal into"):
                increment *= -1
                increment %= size
                offset += increment
                offset %= size
            else:
                num = list(map(int, re.findall(r"[-0-9]+", row)))[0]
                if row.startswith("cut"):
                    offset += increment * num
                    offset %= size
                else:
                    increment *= pow(num, -1, size)
                    increment %= size

    increment_total = pow(increment, iterations, size)
    offset = offset * (1 - increment_total) * pow(1 - increment, -1, size)
    return (offset + increment_total * position) % size


def cut(cards, n):
    return cards[n:] + cards[:n]


def deal_inc(cards, n):
    res = [0] * len(cards)
    i = 0
    for c in cards:
        res[i % len(cards)] = c
        i += n
    return res


if __name__ == "__main__":
    print(solve2("input.txt"))
