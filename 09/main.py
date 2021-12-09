def solve(data):
    count = 0
    max_y = len(data) - 1
    max_x = len(data[0].strip()) - 1
    for y in range(len(data)):
        data[y] = data[y].strip()
        for x in range(len(data[y])):
            points = []
            if x > 0: points.append(data[y][x-1])     
            if y > 0: points.append(data[y-1][x])     
            if x < max_x: points.append(data[y][x+1])     
            if y < max_y: points.append(data[y+1][x])
            greater = True
            for p in points:
                if int(p) <= int(data[y][x]):
                    greater = False
            if greater:
                count += 1 + int(data[y][x])     
    return count

class Point():
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Point):
            return __o.value == self.value and __o.x == self.x and __o.y == self.y
        return False
    
def solve2(data):
    count = 0
    max_y = len(data) - 1
    max_x = len(data[0].strip()) - 1
    possible_basin_startpoints = []
    for y in range(len(data)):
        data[y] = data[y].strip()
        for x in range(len(data[y])):
            points = []
            if x > 0: points.append(data[y][x-1])     
            if y > 0: points.append(data[y-1][x])     
            if x < max_x: points.append(data[y][x+1])     
            if y < max_y: points.append(data[y+1][x])
            greater = True
            for p in points:
                if int(p) <= int(data[y][x]):
                    greater = False
            if greater:
                possible_basin_startpoints.append(Point(int(data[y][x]),x,y))
    basins = []
    for bp in possible_basin_startpoints:
        basin_height = 0
        neighbours = []      
        computed = []
        neighbours.append(bp)
        while len(neighbours) > 0:
            basin_height += 1
            computed.append(neighbours[0])
            get_adjacent_points_smaller_than_nine(data, neighbours.pop(0), neighbours, computed)
        basins.append(basin_height)
 
    value = 1
    for i in range(3):
        m = 0
        for b in basins:
            m = max(m, b)
        basins.remove(m)
        value *= m
    return value    

def get_adjacent_points_smaller_than_nine(data, p : Point, out : list, computed):
    max_y = len(data) - 1
    max_x = len(data[0].strip()) - 1
    x = p.x
    y = p.y
    neighbours = []
    if x > 0: neighbours.append(Point(int(data[y][x-1]), x-1, y))     
    if y > 0: neighbours.append(Point(int(data[y-1][x]), x, y-1))     
    if x < max_x: neighbours.append(Point(int(data[y][x+1]), x+1, y))     
    if y < max_y: neighbours.append(Point(int(data[y+1][x]), x, y+1))
    for p in neighbours.copy():
        if p.value == 9:
            neighbours.remove(p)
        elif p not in out and p not in computed:
            out.append(p)
    
print(solve(open("09/input.txt").readlines()))
print(solve2(open("09/input.txt").readlines()))