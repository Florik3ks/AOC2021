class Node():
    def __init__(self, name):
        self.neighbours = []
        self.name = name
        self.is_small = self.name.islower()

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
    num = find_number_of_paths(nodes, [s], s, get_node_by_name(nodes, "end"))
    return num


def find_number_of_paths(nodes, visited, start, end):
    count = 0
    for n in start.neighbours:
        if n == end:
            count += 1
            continue
        if str(n) not in [str(x) for x in visited]:
            if n.is_small:
                visited.append(n)
            count += find_number_of_paths(nodes, visited.copy(), n, end)
            if n.is_small:
                visited.remove(n)

    return count


with open("12/input.txt", "r") as f:
    data = f.readlines()
    print(solve(data))
