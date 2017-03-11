# https://www.hackerrank.com/challenges/grid-challenge

def done(grid):
    for i in xrange(1, len(grid)):
        for j, let in enumerate(grid[i]):
            if let < grid[i-1][j]:
                return False
    return True

i = input()
for _ in xrange(i):
    n = input()
    grid = []
    for __ in xrange(n):
        grid.append(sorted(raw_input().strip()))
    if done(grid):
        print 'YES'
    else:
        print 'NO'
