from collections import Counter, defaultdict, namedtuple

inp = '''
Step E must be finished before step H can begin.
Step Y must be finished before step T can begin.
Step F must be finished before step S can begin.
Step U must be finished before step K can begin.
Step X must be finished before step Z can begin.
Step Q must be finished before step W can begin.
Step W must be finished before step O can begin.
Step G must be finished before step A can begin.
Step N must be finished before step H can begin.
Step S must be finished before step H can begin.
Step K must be finished before step C can begin.
Step J must be finished before step H can begin.
Step T must be finished before step B can begin.
Step C must be finished before step P can begin.
Step L must be finished before step V can begin.
Step Z must be finished before step A can begin.
Step M must be finished before step A can begin.
Step A must be finished before step P can begin.
Step V must be finished before step O can begin.
Step I must be finished before step O can begin.
Step P must be finished before step H can begin.
Step O must be finished before step D can begin.
Step R must be finished before step B can begin.
Step D must be finished before step B can begin.
Step B must be finished before step H can begin.
Step J must be finished before step L can begin.
Step T must be finished before step V can begin.
Step Z must be finished before step M can begin.
Step G must be finished before step B can begin.
Step K must be finished before step L can begin.
Step Z must be finished before step H can begin.
Step L must be finished before step M can begin.
Step X must be finished before step A can begin.
Step N must be finished before step M can begin.
Step G must be finished before step M can begin.
Step A must be finished before step V can begin.
Step G must be finished before step S can begin.
Step G must be finished before step J can begin.
Step L must be finished before step A can begin.
Step A must be finished before step H can begin.
Step T must be finished before step M can begin.
Step X must be finished before step N can begin.
Step P must be finished before step O can begin.
Step Y must be finished before step F can begin.
Step U must be finished before step G can begin.
Step G must be finished before step O can begin.
Step P must be finished before step D can begin.
Step G must be finished before step L can begin.
Step Z must be finished before step P can begin.
Step C must be finished before step L can begin.
Step E must be finished before step B can begin.
Step T must be finished before step Z can begin.
Step D must be finished before step H can begin.
Step U must be finished before step N can begin.
Step E must be finished before step V can begin.
Step L must be finished before step D can begin.
Step K must be finished before step Z can begin.
Step O must be finished before step R can begin.
Step V must be finished before step R can begin.
Step L must be finished before step O can begin.
Step T must be finished before step H can begin.
Step E must be finished before step Q can begin.
Step S must be finished before step T can begin.
Step U must be finished before step M can begin.
Step Q must be finished before step V can begin.
Step I must be finished before step B can begin.
Step L must be finished before step Z can begin.
Step Y must be finished before step B can begin.
Step J must be finished before step C can begin.
Step F must be finished before step Q can begin.
Step J must be finished before step D can begin.
Step Q must be finished before step L can begin.
Step I must be finished before step D can begin.
Step N must be finished before step V can begin.
Step U must be finished before step H can begin.
Step J must be finished before step R can begin.
Step K must be finished before step V can begin.
Step G must be finished before step P can begin.
Step Y must be finished before step X can begin.
Step L must be finished before step H can begin.
Step R must be finished before step D can begin.
Step S must be finished before step C can begin.
Step Q must be finished before step A can begin.
Step U must be finished before step X can begin.
Step V must be finished before step B can begin.
Step U must be finished before step Z can begin.
Step F must be finished before step P can begin.
Step G must be finished before step D can begin.
Step O must be finished before step H can begin.
Step C must be finished before step D can begin.
Step L must be finished before step P can begin.
Step N must be finished before step I can begin.
Step Q must be finished before step O can begin.
Step Q must be finished before step D can begin.
Step Z must be finished before step D can begin.
Step Y must be finished before step N can begin.
Step M must be finished before step O can begin.
Step W must be finished before step R can begin.
Step S must be finished before step D can begin.
Step O must be finished before step B can begin.
Step I must be finished before step P can begin.
'''

rows = inp.strip().split('\n')

parents = defaultdict(list)
for row in rows:
    parts = row.split()
    parents[parts[-3]].append(parts[1])

vertices = set(parents.keys() + [v for lst in parents.values() for v in lst])

seq = []
def avail(v): return all(dep in seq for dep in parents[v])
def next_avail(): return sorted(set(filter(avail, vertices)) - set(seq))[0]
while len(seq) < len(vertices):
    seq.append(next_avail())

print ''.join(seq)


# part 2
visited = set()
pool_size = 5
pool = set()
t = 0
Worker = namedtuple('Worker', ('item', 'time_started'))

def cost(let): return ord(let) - ord('A') + 61
def avail(v): return all(dep in visited for dep in parents[v])
def next_avail():
    all_avail = set(filter(avail, vertices))
    being_worked_on = set(w.item for w in pool)
    work = sorted(all_avail - visited - being_worked_on)
    if work:
        return work[0]

while len(visited) < len(vertices):
    # remove from pool
    for w in list(pool):
        if t - w.time_started == cost(w.item):
            visited.add(w.item)
            pool.remove(w)
    # add work to pool
    while next_avail() and len(pool) < pool_size:
        pool.add(Worker(next_avail(), t))
    t += 1

print t - 1
