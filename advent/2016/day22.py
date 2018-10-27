from collections import namedtuple

nodes = {}
Node = namedtuple('Node', ['used', 'avail'])
x_max = 0
y_max = 0

def from_num(terabyte_str):
    return int(terabyte_str[:-1])

def node_name(x, y):
    return '/dev/grid/node-x{}-y{}'.format(x, y)

def get_node_coords(node):
    _, x_str, y_str = node.split('-')
    return int(x_str[1:]), int(y_str[1:])

def get_neighbors(node):
    results = []
    x, y = get_node_coords(node)
    if x > 0: results.append(node_name(x-1, y))
    if y > 0: results.append(node_name(x, y-1))
    if x < x_max: results.append(node_name(x+1, y))
    if y < y_max: results.append(node_name(x, y+1))
    return results

with open('22.txt') as f:
    f.next()
    f.next()
    for line in f:
        filename, _, used, avail, _ = line.strip().split()
        nodes[filename] = Node(from_num(used), from_num(avail))
        x, y = get_node_coords(filename)
        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y

# part 1
# answer was 985

viable_count = 0
for node_a in nodes:
    for node_b in nodes:
        if (node_a != node_b
                and nodes[node_a].used > 0
                and nodes[node_a].used < nodes[node_b].avail):
            viable_count += 1

print(viable_count)

# part 2
