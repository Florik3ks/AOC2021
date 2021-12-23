from time import process_time

def solve(data):
    on = set()
    for line in data:
        line = line.strip()
        instruction = line.split()[0]
        x = line.split(",")[0].split("=")[1]
        min_x = max(-50, int(x.split("..")[0]))
        max_x = min(50, int(x.split("..")[1]))
        y = line.split(",")[1].split("=")[1]
        min_y = max(-50, int(y.split("..")[0]))
        max_y = min(50, int(y.split("..")[1]))
        z = line.split(",")[2].split("=")[1]
        min_z = max(-50, int(z.split("..")[0]))
        max_z = min(50, int(z.split("..")[1]))
        pass
        for x1 in range(min_x, max_x + 1):
            for y1 in range(min_y, max_y + 1):
                for z1 in range(min_z, max_z + 1):
                    if instruction == "on":
                        on.add((x1,y1,z1))
                    else:
                        on.discard((x1,y1,z1))
    return len(on)

if __name__ == "__main__":
    with open("22/input.txt", "r") as f:
        data = f.readlines()
        start = process_time()
        print(solve(data))
        print(f"Part 1 finished in {process_time() - start}s")
# on x=-20..26,y=-36..17,z=-47..7
