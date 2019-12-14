from math import ceil

def read(filename):
    reactions = dict()
    with open(filename) as f:
        for row in f:
            reqs, prod = row.split(" => ")
            reqs = list(map(lambda t: (t[1], int(t[0])), map(lambda x: x.split(), reqs.split(", "))))
            prod = (prod.split()[1], int(prod.split()[0]))
            reactions[prod[0]] = (prod[1], reqs)
    return reactions


def solve1(reactions, fuel):
    required = {"FUEL": fuel}
    leftovers = dict()
    while len(required) > 1 or "FUEL" in required:
        cp = required.copy()

        # Filter leftovers from requirements
        for prod, quant in cp.items():
            if prod in leftovers:
                required[prod] -= min(leftovers[prod], quant)
                leftovers[prod] -= min(leftovers[prod], quant)
                if leftovers[prod] == 0:
                    del leftovers[prod]

        # Make requirements
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

            # Calculate how many times we need the formula
            times = ceil(quant / reactions[prod][0])
            prod_quant = reactions[prod][0] * times


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

            # No longer needed
            if required[prod] == 0:
                del required[prod]

            # Requirement was solved with leftovers only
            if quant == 0:
                continue

            # Add all requirements to the list
            for p, q in reqs:
                if p in required:
                    required[p] += q * times
                else:
                    required[p] = q * times
    return required["ORE"]


def solve2(filename):
    reactions = read(filename)
    return bsearch(0, 10**12, reactions)


def bsearch(l, h, reactions):
    highest = 0
    while h - l > 1:
        val = l + (h - l) // 2
        if solve1(reactions, val) > 10**12:
            h = val
        else:
            if val > highest:
                highest = val
            l = val
    return highest


if __name__ == "__main__":
    # print(solve1(read("input.txt"), 1))
    print(solve2("input.txt"))
