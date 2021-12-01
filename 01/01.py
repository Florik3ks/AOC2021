def solve1(data):
    return len([i for i in range(len(data) - 1) if (int(data[i + 1]) > int(data[i]))])

def solve2(data):
    return len([i for i in range(len(data) - 3) if int(data[i + 1]) + int(data[i + 2]) + int(data[i + 3]) > int(data[i]) + int(data[i + 1]) + int(data[i + 2])])


print(solve1(open("input.txt").readlines()))
print(solve2(open("input.txt").readlines()))