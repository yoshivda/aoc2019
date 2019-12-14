def read(filename):
    reactions = dict()
    with open(filename) as f:
        for row in f:
            reqs, prod = row.split(" => ")
            reqs = list(map(lambda t: (t[1], int(t[0])), map(lambda x: x.split(), reqs.split(", "))))
            prod = (prod.split()[1], int(prod.split()[0]))
            reactions[prod[0]] = (prod[1], reqs)
    return reactions


def solve1(filename):
    reactions = read(filename)
    required = dict(reactions["FUEL"][1])
    leftovers = dict()
    while len(required) > 1:
        cp = required.copy()
        for prod, quant in cp.items():
            if prod in leftovers:
                required[prod] -= min(leftovers[prod], quant)
                leftovers[prod] -= min(leftovers[prod], quant)
                if leftovers[prod] == 0:
                    del leftovers[prod]

        if "ORE" in required and required["ORE"] == 180697:
            print(required, leftovers)
        cp = required.copy()
        for prod, quant in cp.items():
            if prod == "ORE":
                continue

            prod_quant, reqs = reactions[prod]

            if quant == 0:
                required[prod] -= quant
                if required[prod] == 0:
                    del required[prod]
                continue

            times = 1
            while prod_quant < quant:
                prod_quant += reactions[prod][0]
                times += 1

            if prod_quant > quant:
                # More produced than necessary
                required[prod] -= quant
                if prod in leftovers:
                    leftovers[prod] += prod_quant - quant
                else:
                    leftovers[prod] = prod_quant - quant
            elif prod_quant == quant:
                # Same production
                required[prod] -= quant
            else:
                # Needs more production
                required[prod] -= prod_quant

            if required[prod] == 0:
                del required[prod]

            if quant == 0:
                continue

            for p, q in reqs:
                if p in required:
                    required[p] += q * times
                else:
                    required[p] = q * times
    if "ORE" in leftovers:
        return required["ORE"] - leftovers["ORE"]
    return required["ORE"]


if __name__ == "__main__":
    print(solve1("input.txt"))
