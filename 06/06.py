
# slow for d2
def solve(data, days=80):
    fishes = [int(x) for x in data[0].split(",")]
    for d in range(days):
        for i in range(len(fishes)):
            if fishes[i] == 0:
                fishes[i] = 6
                fishes.append(8)
            else:
                fishes[i] -= 1

    return len(fishes)

# region tries

# def solve2(data, days=256):
#     fishes = [int(x) for x in data[0].split(",")]
#     return sum([2 ** ((days-fish) // 8) for fish in fishes])

# def solve2(data, days=80):
#     fishes = [int(x) for x in data[0].split(",")]
#     return rek(fishes, days)

# def rek(fishes, days_left):
#     if days_left == 0:
#         return 0
#     count = 0
#     for f in fishes.copy():
#         count += (days_left - f) // 6
#         fishes.remove(f)
#     return rek(fishes, days_left - 1) + count

# endregion tries

def solve2(data, days=256):
    fish_states = {i : 0 for i in range(9)}
    for fish in data[0].split(","):
        fish_states[int(fish)] += 1
        
    for d in range(days):
        tmp = 0
        for i in range(9):
            if i == 0:
                tmp = fish_states[0]
            else:
                fish_states[i - 1] = fish_states[i]
        fish_states[8] = tmp
        fish_states[6] += tmp
    
    c = 0
    for key in fish_states.keys():
        c += fish_states[key]
    return c



print(solve(open("06/input.txt").readlines()))
print(solve2(open("06/input.txt").readlines()))
