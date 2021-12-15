import time
from collections import defaultdict

def solve(data):
    graph = {}
    distances = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y].strip())):
            n = Node(x, y, data[y][x], data)
            graph[(x,y)] = n
    start = (0, 0)
    end =  (len(data[0].strip()) - 1, len(data) - 1)
    start = get_node_at(0, 0, graph)
    start.set_distance(0, distances)
    
    d = dijkstra(start, graph, distances, end[0], end[1])
    return d

class Node():
    def __init__(self, x, y, value, grid):
        self.x = x
        self.y = y
        self.value = int(value)
        self.previous = None
        self.distance = float('inf')
        self.adjacent = get_adjacent(grid, x, y)
        
    def get_adjacent_nodes(self, graph):
        res = []
        for a in self.adjacent:
            tmp = get_node_at(a[1], a[0], graph)
            if tmp != None:
                res.append(tmp)
        return res
    
    def set_distance(self, distance, distances):
        distance = float(distance)
        old_dist = self.distance
        if self in distances[old_dist]:
            distances[old_dist].remove(self)
        self.distance = distance
        distances[distance].append(self)
        if len(distances[old_dist]) == 0:
            del distances[old_dist]
        
def get_adjacent(grid, x, y):
    points = []
    if x > 0: points.append((y, x - 1))     
    if y > 0: points.append((y - 1, x))     
    if x < len(grid[0]): points.append((y, x+1))     
    if y < len(grid): points.append((y+1, x))
    return points
def get_node_at(x, y, graph):
    if (x,y) in graph.keys():
        return graph[(x,y)]
    return None

def rm_min_node(distances):
    min_ = min(distances.keys())
    n = distances[min_][0]
    distances[min_].remove(n)
    if len(distances[min_]) == 0:
            del distances[min_]
    return n

def dijkstra(start, graph, distances, end_x, end_y):
    queue = [start]
    while len(queue) > 0:
        u = rm_min_node(distances)
        queue.remove(u)
        for v in u.get_adjacent_nodes(graph):
            dist = u.distance + v.value
            if v.distance > dist:
                v.set_distance(dist, distances)
                v.previous = u
                if v not in queue:
                    queue.append(v)
    end = get_node_at(end_x, end_y, graph)
    return int(end.distance)
  
def get_bigger_data(data):
    result = []
    for ny in range(5):
        for nx in range(5):
            advance_by = ny+nx
            for y in range(len(data)):
                result.append("")
                for x in range(len(data[y].strip())):
                    value = int(data[y][x]) + advance_by
                    while value > 9:
                        value -= 9
                    result[ny * len(data) + y] += str(value)

    for i in range(len(result) - 1, 0, -1):
        if result[i] == "":
            result.pop(i)
    return result
 
if __name__ == "__main__":
    with open("15/input.txt", "r") as f:
        data = f.readlines()
        #d1 ~ 0.5s
        start_time = time.process_time()
        print(solve(data))
        print(f"{time.process_time() - start_time}s elapsed")
        #d2 ~ 19.5s: room for improvement
        data = get_bigger_data(data)
        start_time = time.process_time()
        print(solve(data))
        print(f"{time.process_time() - start_time}s elapsed")        
