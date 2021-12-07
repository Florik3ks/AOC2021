def solve(data):
    crabs = [int(x) for x in data.split(",")]
    fuel = 0
    min_fuel = 2**31 - 1
    _max = 0
    _min = 2**31 - 1
    for c in crabs:
        _max = max(_max, c)
        _min = min(_min, c)
    for p in range(_min, _max):
        fuel = 0
        for c in crabs:
            fuel += abs(c - p)
        min_fuel = min(fuel, min_fuel)
    return min_fuel


def solve2(data):
    crabs = [int(x) for x in data.split(",")]
    fuel = 0
    min_fuel = 2**31 - 1
    _max = 0
    _min = 2**31 - 1
    for c in crabs:
        _max = max(_max, c)
        _min = min(_min, c)
    for p in range(_min, _max):
        fuel = 0
        for c in crabs:
            n = abs(c-p)
            fuel += (n**2 + n) // 2
        min_fuel = min(fuel, min_fuel)
    return min_fuel

print(solve(open("07/input.txt").readlines()[0].strip()))
print(solve2(open("07/input.txt").readlines()[0].strip()))