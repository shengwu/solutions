from collections import defaultdict, deque

def delta(letter):
    return {
        'E': (0, 1),
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
    }[letter]

def apply_delta(curr, delta):
    return (curr[0] + delta[0], curr[1] + delta[1])

def traverse(exp, curr_loc, edges):
    i = 0
    orig_loc = curr_loc
    while i < len(exp):
        e = exp[i]
        if e == '(':
            i += traverse(exp[i+1:], curr_loc, edges)
        elif e == ')':
            return i + 1
        elif e == '|':
            curr_loc = orig_loc
        else:
            assert e in 'NEWS'
            old = curr_loc
            curr_loc = apply_delta(curr_loc, delta(e))
            edges[old].add(curr_loc)
        i += 1
    return None

def furthest(edges, start=(0, 0)):
    q = deque([(0,) + start])
    visited = set()
    max_dist = 0
    at_least_a_thousand_away = 0
    while q:
        dist, x, y = q.popleft()
        if dist > max_dist:
            max_dist = dist
        if dist >= 1000:
            at_least_a_thousand_away += 1
        for neighbor in edges[(x, y)]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((dist+1,) + neighbor)
    return max_dist, at_least_a_thousand_away

def get_furthest(regex):
    edges = defaultdict(set)
    traverse(regex, (0, 0), edges)
    return furthest(edges)

regex = open('20.txt').read().strip()[1:-1]

assert get_furthest('WNE') == (3, 0)
assert get_furthest('ENWWW(NEEE|SSE(EE|N))') == (10, 0)
assert get_furthest('ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN') == (18, 0)
assert get_furthest('ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))') == (23, 0)
assert get_furthest('WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))') == (31, 0)
print get_furthest(regex)
