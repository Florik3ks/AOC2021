def solve(data):
    grid = []
    positions = []
    instructions = []
    for line in data:
        line = line.strip()
        if not line.startswith("fold") and line != "":
            positions.append([int(x) for x in line.split(",")])
        elif line != "":
            asx =  line.split("fold along ")[1]
            axis, value = asx.split("=")
            instructions.append((axis, value))
            
    # d1
    axis, value = instructions[0]
    value = int(value)
    for p in positions.copy():
        p = get_new_val(p, axis, value)
        positions.remove(p)
        if p in positions:
            positions.remove(p)
        positions.append(p)
    d1 = len(positions)

    instructions.pop(0)
    
    # d2
    for axis, value in instructions:
        value = int(value)
        for p in positions.copy():
            p = get_new_val(p, axis, value)
            positions.remove(p)
            if p in positions:
                positions.remove(p)
            positions.append(p)
    
    print_grid(positions)
    return 

def get_new_val(p, axis, val):
    val = int(val)
    if axis == "y":
        if p[1] < val:
            return p
        i = 1
    elif axis == "x":
        if p[0] < val:
            return p
        i =  0
    dist_to_border = p[i] - val
    p[i] = val - dist_to_border
    return p
    
def print_grid(positions):    
    max_x = 0
    max_y = 0
    printing_grid = []
    for p in positions:
        max_x = max(max_x, p[0])
        max_y = max(max_y, p[1])
    max_x += 1
    max_y += 1
    for y in range(max_y):
        printing_grid.append(["." for x in range(max_x)])
    for p in positions:
        printing_grid[p[1]][p[0]] = "#"  
    
    for y in range(max_y):
        print(''.join(printing_grid[y]))
        
with open("13/input.txt", "r") as f:
    data = f.readlines()
    print(solve(data))