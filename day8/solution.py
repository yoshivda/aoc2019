def solve1(filename, width, height):
    with open(filename) as f:
        row = f.readline().strip()
        layers = [row[x:x+width*height] for x in range(0, len(row), width*height)]
        layer = min(layers, key=lambda x: x.count("0"))
        return layer.count("1") * layer.count("2")


def solve2(filename, width, height):
    with open(filename) as f:
        row = f.readline().strip()
        layers = [row[x:x+width*height] for x in range(0, len(row), width*height)]
        res = ""
        for i in range(width*height):
            for layer in layers:
                if layer[i] == "0":
                    res += " "
                    break
                elif layer[i] == "1":
                    res += "#"
                    break
        res = [res[x:x+width] for x in range(0, len(row), width)]
        return "\n".join(res)


if __name__ == "__main__":
    # print(solve1("input.txt", 25, 6))
    print(solve2("input.txt", 25, 6))
