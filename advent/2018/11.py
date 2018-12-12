from collections import Counter, defaultdict

serial = 5093
#serial = 18
grid = []
for _ in xrange(300):
    grid.append([0] * 300)
#serial = 8

def power(cell, serial):
    rack_id = cell[0] + 10
    level = rack_id * cell[1]
    level += serial
    level *= rack_id
    level /= 100
    level %= 10
    return level - 5

for i, row in enumerate(grid):
    for j in xrange(len(row)):
        grid[i][j] = power([i, j], serial)

maxp = 0
coords = None
for i in xrange(len(grid)-2):
    for j in xrange(len(row)-2):
        curr = 0
        for k in xrange(3):
            for l in xrange(3):
                curr += grid[i+k][j+l]
        if curr > maxp:
            maxp = curr
            coords = [i, j]
print coords


# naive part 2

'''
maxp = 0
maxside = 0
coords = None
for i in xrange(len(grid)):
    for j in xrange(len(row)):
        for sidelen in xrange(1, 300-max(i, j)):
            curr = 0
            for k in xrange(sidelen):
                for l in xrange(sidelen):
                    curr += grid[i+k][j+l]
            if curr > maxp:
                maxp = curr
                maxside = sidelen
                coords = [i, j]
print coords, maxside
# 285,169,12 incorrect
# [285, 169] 12
'''



# cached part 2

cache = {}
maxp = 0
maxside = 0
coords = None
for j in xrange(len(row)-1, -1, -1):
    for i in xrange(len(grid)-1, -1, -1):
        for sidelen in xrange(1, 300-max(i, j)+1):
            curr = 0
            if (i+1, j+1, sidelen-1) in cache:
                curr = cache[(i+1, j+1, sidelen-1)]
                curr += grid[i][j]
                for k in xrange(1, sidelen):
                    curr += grid[i+k][j]
                    curr += grid[i][j+k]
                cache[(i, j, sidelen)] = curr
            else:
                for k in xrange(sidelen):
                    for l in xrange(sidelen):
                        curr += grid[i+k][j+l]
                cache[(i, j, sidelen)] = curr
            if curr > maxp:
                maxp = curr
                maxside = sidelen
                coords = [i, j]
print coords, maxside, maxp
# 285,169,14 incorrect


# dynamic programming

'''

c = []
for _ in xrange(300):
    c.append([0] * 300)

for i in xrange(len(grid)):
    c[len(grid)-1][i] = (1, grid[len(grid)-1][i])
    c[i][len(row)-1] = (1, grid[i][len(row)-1])

for i in xrange(len(grid)-2, -1, -1):
    for j in xrange(len(row)-2, -1, -1):
        # look at square one down and to the right
        side, val = c[i+1][j+1]
        # option one: just take ourselves
        selfval = grid[i][j]
        # option two: include the down and to the right opt square
        inclval = grid[i][j]
        for k in xrange(1, side+1):
            inclval += grid[i][j+k]
            inclval += grid[i+k][j]
        if selfval > inclval:
            c[i][j] = (1, selfval)
        else:
            print i, j, side+1, inclval
            c[i][j] = (side+1, inclval)

#print c
print ', '.join([str(s[0]) for row in c for s in row])
print
print
print
print
print ', '.join([str(s[1]) for row in c for s in row])
#print ', '.join([str(s[1]) for s in row for row in c])

maxp = 0
maxside = 0
coords = None
for i, row in enumerate(c):
    for j, elem in enumerate(row):
        side, val = elem
        if val > maxp:
            maxside = side
            maxp = val
            coords = [i, j]
print coords, maxside, maxp
# 290,179,6 incorrect

'''
