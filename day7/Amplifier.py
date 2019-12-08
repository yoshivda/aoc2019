import itertools


class Amplifier:
    def __init__(self, name, output_func, prog):
        self.name = name
        self.output_func = output_func
        self.prog = prog[:]
        self.prog_index = 0
        self.output_val = -1
        self.init_val = -1

    def calc(self, in_val):
        print(f"Calculating with {in_val} on amp {self.name}")
        while True:
            i = self.prog_index
            op = self.prog[i] % 100
            mode1 = self.prog[i] % 1000 // 100
            mode2 = self.prog[i] % 10000 // 1000

            if op == 1:
                self.prog[self.prog[i + 3]] = self.get_value(i + 1, mode1) + self.get_value(i + 2, mode2)
                self.prog_index = i + 4
            elif op == 2:
                self.prog[self.prog[i + 3]] = self.get_value(i + 1, mode1) * self.get_value(i + 2, mode2)
                self.prog_index = i + 4
            elif op == 3:
                if self.init_val > 0:
                    data = self.init_val
                    self.init_val = -1
                else:
                    data = in_val
                self.prog[self.prog[i + 1]] = data
                self.prog_index = i + 2
            elif op == 4:
                res = self.get_value(i + 1, mode1)
                if self.name == "E":
                    print(res)
                    self.output_val = res
                self.prog_index = i + 2
                self.output_func(res)
                break
            elif op == 5:
                if self.get_value(i + 1, mode1) != 0:
                    self.prog_index = self.get_value(i + 2, mode2)
                else:
                    self.prog_index = i + 3
            elif op == 6:
                if self.get_value(i + 1, mode1) == 0:
                    self.prog_index = self.get_value(i + 2, mode2)
                else:
                    self.prog_index = i + 3
            elif op == 7:
                if self.get_value(i + 1, mode1) < self.get_value(i + 2, mode2):
                    self.prog[self.prog[i + 3]] = 1
                else:
                    self.prog[self.prog[i + 3]] = 0
                self.prog_index = i + 4
            elif op == 8:
                if self.get_value(i + 1, mode1) == self.get_value(i + 2, mode2):
                    self.prog[self.prog[i + 3]] = 1
                else:
                    self.prog[self.prog[i + 3]] = 0
                self.prog_index = i + 4
            else:
                break

    def get_value(self, i, mode):
        if mode == 0:
            return self.prog[self.prog[i]]
        elif mode == 1:
            return self.prog[i]


if __name__ == "__main__":
    phases = list(itertools.permutations(list(range(5, 10))))
    prog = []
    with open("input.txt") as f:
        for row in f:
            prog = list(map(int, row.split(",")))
    max_val = 0
    for config in phases:
        amps = [Amplifier(name, None, prog) for name in ["A", "B", "C", "D", "E"]]
        amps[0].output_func = lambda x: amps[1].calc(x)
        amps[1].output_func = lambda x: amps[2].calc(x)
        amps[2].output_func = lambda x: amps[3].calc(x)
        amps[3].output_func = lambda x: amps[4].calc(x)
        amps[4].output_func = lambda x: amps[0].calc(x)
        for index, num in enumerate(config):
            amps[index].init_val = num
        amps[0].calc(0)
        if amps[-1].output_val > max_val:
            max_val = amps[-1].output_val
    print(max_val)

