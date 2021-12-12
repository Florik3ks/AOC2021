class Node():
    def __init__(self, name):
        self.neighbours = []
        self.name = name
        self.is_small = self.name.islower()
        if self.is_small:
            self.can_be_visited = 2
        if self.name == "start":
            self.can_be_visited = 0

    def set_neighbour(self, n):
        self.neighbours.append(n)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Node):
            return self.name == o.name
        return False

    def __str__(self):
        return self.name

def get_node_by_name(nodes, name) -> Node:
    for n in nodes:
        if n.name == name:
            return n
    return None


def solve(data):
    nodes = []
    for line in data:
        node = line.strip().split("-")
        for n in node:
            if str(n) not in [str(x) for x in nodes]:
                nodes.append(Node(n))

    for line in data:
        node = line.strip().split("-")
        n0 = get_node_by_name(nodes, node[0])
        n1 = get_node_by_name(nodes, node[1])
        n0.set_neighbour(n1)
        n1.set_neighbour(n0)

    s = get_node_by_name(nodes, "start")
    p = []
    num = find_number_of_paths(nodes, s, True, get_node_by_name(nodes, "end"),[str(s)], p)
    # for p_ in p:
    #     print(p_)
    return num    

def find_number_of_paths(nodes, start, can_visit_single_double, end, current_path, paths):
    count = 0
    for n in start.neighbours:
        if n == end:
            count += 1
            current_path.append(str(n))
            paths.append(','.join(current_path))
            current_path.reverse()
            current_path.remove(str(n))
            current_path.reverse()
            continue
        
        can_visit = True
        changed_small = False
        visits_removed = 0
        if n.is_small: 
            if str(n) in current_path:
                if str(n) == "start":
                    can_visit = False
                else:
                    if can_visit_single_double:
                        can_visit_single_double = False
                        changed_small = True
                    else: can_visit = False
        if can_visit:
            current_path.append(str(n))
            count += find_number_of_paths(nodes, n, can_visit_single_double, end, current_path, paths)
            if changed_small:
                can_visit_single_double = True
            current_path.reverse()
            current_path.remove(str(n))
            current_path.reverse()
    return count


with open("12/input.txt", "r") as f:
    data = f.readlines()
    print(solve(data))
