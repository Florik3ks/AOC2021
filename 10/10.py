def solve(data):
    d = {"open" : ["[","(","{","<"],
         "close": ["]",")","}",">"]}
    nums = {")": 3, "]": 57, "}":1197,">":25137}
    count = 0
    for line in data:
        brackets = []
        for c in line.strip():
            if c in d["open"]:
                brackets.append(c)
            elif c in d["close"]:
                if len(brackets) == 0:
                    continue
                # corrupted
                index = d["open"].index(brackets[-1])
                if c != d["close"][index]:
                    count += nums[c]
                    break
                else:
                    brackets.pop(len(brackets) - 1)

    return count


def solve2(data):
    d = {"open" : ["[","(","{","<"],
         "close": ["]",")","}",">"]}
    nums = {")": 1, "]": 2, "}":3,">":4}
    scores = []
    for line in data:
        brackets = []
        is_corrupted = False
        for c in line.strip():
            if c in d["open"]:
                brackets.append(c)
            elif c in d["close"]:
                if len(brackets) == 0:
                    continue
                # corrupted
                index = d["open"].index(brackets[-1])
                if c != d["close"][index]:
                    is_corrupted = True
                    break
                else:
                    brackets.pop(len(brackets) - 1)
        if is_corrupted:
            continue
        brackets.reverse()
        score = 0
        for c in brackets:
            index = d["open"].index(c)
            score *= 5
            score += nums[d["close"][index]]
        scores.append(score)
        

    scores.sort()
    return scores[(len(scores) // 2)]

print(solve(open("10/input.txt").readlines()))
print(solve2(open("10/input.txt").readlines()))