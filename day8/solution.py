def solve(filename, width, height):
    with open(filename) as f:
        row = f.readline().strip()
        layers = [row[x:x+width*height] for x in range(0, len(row), width*height)]
        layer = min(layers, key=lambda x: x.count("0"))
        return layer.count("1") * layer.count("2")


if __name__ == "__main__":
    print(solve("input.txt", 25, 6))
