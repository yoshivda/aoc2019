

def solve(filename):
    res = 0
    with open(filename) as f:
        for row in f:
            fuel = int(row) // 3 - 2
            res += fuel
            while True:
                fuel = fuel // 3 - 2
                if fuel <= 0:
                    break
                res += fuel
    return res


if __name__ == "__main__":
    print(solve("input.txt"))
