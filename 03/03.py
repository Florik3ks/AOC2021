from collections import defaultdict
def solve(data):
    bits = defaultdict(lambda: defaultdict(int))
    
    for line in data:
        for i in range(len(line)):
            bit = line[i]
            if bit == "1" or bit == "0":
                bits[i][bit] += 1
            
    new_bits = []
    for pos in bits.keys():
        if bits[pos]["0"] > bits[pos]["1"]:
            new_bits.append(0)
        else:
            new_bits.append(1)
                   
    gamma_rate = ''.join([str(x) for x in new_bits])
    epsilon_rate = ''.join(["0" if x == 1 else "1" for x in new_bits])
    return int(gamma_rate, 2) * int(epsilon_rate, 2)
    
def solve2(data):
    bits = defaultdict(lambda: defaultdict(int))

    oxygen = data.copy()
    co2 = data.copy()
    for pos in range(len(oxygen[0])):
        if oxygen[0][pos] != "1" and oxygen[0][pos] != "0":
            continue
        nums = defaultdict(int)
        for line in oxygen:
            nums[line[pos]] += 1
        
        if nums["1"] >= nums["0"]:
            num = "1"
        else:
            num = "0"
        c = 0
        for i in range(len(oxygen)):
            if oxygen[i - c][pos] != num:
                oxygen.remove(oxygen[i - c])
                c += 1
                if len(oxygen) == 1: break
        if len(oxygen) == 1: break    
            
    for pos in range(len(co2[0])):
        if co2[0][pos] != "1" and co2[0][pos] != "0":
            continue
        nums = defaultdict(int)
        for line in co2:
            nums[line[pos]] += 1
        
        if nums["0"] <= nums["1"]:
            num = "0"
        else:
            num = "1"
        c = 0
        for i in range(len(co2)):
            if co2[i - c][pos] != num:
                co2.remove(co2[i - c])
                c += 1
                if len(co2) == 1: break
        if len(co2) == 1: break
    return int(co2[0], 2) * int(oxygen[0], 2)

    
    
print(solve(open("03/input.txt").readlines()))
print(solve2(open("03/input.txt").readlines()))