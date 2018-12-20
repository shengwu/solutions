from collections import defaultdict, deque

def delta(letter):
    return {
        'E': (0, 1),
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
    }[letter]

def step(curr, letter):
    d = delta(letter)
    return (curr[0] + d[0], curr[1] + d[1])

def traverse(exp, curr, edges, vertices):
    i = 0
    orig_loc = curr
    while i < len(exp):
        #print exp, curr, i
        #raw_input()
        e = exp[i]
        if e == '(':
            i += traverse(exp[i+1:], curr, edges, vertices) + 1
        elif e == ')':
            return i
        elif e == '|':
            curr = orig_loc
        else:
            assert e in 'NEWS'
            edges[curr].add(delta(e))
            curr = step(curr, e)
            vertices.add(curr)
        i += 1
    return None



def furthest(vertices, edges, start=(0, 0)):
    q = deque([(0,) + start])
    visited = set()
    max_dist = 0
    at_least_a_thousand_away = 0
    while q:
        dist, x, y = q.popleft()
        if dist > max_dist:
            #print x, y
            max_dist = dist
        if dist >= 1000:
            at_least_a_thousand_away += 1
        for i, j in edges[(x, y)]:
            nx, ny = x+i, y+j
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((dist+1, nx, ny))
    return max_dist, at_least_a_thousand_away


def get_furthest(regex):
    start = (0, 0)
    vertices = set([start])
    edges = defaultdict(set)
    traverse(regex, start, edges, vertices)
    #print vertices, edges
    return furthest(vertices, edges)


regex = open('20.txt').read().strip()[1:-1]

assert get_furthest('WNE') == (3, 0)
assert get_furthest('ENWWW(NEEE|SSE(EE|N))') == (10, 0)
assert get_furthest('ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN') == (18, 0)
assert get_furthest('ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))') == (23, 0)
assert get_furthest('WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))') == (31, 0)
print get_furthest(regex)
