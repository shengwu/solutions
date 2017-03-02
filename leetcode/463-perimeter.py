

def get_first(grid):
    for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    return (i, j)

def get_falses(grid):
    ngrid = []
    for row in grid:
        ngrid.append([False for _ in xrange(len(row))])
    return ngrid

def count_exposed_sides(grid, loc):
    count = 0
    if loc[0] == 0 or (loc[0] > 0 and grid[loc[0]-1][loc[1]]) == 0:
        count += 1
    if loc[1] == 0 or (loc[1] > 0 and grid[loc[0]][loc[1]-1]) == 0:
        count += 1
    if loc[0] == len(grid) - 1 or (loc[0] < len(grid) - 1 and grid[loc[0]+1][loc[1]]) == 0:
        count += 1
    if loc[1] == len(grid[0]) - 1 or (loc[1] < len(grid[0]) - 1 and grid[loc[0]][loc[1]+1]) == 0:
        count += 1
    return count

def get_adj(grid, loc):
    adj = []
    if loc[0] > 0 and grid[loc[0]-1][loc[1]] == 1:
        adj.append((loc[0]-1, loc[1]))
    if loc[1] > 0 and grid[loc[0]][loc[1]-1] == 1:
        adj.append((loc[0], loc[1]-1))
    if loc[0] < len(grid) - 1 and grid[loc[0]+1][loc[1]] == 1:
        adj.append((loc[0]+1, loc[1]))
    if loc[1] < len(grid[0]) - 1 and grid[loc[0]][loc[1]+1] == 1:
        adj.append((loc[0], loc[1]+1))
    return adj

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = get_falses(grid)
        first = get_first(grid)
        visited[first[0]][first[1]] = True
        q = [first]
        count = 0
        while len(q) > 0:
            curr = q.pop()
            adj = get_adj(grid, curr)
            count += count_exposed_sides(grid, curr)
            for neighbor in adj:
                if not visited[neighbor[0]][neighbor[1]]:
                    q.append(neighbor)
                    visited[neighbor[0]][neighbor[1]] = True
        return count


s = Solution()
print s.islandPerimeter([[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]])
print s.islandPerimeter([[0, 1]])
