def solve1(data):
    h = 0
    d = 0
    
    for line in data:
        value = int(line.split()[1])
        direction = line.split()[0]
        if direction == "forward": h+=value
        if direction == "down": d+=value
        if direction == "up": d-=value
    return h * d

def solve2(data):
    h = 0
    d = 0
    a = 0    
    for line in data:
        value = int(line.split()[1])
        direction = line.split()[0]
        if direction == "forward": h+=value;d+=value * a
        if direction == "down": a+=value
        if direction == "up": a-=value
    return h * d

print(solve1(open("02/input.txt")))
print(solve2(open("02/input.txt")))
        