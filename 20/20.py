from time import process_time

def solve(data, steps):
    lookup = data[0].strip()
    data = data[2:]
    infinite_grid_char = '.'
    for step in range(steps):
        extend_grid(data, 1, infinite_grid_char)
        new_data = []
        for y in range(len(data)):
            new_data.append("")
            for x in range(len(data[y].strip())):
                num = get_neighbours(data,x,y,infinite_grid_char)
                new_data[y] += lookup[num]
        data = new_data
        infinite_grid_char = lookup[0] if infinite_grid_char == '.' else lookup[-1]
    
    count = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '#':
                count += 1
    return count

def extend_grid(data, n, c):
    for _ in range(n):
        data.insert(0, c * len(data[0].strip()))
        data.append(c * len(data[0].strip()))
        for y in range(len(data)):
            data[y] = c + data[y].strip() + c
        
def get_neighbours(data, x, y, c):
    max_y = len(data) - 1
    max_x = len(data[0].strip()) - 1
    neighbours = []
    for nx, ny in ([-1, -1], [0, -1], [1, -1], [-1, 0], [0, 0], [1, 0], [-1, 1], [0, 1], [1, 1]):
        if 0 <= x + nx <= max_x and 0 <= y + ny <= max_y:
            neighbours.append(data[ny + y][nx + x])
        else:
            neighbours.append(c)
    result = ""
    for n in neighbours:
        result += '0' if n == '.' else '1'
    return int(result, 2)

if __name__ == "__main__":
    with open("20/input.txt", "r") as f:
        data = f.readlines()
        start = process_time()
        print(solve(data, 2))
        print(f"Part 1 finished in {process_time() - start}s")
        start = process_time()
        print(solve(data, 50))
        print(f"Part 2 finished in {process_time() - start}s")
#5391