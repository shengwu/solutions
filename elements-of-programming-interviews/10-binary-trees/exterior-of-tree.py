class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_exterior(root):
    return exterior(root, 'root')

def is_leaf(node):
    return node.left == None and node.right == None

def exterior(node, case):
    if node == None:
        return []
    if is_leaf(node):
        return [node.val]
    if case == 'interior':
        return exterior(node.left, 'interior') + exterior(node.right, 'interior')
    if case == 'root':
        return [node.val] \
                + exterior(node.left, 'left')\
                + exterior(node.right, 'right')
    if case == 'left':
        return [node.val] \
                + exterior(node.left, 'left')\
                + exterior(node.right, 'interior')
    # case == 'right'
    return exterior(node.left, 'interior')\
            + exterior(node.right, 'right')\
            + [node.val]

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')
h = Node('H')
i = Node('I')
j = Node('J')
k = Node('K')
l = Node('L')
m = Node('M')
n = Node('N')
o = Node('O')
p = Node('P')

a.left = b
a.right = i
b.left = c
b.right = f
c.left = d
c.right = e
f.right = g
g.left = h
i.left = j
j.right = k
k.left = l
l.right = m
k.right = n
i.right = o
o.right = p

# expect A B C D E H M N P O I
print get_exterior(a)
