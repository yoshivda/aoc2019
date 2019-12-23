import threading
from time import sleep

done = False


def solve(filename):
    with open(filename) as f:
        prog = list(map(int, f.readline().split(",")))
    comps = [Computer(prog.copy(), i) for i in range(50)]
    comps.append(Nat())
    for c in comps:
        c.computers = comps
    for c in (comps[-1:] + comps[:-1]):
        c.run()


class Nat:
    def __init__(self):
        self.inputs = []
        self.computers = []
        self.outputs = []
        self.t = None
        self.sent = None

    def run(self):
        print("Starting NAT")
        self.computers = self.computers[:-1]
        self.t = threading.Thread(target=self.calc)
        self.t.start()

    def stop(self):
        self.t.join()

    def calc(self):
        res = None
        while True:
            if len(self.inputs) > 0:
                res = self.inputs[-1]
                self.inputs = []
            if self.idle():
                if self.sent and res[1] == self.sent:
                    print("Result:", res[1])
                    for c in self.computers:
                        c.stop()
                    return
                elif res:
                    self.sent = res[1]
                    self.computers[0].inputs.extend(res)
                    sleep(2)

    def idle(self):
        return not(any(c.inputs for c in self.computers)) and all(c.tries > 10 for c in self.computers)


class Computer:

    def __init__(self, prog, address):
        self.address = address
        self.prog = prog
        self.base = 0
        self.inputs = [address]
        self.computers = []
        self.outputs = []
        self.tries = 0

    def run(self):
        print("Starting", self.address)
        self.t = threading.Thread(target=self.calc)
        self.t.start()

    def stop(self):
        self.t.join()

    def calc(self):
        i = 0

        while i < len(self.prog):
            op = self.prog[i] % 100
            mode1 = self.prog[i] % 1000 // 100
            mode2 = self.prog[i] % 10000 // 1000
            mode3 = self.prog[i] % 100000 // 10000

            try:
                if op == 1:
                    self.prog[self.get_index(i + 3, mode3)] = self.get_value(i + 1, mode1) + self.get_value(i + 2, mode2)
                    i += 4
                elif op == 2:
                    self.prog[self.get_index(i + 3, mode3)] = self.get_value(i + 1, mode1) * self.get_value(i + 2, mode2)
                    i += 4
                elif op == 3:
                    if len(self.inputs) > 0:
                        self.tries = 0
                        data = self.inputs.pop(0)
                    else:
                        self.tries += 1
                        data = -1
                    self.prog[self.get_index(i + 1, mode1)] = data
                    i += 2
                elif op == 4:
                    self.outputs.append(self.get_value(i + 1, mode1))
                    if len(self.outputs) == 3:
                        a, x, y = self.outputs
                        if a == 255:
                            self.computers[50].inputs.append([x, y])
                        else:
                            self.computers[a].inputs.extend([x, y])
                        self.outputs = []
                    i += 2
                elif op == 5:
                    if self.get_value(i + 1, mode1) != 0:
                        i = self.get_value(i + 2, mode2)
                    else:
                        i += 3
                elif op == 6:
                    if self.get_value(i + 1, mode1) == 0:
                        i = self.get_value(i + 2, mode2)
                    else:
                        i += 3
                elif op == 7:
                    if self.get_value(i + 1, mode1) < self.get_value(i + 2, mode2):
                        self.prog[self.get_index(i + 3, mode3)] = 1
                    else:
                        self.prog[self.get_index(i + 3, mode3)] = 0
                    i += 4
                elif op == 8:
                    if self.get_value(i + 1, mode1) == self.get_value(i + 2, mode2):
                        self.prog[self.get_index(i + 3, mode3)] = 1
                    else:
                        self.prog[self.get_index(i + 3, mode3)] = 0
                    i += 4
                elif op == 9:
                    self.base += self.get_value(i + 1, mode1)
                    i += 2
                else:
                    return -1
            except IndexError:
                self.prog += [0] * 1000
        print("PC", self.address, "terminated!")

    def get_index(self, i, mode):
        try:
            if mode == 0:
                return self.prog[i]
            elif mode == 1:
                return i
            elif mode == 2:
                return self.base + self.prog[i]
        except IndexError:
            self.prog += [0] * 1000
            return self.get_index(i, mode)

    def get_value(self, i, mode):
        return self.prog[self.get_index(i, mode)]


if __name__ == "__main__":
    solve("input.txt")



