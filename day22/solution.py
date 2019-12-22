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
    print(solve("input.txt").index(2019))
