inp = '''
.|#.#|..#...|..##||...|#..##..#..|#|....#.#|.|....
.||....#..#...|#....#.||....||...||...|..#|..||..|
......|.|.#.#.#..|.....#.###.....#........|.||..#|
..|.....||...#||#.#|#.....|##.|.|....|#....#|..#.#
|...#.|..#|#.#....|.#.#.|.#...#..#|#.....##|#..#.|
#....|#|......#.|||..#..#..||...#.#...|||##|..|#..
.#||.|....|.......#|##...|.#.....#.##...|.|.#...#|
....#|.|.|...##.......|#.....|..#......#...#|.#..#
...#.|....#.|.#...|||......##..|#|||#..#...|.|#.#.
.#..|...|..#.|##.#.#......#...||.||.#...|.#.#.#|..
|...#.|||...#|.#||.......|.##.....|..||...####...|
.##..|..##|...##.#...#...#.#|.|###...#............
|.....||...#.......|.#..|#.....|.|#.|..||.##.|#|..
.#..##|.#|.|..|.#..#.|.#..#|......##...#.#.......#
...#.##.|..|.#.....#....#..#.............|.|##||..
||.##.||.|.|..|..#.|.|.##|.|...|.#.|#.......#.|...
..|#.##..#|.#|#.#...........|.|........#...#|...#|
....|.#|..|.#|#|...|.|.#..#.....#|##|||##.#....#..
...###.#.....#.||......#|#..##...|#....#....|#|.#.
.##.|.##|.#.||....#|....|.#.|#.|....##..#.##|.....
|...|...#|....#....#...#|#...|..#.#.|.|.....|.#|..
.|.|.#.#.#|.#.|#....|.|###..#......|...|...#.|#...
..|...||.|..##|...|..|#|...|......#.||.#...#..|#.|
........|..#||..|....|.....|.|#..#....|#..|.#.....
#.|.|#....#...|..|....|.#.....||.....|..|........#
...||||....|.#.|....#..#....|###....|...#...##....
|||........|.#|.|......||#.|.....|.||#|.##....#|..
.....|#|#..||#...|##.|..||....####.|#.|..#....|.#.
.||..#||....#.....#.#|.|....|.##|..|.#..|##....##.
.|#.#|#|#|.....||..|.|.|.#......#..|.#..#..|.#||#.
|.|#.......|..#|#|....|.#.#.#.|...|.......##.|||#|
..|.....#...||.|....|##|...#..#.#.....|##|##.##...
.|.|..##.#|..|.|#.......#....#||.|...||#...|......
|.|##.#....|#..|....#..#..|##.|.##..#......#|##|..
..#....#.|#...#.#...|.....|.||.#.#|.#.|###..|..#.#
..|.##...........|..###.||.|.##.|....|.|.#|#.#.|#|
..|....|.|#|...#|#...|.#......#.#||...|.#|...#.|#.
..#.......|.||.....||.|....|#||..........#...|#...
.|..#....|#|||#..##||..#|.......|..|###..|.#...|.|
|..|.#|.#...#....|.....#.....#....#...|..|.|.#.|.#
....###.#....|.#..#...#...###.|.|.....#|...#.....|
..#....##.....##..|.#.||#.|.#|#||..|...#|..|.#....
|#..#.#|||#.|#..#........#......||...#.|..#|....#|
......#|...#.|...#...|.|...|#|#......#|.##.#|.|.#|
#||.#......#.##......#..||.##|.|.||..|#....#..#...
#.#...#.|.#|#||#.#......#....|##|.........##.#|...
.....###...#||....|####..#|||...#..#|.|....#|..#..
......|#..#.#.#..|.#|#||..||.|...#....##...|......
...#...|..#..##.||.#.#.....|.###.....##|#||..#..#|
.#..#||.#....||....|##..|||...|.||...#..##.#....#.
'''

grid = inp.strip().split('\n')
state = list(grid)

def neighbors(pt): 
    x, y = pt 
    return ((x+1, y), (x-1, y), (x, y+1), (x, y-1),
            (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1))

def in_grid(grid, pt):
    return pt[0] >= 0 and pt[0] < len(grid) and pt[1] >= 0 and pt[1] < len(grid[0])

def neighbors_in(grid, pt):
    return filter(lambda p: in_grid(grid, p), neighbors(pt))

def count_neighbors(grid, pt, target):
    count = 0
    for x, y in neighbors_in(grid, pt):
        if grid[x][y] == target:
            count += 1
    return count

def empty(curr):
    return [[None for x in xrange(len(curr[0]))] for _ in xrange(len(curr))]

def tick(state):
    new = empty(state)
    for i, row in enumerate(state):
        for j, cell in enumerate(row):
            if cell == '.':
                if count_neighbors(state, (i, j), '|') >= 3:
                    new[i][j] = '|'
                else:
                    new[i][j] = '.'
            elif cell == '|':
                if count_neighbors(state, (i, j), '#') >= 3:
                    new[i][j] = '#'
                else:
                    new[i][j] = '|'
            elif cell == '#':
                if count_neighbors(state, (i, j), '#') >= 1 and count_neighbors(state, (i, j), '|') >= 1:
                    new[i][j] = '#'
                else:
                    new[i][j] = '.'
    return new

def count(grid, char):
    return sum(sum(c == char for c in row) for row in grid)

def print_state(state):
    print '\n'.join(''.join(row) for row in state)

# part 1
for _ in xrange(10):
    state = tick(state)

print count(state, '|') * count(state, '#')

# part 2 - find the pattern
memory = {}
diffs = {}
state = list(grid)
for i in xrange(1000000000):
    state = tick(state)
    val = count(state, '|') * count(state, '#')
    if val in memory:
        diff = i - memory[val]
        if diff in diffs:
            print 'previous diff started at', diffs[diff]
            print 'cycle size', diff
            print 'i', i
            print 'spot in cycle', i % diff
            print val
        else:
            diffs[diff] = memory[val]
    memory[val] = i

# did this by hand

# 184920 was wrong - too low!
# it was 191820, needed to adjust the other way
