from time import process_time

def solve(data):
    rectangle = [int(x) for x in data[0].strip().replace(" ", "").replace("targetarea:", "").replace(",","..").replace("x=","").replace("y=","").split("..")]
    max_y = 0
    targets = set()
    for x in range(10, rectangle[1] + 1):
        for y in range(rectangle[2] - 1, 250):
            velocity = [x, y]
            local_max_y = 0
            position = [0, 0]
            while position[0] <= rectangle[1] + 1 and position[1] >= rectangle[2]:
                position[0] += velocity[0]
                position[1] += velocity[1]
                local_max_y = max(local_max_y, position[1])
                if velocity[0] < 0: velocity[0] += 1
                elif velocity[0] > 0: velocity[0] -= 1
                velocity[1] -= 1
                if is_in_rect(rectangle, position[0], position[1]):
                    max_y = max(local_max_y, max_y)
                    targets.add((x,y))
    return max_y, len(targets)
 
def is_in_rect(rect, px, py):
    return rect[0] <= px <= rect[1] and rect[2] <= py <= rect[3]

if __name__ == "__main__":
    with open("17/input.txt", "r") as f:
        data = f.readlines()
        start = process_time()
        print(solve(data))
        print(f"finished in {process_time() - start}s")