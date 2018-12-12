def power(cell, serial):
    rack_id = cell[0] + 10
    level = rack_id * cell[1]
    level += serial
    level *= rack_id
    level /= 100
    level %= 10
    return level - 5

def empty_grid(side_len):
    return [[0] * side_len for _ in xrange(side_len)]

def build_grid(side_len, serial):
    grid = empty_grid(side_len)
    for i, row in enumerate(grid):
        for j in xrange(len(grid[0])):
            grid[i][j] = power([i, j], serial)
    return grid

def build_sum_grid(grid):
    '''Builds a grid of sums based on `grid`, starting from the bottom right corner'''
    sum_grid = empty_grid(len(grid)+1)
    for i in xrange(len(grid)-1, -1, -1):
        for j in xrange(len(grid)-1, -1, -1):
            sum_grid[i][j] = grid[i][j] + sum_grid[i+1][j] + sum_grid[i][j+1] - sum_grid[i+1][j+1]
    return sum_grid

def square_total_at(sum_grid, i, j, sq_side_len):
    assert sq_side_len <= (len(sum_grid) - max(i, j))
    # since sum_grid[i-sq_side_len][j] and sum_grid[i][j-sq_side_len] overlap,
    # we add back the overlapping section
    return (sum_grid[i][j] -
            sum_grid[i+sq_side_len][j] -
            sum_grid[i][j+sq_side_len] +
            sum_grid[i+sq_side_len][j+sq_side_len])

def argmax(seq, key=lambda x: x):
    m = float('-inf')
    marg = None
    for elem in seq:
        v = key(elem)
        if v > m:
            m = v
            marg = elem
    return marg

def max_level_3x3(side_len, serial):
    grid = build_grid(side_len, serial)
    sum_grid = build_sum_grid(grid)
    valid_coordinates = ((i, j)
                         for i in xrange(side_len-2)
                         for j in xrange(side_len-2))
    return argmax(valid_coordinates,
                  key=lambda sq: square_total_at(sum_grid, sq[0], sq[1], 3))

def max_level_n(side_len, serial):
    grid = build_grid(side_len, serial)
    sum_grid = build_sum_grid(grid)
    valid_tuples = ((i, j, k)
                         for i in xrange(side_len)
                         for j in xrange(side_len)
                         for k in xrange(side_len-max(i,j), -1, -1))
    return argmax(valid_tuples,
                  key=lambda sq: square_total_at(sum_grid, sq[0], sq[1], sq[2]))

grid_size = 300
assert max_level_3x3(grid_size, 42) == (21, 61)
assert max_level_3x3(grid_size, 18) == (33, 45)
assert max_level_n(grid_size, 42) == (232, 251, 12)
assert max_level_n(grid_size, 18) == (90, 269, 16)

serial = 5093
print max_level_3x3(grid_size, serial)
print max_level_n(grid_size, serial)
