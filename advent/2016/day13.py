from collections import deque

inp = 1362

def is_wall(x, y):
    s = x*x + 3*x + 2*x*y + y + y*y + inp
    return sum(1 if dig == '1' else 0 for dig in bin(s)[2:]) % 2 == 1

def neighbors(x, y):
    result = [(x+1, y), (x, y+1)]
    if x > 0: result.append((x-1, y))
    if y > 0: result.append((x, y-1))
    return result

# run a bfs
# part 1 - answer was 82
def get_shortest(goal):
    q = deque([(1, 1, 0)])
    visited = set()
    while q:
        x, y, dist = q.popleft()
        if (x, y) == goal:
            return dist
        visited.add((x, y))
        for nx, ny in neighbors(x, y):
            if (nx, ny) not in visited and not is_wall(nx, ny):
                q.append((nx, ny, dist+1))

print get_shortest((31, 39))

# part 2 - answer was 138

def count_locs(limit):
    q = deque([(1, 1, 0)])
    visited = set()
    while q:
        x, y, dist = q.popleft()
        visited.add((x, y))
        if dist == limit:
            continue
        for nx, ny in neighbors(x, y):
            if (nx, ny) not in visited and not is_wall(nx, ny):
                q.append((nx, ny, dist+1))
    return len(visited)

print count_locs(50)
