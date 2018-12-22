from collections import deque
import heapq

depth = 4080
target = (14, 785)
mod = 20183

#depth = 510
#target = (10, 10)

cache = {}
def geo(x, y):
    if (x, y) in cache:
        return cache[(x, y)]
    if (x, y) == target:
        return 0
    if x == 0:
        return (y * 48271) % mod
    if y == 0:
        return (x * 16807) % mod
    result = (erosion(x-1, y) * erosion(x, y-1)) % mod
    cache[(x, y)] = result
    return result

def erosion(x, y):
    result = (geo(x, y) + depth) % mod
    return result

def risk(x, y):
    return erosion(x, y) % 3

# part 1

r = 0
for i in range(target[0]+1):
    for j in range(target[1]+1):
        r += risk(i, j)
print r

# part 2

def excluded(x, y):
    return ('neither', 'torch', 'gear')[erosion(x, y) % 3]

def neighbors(x, y):
    n = []
    if x > 0:
        n.append((x-1, y))
    if y > 0:
        n.append((x, y-1))
    n.append((x, y+1))
    n.append((x+1, y))
    return n

gears = frozenset(['neither', 'torch', 'gear'])

dist = {}
dist[('torch', 0, 0)] = 0
q = [(0, 'torch', 0, 0)]
while q:
    cost, gear, x, y = heapq.heappop(q)
    if (gear, x, y) == (('torch',) + target):
        print cost
        break
    for i, j in neighbors(x, y):
        if gear == excluded(i, j):
            # can only switch to equipment valid for your CURRENT location
            for choice in gears - set([gear]) - set([excluded(x, y)]):
                new_cost = cost + 8
                if (choice, i, j) not in dist or new_cost < dist[(choice, i, j)]:
                    dist[(choice, i, j)] = new_cost
                    heapq.heappush(q, (new_cost, choice, i, j))
        else:
            new_cost = cost + 1
            if (gear, i, j) not in dist or new_cost < dist[(gear, i, j)]:
                dist[(gear, i, j)] = new_cost
                heapq.heappush(q, (new_cost, gear, i, j))
