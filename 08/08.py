def solve(data):
    d = {2: 1,
         4: 4,
         3: 7,
         7: 8}
    c = 0
    for line in data:
        for x in line.split("|")[1].split():
            if len(x) in d.keys():
                c += 1
    return c


def get_dict_entry_per_length(d, l):
    r = []
    for i in d.keys():
        if len(d[i]) == l:
            for x in d[i]:
                if x not in r:
                    r.append(x)
    return r



def solve2(data):
    count = 0
    for line in data:
        nums = line.split("|")[0].split()
        mapped = decode(nums)
        res = ""
        for val in line.split("|")[1].split():
            for k in mapped.keys():
                if len(k) != len(val):
                    continue
                skip = False
                for digit in val:
                    if digit not in k:    
                        skip = True    
                        break
                if skip: continue
                               
                res += str(mapped[k])
                break
        count += int(res)
    return count
    
    
    
def intersect(a,b):
    return list(set(a) & set(b))
def not_shared(a,b):
    return list(set(a) ^ set(b))

def decode(nums):
    one = remove_first_by_length(nums, 2)
    four = remove_first_by_length(nums, 4)
    seven = remove_first_by_length(nums, 3)
    eight = remove_first_by_length(nums, 7)
    
    nine = remove_first_by_func(nums, f"len(str(n)) == 6 and len(intersect('{four}', n)) == 4")
    six = remove_first_by_func(nums, f"len(str(n)) == 6 and len(not_shared('{seven}', n)) == 5")
    zero = remove_first_by_func(nums, f"len(str(n)) == 6")
    five = remove_first_by_func(nums, f"len(intersect(intersect('{nine}', '{six}'), n)) == 5")
    three = remove_first_by_func(nums, f"len(intersect('{one}', n)) == 2")
    two = nums[0]
    
    mapped = {
        zero : 0,
        one : 1,
        two : 2,
        three : 3,
        four : 4,
        five : 5,
        six : 6,
        seven : 7,
        eight : 8,
        nine : 9        
    }
    return mapped
    
def remove_first_by_length(nums, l):
    for n in nums:
        if len(n) == l:
            nums.remove(n)
            return n
def remove_first_by_func(nums, f):
    e = eval("lambda n: " + f)
    for n in nums:
        if e(n):
            nums.remove(n)
            return n
    
print(solve(open("08/input.txt").readlines()))
print(solve2(open("08/input.txt").readlines()))


# region old_part_two
# def solve2(data):
#     # d = {2: 1,
#     #      4: 4,
#     #      3: 7,
#     #      7: 8}
#     c = 0                          
#     pos = {
#         1: [3, 6],
#         2: [1, 3, 4, 5, 7],
#         3: [1, 3, 4, 6, 7],
#         4: [2, 3, 4, 6],
#         5: [1, 2, 4, 6, 7],
#         6: [1, 2, 4, 5, 6, 7],
#         7: [1, 3, 6],
#         8: [1, 2, 3, 4, 5, 6, 7],
#         9: [1, 2, 3, 4, 6, 7],
#         0: [1,2,3,5,6,7]
#     }
#     maps = defaultdict(list)
#     data = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
#     for line in data:
#         halves = line.split("|")
#         for h in halves:
#             for x in h.split():
#                 for digit in x:
#                     if len(maps[digit]) == 0:
#                         maps[digit] = get_dict_entry_per_length(pos, len(x))
#                     else:
#                         tmp = get_dict_entry_per_length(pos, len(x))
#                         for item in maps[digit].copy():
#                             if item not in tmp:
#                                 maps[digit].remove(item)
        
              
#         res = solve3(halves[1], maps, pos, list(pos.keys()))
#         c += int(res)
#     return res


# def solve3(h, maps, pos, poskeys):
#     res = ""
#     wc = []
#     for code in h.split().copy():
#         for k in poskeys:
#             positions_by_k = pos[k].copy()
#             mapped_positions = []
#             for digit in code:
#                 for i in maps[digit]:
#                     if len(maps[digit]) != 7:
#                         if i not in mapped_positions:
#                             mapped_positions.append(i)
#                     else:
#                         wc.append(digit)
                        
#             if len(wc) > 0:
#                 for wcitem in wc:
#                     m_backup = maps[wcitem]
#                     for i in range(1,8):
#                         maps[wcitem] = [i]
#                         r = solve3(h, maps, pos, poskeys)
#                         if r != "":
#                             return r
            
#             for i in positions_by_k:
#                 if i in mapped_positions:
#                     mapped_positions.remove(i)
                    
#             if len(positions_by_k) == 0 and len(pos[k]) == len(code):
#                 res += str(k)
                
#         h = ' '.join(h.split()[1:])
#     return res
# endregion old_part_two
