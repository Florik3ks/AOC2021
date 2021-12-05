from collections import defaultdict
from math import copysign

def print_debug(d):
    max_x = 0
    max_y = 0
    for k in d.keys():
        x,y = k
        max_x = max(max_x, int(x))
        max_y = max(max_y, int(y))
    for y in range(max_y + 1):
        row_str = ""
        for x in range(max_x + 1):
            row_str += str(d[str(x),str(y)]) if d[str(x),str(y)] != 0 else "."
        print(row_str)

def solve1(data):
    d = defaultdict(int)
    for line in data:
        x1, y1, x2, y2 = line.replace("\n","").replace(" -> ", ",").split(",")
        if x1 == x2:
            for i in range(min(int(y1), int(y2)), max(int(y1), int(y2)) + 1):
                d[x1, str(i)] += 1
        if y1 == y2:
            for i in range(min(int(x1), int(x2)), max(int(x1), int(x2)) + 1):
                d[str(i), y1] += 1
            
    count = 0
    for key in d.keys():
        if d[key] >= 2: count += 1
    return count

def solve2(data):
    d = defaultdict(int)
    for line in data:
        x1, y1, x2, y2 = line.replace("\n","").replace(" -> ", ",").split(",")
        if x1 == x2:
            for i in range(min(int(y1), int(y2)), max(int(y1), int(y2)) + 1):
                d[x1, str(i)] += 1
        if y1 == y2:
            for i in range(min(int(x1), int(x2)), max(int(x1), int(x2)) + 1):
                d[str(i), y1] += 1
        
        if (x1 == y2 and y1 == x2) or (x1 == x2 and y1 == y2) or (int(y2) - int(y1) == int(x2) - int(x1) or (int(x2) - int(x1) == int(y1) - int(y2))):
            x = int(x1)
            y = int(y1)
            while x != int(x2) + copysign(1, int(x2) - int(x1)):
                d[str(x), str(y)] += 1
                x += int(copysign(1, int(x2) - int(x1)))
                y += int(copysign(1, int(y2) - int(y1)))
            
    # print_debug(d)
    count = 0
    for key in d.keys():
        if d[key] >= 2: count += 1
    return count

print(solve1(open("05/example.txt").readlines()))
print(solve2(open("05/input.txt").readlines()))