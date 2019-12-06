prog = []


def solve(filename, init1, init2):
    global prog
    with open(filename) as f:
        for row in f:
            prog = list(map(int, row.split(",")))
    if filename == "input.txt":
        prog[1] = init1
        prog[2] = init2
    for i in range(0, len(prog), 4):
        if prog[i] not in [1, 2]:
            return prog
        calc(i)
    return prog


def calc(i):
    global prog
    if prog[i] == 1:
        prog[prog[i + 3]] = prog[prog[i + 1]] + prog[prog[i + 2]]
    elif prog[i] == 2:
        prog[prog[i + 3]] = prog[prog[i + 1]] * prog[prog[i + 2]]


if __name__ == "__main__":
    for i in range(100):
        for j in range(100):
            if solve("input.txt", i, j)[0] == 19690720:
                print(i*100+j)
