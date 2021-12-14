from collections import Counter, defaultdict

def solve(data):
    start = data[0].strip()
    instructions = []
    for l in range(2, len(data)):
        line = data[l].strip()
        old, new = line.split(" -> ")
        instructions.append((old, new))
    
    for _ in range(10):
        result = ""
        for i in range(0, len(start) - 1):
            pair = start[i] + start[i + 1]
            result += pair[0]
            for instruction in instructions:
                if pair == instruction[0]:
                    result += instruction[1]
                    break
            if i == len(start) - 2:
                result += pair[1]
            # result += pair[1]
        start = result
        
    minval = 31**2 - 1
    maxval = 0
    for v in Counter(result).values():
        minval = min(minval, v)
        maxval = max(maxval, v)
    return maxval - minval

def solve2(data):
    start = data[0].strip()
    instructions = []
    replacements = {}
    for l in range(2, len(data)):
        line = data[l].strip()
        old, new = line.split(" -> ")
        instructions.append((old, new))
        replacements[old] = old[0] + new
    replacer = replacements.get
    for _ in range(40):

        values = list(generate_multiple_sets_of_two(start))
        start = ''.join([replacer(n, n) for n in values]) + start[len(start) - 1]
      
    minval = 2 ** 31 - 1
    maxval = 0
    for v in Counter(start).values():
        minval = min(minval, v)
        maxval = max(maxval, v)
    return maxval - minval

def solve2(data):
    start = data[0].strip()
    instructions = {}
    quantities = defaultdict(int)
    for l in range(2, len(data)):
        line = data[l].strip()
        old, new = line.split(" -> ")
        instructions[old] = new
    
    for chunk in generate_multiple_sets_of_two(start):
        quantities[chunk] += 1

    for _ in range(40):
        new_quantities = defaultdict(int)
        for chunk, quantity in quantities.items():
            new_quantities[chunk[0] + instructions[chunk]] += quantity
            new_quantities[instructions[chunk] + chunk[1]] += quantity
        quantities = new_quantities
      
    occurences = defaultdict(int)
    for k, v in quantities.items():
        occurences[k[0]] += v
    occurences[start[-1]] += 1
    minval = float('inf')
    maxval = 0
    for v in occurences.values():
        minval = min(minval, v)
        maxval = max(maxval, v)
    return maxval - minval

def generate_multiple_sets_of_two(string):
    for i in range(0, len(string) - 1):
        yield string[i:i + 2]
with open("14/input.txt", "r") as f:
    data = f.readlines()
    print(solve(data))
    print(solve2(data))
    