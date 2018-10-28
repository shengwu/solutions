import md5
from collections import deque

def is_open(c):
    return c in 'bcdef'

# strategy: run a BFS
def search(init_hash, start, goal):
    q = deque([(start, '')])
    while q:
        curr, path = q.popleft()
        if curr == goal:
            return path
        directions = md5.new(init_hash + path).hexdigest()[:4]
        if curr[1] > 1 and is_open(directions[0]):
            q.append(((curr[0], curr[1] - 1), path + 'U'))
        if curr[1] < 4 and is_open(directions[1]):
            q.append(((curr[0], curr[1] + 1), path + 'D'))
        if curr[0] > 1 and is_open(directions[2]):
            q.append(((curr[0] - 1, curr[1]), path + 'L'))
        if curr[0] < 4 and is_open(directions[3]):
            q.append(((curr[0] + 1, curr[1]), path + 'R'))

# part 1
# answer was DDRRULRDRD

init_hash = 'veumntbg'
print search(init_hash, (1, 1), (4, 4))

# part 2
# answer was 536

def max_path_length(init_hash, start, goal):
    q = deque([(start, '')])
    max_len = 0
    while q:
        curr, path = q.popleft()
        if curr == goal:
            max_len = len(path)
            continue
        directions = md5.new(init_hash + path).hexdigest()[:4]
        if curr[1] > 1 and is_open(directions[0]):
            q.append(((curr[0], curr[1] - 1), path + 'U'))
        if curr[1] < 4 and is_open(directions[1]):
            q.append(((curr[0], curr[1] + 1), path + 'D'))
        if curr[0] > 1 and is_open(directions[2]):
            q.append(((curr[0] - 1, curr[1]), path + 'L'))
        if curr[0] < 4 and is_open(directions[3]):
            q.append(((curr[0] + 1, curr[1]), path + 'R'))
    return max_len

assert max_path_length('ihgpwlah', (1, 1), (4, 4)) == 370
assert max_path_length('kglvqrro', (1, 1), (4, 4)) == 492
assert max_path_length('ulqzkmiv', (1, 1), (4, 4)) == 830
print max_path_length(init_hash, (1, 1), (4, 4))
