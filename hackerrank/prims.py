from collections import defaultdict
import heapq

edges = defaultdict(list)
n, m = map(int, raw_input().split())
for _ in xrange(m):
    x, y, r = map(int, raw_input().split())
    edges[x].append((y, r))
    edges[y].append((x, r))
    
start = input()
visited = set()
q = [(0, start)]
total = 0
while len(visited) < n:
    weight, node = heapq.heappop(q)
    # seems inelegant to do two checks
    if node in visited:
        continue
    visited.add(node)
    total += weight
    for neighbor, wt in edges[node]:
        if neighbor not in visited:
            heapq.heappush(q, (wt, neighbor))
print total
