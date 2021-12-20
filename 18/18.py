from time import process_time
from math import ceil, floor

class Tree():
    def __init__(self):
        self.root = []
        
class Node():
    def __init__(self, left = None, right = None):
        self.right = right
        self.left = left

def solve(data):
    tree = parse_tree(data[0].strip().split(" + ")[0])
    for line in data[1:]:
        line = line.strip()
        add_node(tree, split_pair_in_nodes(line))
        reduced = True
        while reduced:
            reduced = reduce(tree)
        # print_tree(tree)
    return get_magnitude(tree.root)

def solve2(data):
    max_magnitude = 0
    for line in data:
        for line2 in data:
            if line != line2:
                tree = parse_tree(line.strip().split(" + ")[0])
                line2 = line2.strip()
                add_node(tree, split_pair_in_nodes(line2))
                reduced = True
                while reduced:
                    reduced = reduce(tree)
                # print_tree(tree)
                max_magnitude = max(max_magnitude, get_magnitude(tree.root))
    return max_magnitude

def get_magnitude(node):
    if isinstance(node, int):
        return node
    if isinstance(node, Node):
        return get_magnitude(node.left) * 3 + get_magnitude(node.right) * 2

def print_tree(tree):
    print(print_nodes(tree.root))

def print_nodes(node):
    if isinstance(node, int):
        return str(node)
    result = "[" + print_nodes(node.left) + "," + print_nodes(node.right) + "]"
    return result
    
def add_node(tree, node):
    rootcpy = tree.root
    tree.root = Node(rootcpy, node)
    
def parse_tree(line):
    tree = Tree()
    tree.root = split_pair_in_nodes(line)
    return tree

def split_pair_in_nodes(pair_str):
    if pair_str[0] == "[" and pair_str[-1] == "]":
        pair_str = pair_str[1:-1]
    if pair_str == "":
        return Node()
    if pair_str.isdigit():
        return int(pair_str)
    if "[" not in pair_str:
        l, r = [int(x) for x in pair_str.split(",")]
        return Node(l, r)
    n = Node()
    bracket_stack = []
    for i in range(len(pair_str)):
        if pair_str[i] == "[":
            bracket_stack.append("[")
        elif pair_str[i] == "]":
            bracket_stack.pop()
        elif pair_str[i] == "," and len(bracket_stack) == 0:
            strings = [pair_str[:i], pair_str[i + 1:]]
            n.left = split_pair_in_nodes(strings[0])
            n.right = split_pair_in_nodes(strings[1])
            break
            
    return n

def reduce(tree):
    reduced = False
    reduced = try_explode(tree.root)
    if not reduced:
        reduced = try_split(tree.root)
    if reduced: return True
    return False
        
def try_explode(node, parent=None, depth = 0):
    exploding = False
    if max_depth(node, depth < 4):
        return False
    if depth == 4:
        return (node.left, node.right)
        
    if isinstance(node.left, Node):
        exploding = try_explode(node.left, node, depth + 1)
    if exploding:
        if depth == 3:
            node.left = 0
        if isinstance(node.right, int):
            node.right += exploding[1]
        else:
            add_left(node.right, exploding[1])
        return (exploding[0], 0)
    
    if isinstance(node.right, Node):
        exploding = try_explode(node.right, node, depth + 1)
    if exploding:
        if depth == 3:
            node.right = 0
        if isinstance(node.left, int):
            node.left += exploding[0]
        else:
            add_right(node.left, exploding[0])
        return (0, exploding[1])
    return None
    
def max_depth(node, depth = 0):
    maxdepth = 0
    if isinstance(node.left, Node):
        maxdepth = max(maxdepth, max_depth(node.left, depth + 1))
    if isinstance(node.right, Node):
        maxdepth = max(maxdepth, max_depth(node.right, depth + 1))
    return maxdepth

def add_left(node, number):
    if isinstance(node.left, int):
        node.left += number
        return
    add_left(node.left, number)
    return

def add_right(node, number):
    if isinstance(node.right, int):
        node.right += number
        return
    add_right(node.right, number)
    return  

def try_split(node):
    splitted = False
    if isinstance(node.left, int):
        if node.left >= 10:
            node.left = Node(floor(node.left / 2), ceil(node.left / 2)) 
            return True
    else: splitted = try_split(node.left)
    
    if not splitted:
        if isinstance(node.right, int):
            if node.right >= 10:
                node.right = Node(floor(node.right / 2), ceil(node.right / 2)) 
                return True
        else: splitted = try_split(node.right)        

    return splitted

if __name__ == "__main__":
    with open("18/input.txt", "r") as f:
        data = f.readlines()
        start = process_time()
        print(solve(data))
        print(f"Part 1 finished in {process_time() - start}s")
        
        start = process_time()
        print(solve2(data))
        print(f"Part 2 finished in {process_time() - start}s")