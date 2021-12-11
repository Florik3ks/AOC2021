def solve(inp):
    data = []
    for y in range(len(inp)):
        data.append([])
        for x in inp[y].strip():
            data[y].append(x)
            
    d1 = 0
    d = 0
    flashes = 0
    flashed = []
    while len(flashed) != 100:
        if d == 100:
            d1 = flashes
        d += 1
        flashed = []
        for y in range(len(data)):
            for x in range(len(data[y])):
                data[y][x] = int(data[y][x]) + 1
                if int(data[y][x]) > 9:
                    if (y, x) not in flashed:
                        flashed.append((y,x))
                
        for py, px in flashed:
            flashes += get_neighbours_of_flashing_octopus(data, px, py, flashed)
        for py, px in flashed:
            data[py][px] = 0
    d2 = d
    show(data)
    return d1, d2

def show(data):
    res = ""
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] > 9:
                res += "0"
            else:
                res += str(data[y][x])
        res += "\n"
    print(res + "\n")
    
def get_neighbours_of_flashing_octopus(data, x, y, flashed):
    max_y = len(data) - 1
    max_x = len(data[0]) - 1
    neighbours = []
    for nx, ny in ([-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]):
        if 0 <= x + nx <= max_x and 0 <= y + ny <= max_y:
            neighbours.append((ny + y, nx + x))
    f = 1
    flashing_n = []
    for py, px in neighbours:
        data[py][px] = int(data[py][px]) + 1
        if (py, px) not in flashed:
            if int(data[py][px]) > 9:
                flashed.append((py, px))
                flashing_n.append((py, px))
    for py, px in flashing_n:
        if (py, px) not in flashed:
            flashed.append((py, px))
            f += get_neighbours_of_flashing_octopus(data, px, py, flashed)
        
    return f

with open("11/input.txt", "r") as f:
    data = f.readlines()
    print(solve(data))