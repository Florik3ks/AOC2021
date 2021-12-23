from time import process_time
from collections import defaultdict
from functools import lru_cache


def solve(data):
    positions = [int(data[0].split()[-1]), int(data[1].split()[-1])]
    score = [0, 0]
    die = 1
    player = 0
    total_rolls = 0
    while max(score) < 1000:
        roll = 0
        for i in range(3):
            roll += die
            die += 1
            if die > 100:
                die = 1
            total_rolls += 1

        new_pos = positions[player] + roll
        positions[player] = new_pos % 10
        if positions[player] == 0:
            positions[player] = 10

        score[player] += positions[player]
        player = 1 if player == 0 else 0

    return min(score) * total_rolls


def solve2(data):
    possible_rolls = []
    for i in range(1, 4):
        for j in range(1, 4):
            for z in range(1, 4):
                possible_rolls.append(i+j+z)
    positions = [int(data[0].split()[-1]), int(data[1].split()[-1])]
    
    total_wins = {0: 0, 1: 0}
    state = (positions[0], 0, positions[1], 0, 0)
    states = {state : 1}

    while len(states.keys()) > 0:
        new_states = defaultdict(int)
        for k in states.keys():
            (p0, s0, p1, s1, player) = k
            for roll in possible_rolls:
                if player == 0:
                    new_pos = (p0 + roll) % 10
                    if new_pos == 0: new_pos = 10
                    score = new_pos + s0
                    if score >= 21:
                        total_wins[player] += states[k]
                    else:
                        new_states[(new_pos, score, p1, s1, 1)] += states[k]
                else:
                    new_pos = (p1 + roll) % 10
                    if new_pos == 0: new_pos = 10
                    if new_pos == 0: new_pos = 10
                    score = new_pos + s1
                    if score >= 21:
                        total_wins[player] += states[k]
                    else:
                        new_states[(p0, s0, new_pos, score, 0)] += states[k]
        states = new_states
    return max(total_wins.values())

# alternative Version
# @lru_cache(maxsize=None)
# def compute(p0, s0, p1, s1, player):
#     if s0 >= 21: return (1, 0)
#     if s1 >= 21: return (0, 1)
    
#     p0_wins = 0
#     p1_wins = 0
#     # for roll in possible_rolls:
#     for i in range(1, 4):
#         for j in range(1, 4):
#             for z in range(1, 4):
#                 roll = i+j+z
#                 if player == 0:
#                     new_pos = (p0 + roll) % 10
#                     if new_pos == 0:
#                         new_pos = 10
#                     score = new_pos + s0
                    
#                     wins = compute(new_pos, score, p1, s1, 1)
#                 else:
#                     new_pos = (p1 + roll) % 10
#                     if new_pos == 0:
#                         new_pos = 10
#                     score = new_pos + s1

#                     wins = compute(p0, s0, new_pos, score, 0)
                    
#                 p0_wins += wins[0]
#                 p1_wins += wins[1]
#     return (p0_wins, p1_wins)

if __name__ == "__main__":
    with open("21/input.txt", "r") as f:
        data = f.readlines()
        start = process_time()
        print(solve(data))
        print(f"Part 1 finished in {process_time() - start}s")
        start = process_time()
        print(solve2(data))
        print(f"Part 2 finished in {process_time() - start}s")
