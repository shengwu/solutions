from collections import deque

class Player(object):
    def __init__(self, hp, type, x, y):
        self.hp = hp
        self.type = type
        self.x = x
        self.y = y

    def __repr__(self):
        return '{} hp: {} at ({}, {})'.format(self.type, self.hp, self.x, self.y)

def loc(player):
    return (player.x, player.y)

def around_coords(x, y):
    return set(
        (x+dx, y+dy)
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))
    )

def around(player):
    return around_coords(*loc(player))

def attackable(player, elves, goblins):
    neighboring_spots = around(player)
    enemies = elves if player.type == 'goblin' else goblins
    return filter(lambda enemy: loc(enemy) in neighboring_spots, enemies)

def attack(attackable, power=3):
    assert len(attackable) > 0
    # find enemies with the lowest hp
    min_hp = min(a.hp for a in attackable)
    lowest = filter(lambda enemy: enemy.hp == min_hp, attackable)
    # sort by location
    lowest.sort(key=loc)
    # attack!
    lowest[0].hp -= power

def bfs_dist(grid, players_locs, start, end):
    q = deque([(0,) + start])
    visited = set()
    def obstructed(x, y):
        return grid[x][y] == '#' or (x, y) in players_locs
    while q:
        dist, x, y = q.popleft()
        if (x, y) == end:
            return dist
        for i, j in around_coords(x, y):
            if not obstructed(i, j) and (i, j) not in visited:
                visited.add((i, j))
                q.append((dist+1, i, j))
    return float('inf')

def move(player, goblins, elves, grid):
    # run bfs to find closest enemy
    # goal: collect squares adjacent to enemies

    goblin_locs = set(map(loc, goblins))
    elf_locs = set(map(loc, elves))
    enemy_locs = goblin_locs if player.type == 'elf' else elf_locs
    friendly_locs = elf_locs if player.type == 'elf' else goblin_locs
    players_locs = enemy_locs | friendly_locs

    def obstructed(x, y, avoid_locs=players_locs):
        return grid[x][y] == '#' or (x, y) in avoid_locs

    q = deque([(0,) + loc(player)])
    visited = set()
    possibilities = set()
    min_dist = float('inf')
    while q:
        dist, x, y = q.popleft()
        if dist > min_dist:
            break
        for i, j in around_coords(x, y):
            if ((i, j) in enemy_locs and
                    not obstructed(i, j, avoid_locs=friendly_locs) and
                    (i, j) not in visited):
                #print (i, j), 'in enemy locs', (dist, x, y)
                possibilities.add((dist, x, y))
                min_dist = min(min_dist, dist)
                continue
            if not obstructed(i, j) and (i, j) not in visited:
                visited.add((i, j))
                q.append((dist+1, i, j))

    if len(possibilities) == 0:
        # couldn't find anywhere to attack
        # maybe enemies are already surrounded on all sides
        # maybe there are no enemies
        return
    # choose a spot where we can attack an enemy
    final = filter(lambda p: p[0] == min_dist, possibilities)
    chosen = sorted((p[1], p[2]) for p in possibilities)[0]

    # choose a step towards that enemy on the shortest path
    possible_next_steps = filter(
        lambda loc: not obstructed(loc[0], loc[1], avoid_locs=friendly_locs),
        around(player))
    next_steps_with_dists = [(bfs_dist(grid, players_locs, (s[0], s[1]), chosen), s)
                             for s in possible_next_steps]
    # several assumptions baked into the following line
    # next_steps_with_dists is a list of tuples (dist, coordinate_tuple)
    # we want the minimum distance
    # and if there are multiple steps for the minimum distance path, we'll take the
    # one that occurs first in reading order
    # using a simple sort does this for us
    chosen_next_step = sorted(next_steps_with_dists)[0][1]
    player.x = chosen_next_step[0]
    player.y = chosen_next_step[1]

def turn(player, goblins, elves, grid, elf_power):
    '''Returns true if the player did something'''
    if player.hp <= 0:
        return False
    def try_attack():
        '''Returns True if we attacked'''
        enemies = attackable(player, elves, goblins)
        if enemies:
            if player.type == 'elf':
                attack(enemies, power=elf_power)
            else:
                attack(enemies)
            return True
        return False
    if try_attack():
        return True
    move(player, goblins, elves, grid)
    return try_attack()

def remove_dead(players):
    to_remove = filter(lambda p: p.hp <= 0, players)
    for rem in to_remove:
        players.remove(rem)

def print_game_state(grid, goblins, elves):
    order = sorted(goblins + elves, key=loc)
    d = dict(zip(map(loc, order), order))
    for i, row in enumerate(grid):
        for j, p in enumerate(row):
            if (i, j) in d:
                if d[(i, j)].type == 'goblin':
                    print 'G',
                else:
                    print 'E',
            elif p == '#':
                print '#',
            else:
                print '.',
        print
    print goblins, '\n', elves
    raw_input()

def tick(goblins, elves, grid, elf_power):
    #print_game_state(grid, goblins, elves)
    order = sorted(goblins + elves, key=loc)
    went = 0
    for player in order:
        turn(player, goblins, elves, grid, elf_power=elf_power)
        remove_dead(goblins)
        remove_dead(elves)

def outcome(turns, goblins, elves):
    assert len(goblins) == 0 or len(elves) == 0
    if len(goblins) == 0:
        #print turns, sum(e.hp for e in elves)
        return turns * sum(e.hp for e in elves)
    #print turns, sum(g.hp for g in goblins)
    return turns * sum(g.hp for g in goblins)

def parse_input(inp):
    elves = []
    goblins = []
    grid = inp.strip().split('\n')
    for i, row in enumerate(grid):
        for j, elem in enumerate(row):
            if elem == 'G':
                goblins.append(Player(200, 'goblin', i, j))
            elif elem == 'E':
                elves.append(Player(200, 'elf', i, j))
    return elves, goblins, grid

def get_battle_outcome_with_elf_count(inp, elf_power=3):
    elves, goblins, grid = parse_input(inp)
    turns = 0
    while True:
        tick(goblins, elves, grid, elf_power=elf_power)
        if len(goblins) == 0 or len(elves) == 0:
            break
        turns += 1
    return outcome(turns, goblins, elves), len(elves)

def get_battle_outcome(inp, elf_power=3):
    battle_outcome, _ =  get_battle_outcome_with_elf_count(inp, elf_power=elf_power)
    return battle_outcome

def get_elf_power_with_no_deaths(inp):
    orig_elves, orig_goblins, grid = parse_input(inp)

    def run(elf_power):
        curr_outcome, elf_count = get_battle_outcome_with_elf_count(inp, elf_power=elf_power)
        if elf_count != len(orig_elves):
            return None
        return curr_outcome

    elf_power = 3
    result = run(elf_power)
    while result is None:
        elf_power += 1
        result = run(elf_power)
    return result


inp = '''
################################
######......###...##..##########
######....#G###G..##.G##########
#####...G##.##.........#########
##....##..#.##...........#######
#....#G.......##.........G.#####
##..##GG....G.................##
##.......G............#.......##
###.....G.....G#......E.......##
##......##....................##
#.....####......G.....#...######
#.#########.G....G....#E.#######
###########...#####......#######
###########..#######..E.......##
###########.#########......#.###
########..#.#########.........##
#######G....#########........###
##.##.#.....#########...EE#..#.#
#...GG......#########.#...##..E#
##...#.......#######..#...#....#
###.##........#####......##...##
###.........................#..#
####.............##........###.#
####............##.........#####
####..##....###.#...#.....######
########....###..............###
########..G...##.###...E...E.###
#########...G.##.###.E....E.####
#########...#.#######.......####
#############..########...######
##############.########.########
################################
'''

test1 = '''
#######   
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#   
#######
'''

test2 = '''
#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######
'''

test3 = '''
#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######
'''

test4 = '''
#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######
'''

test5 = '''
#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######
'''

test6 = '''
#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########
'''

# my solution is incorrect for test1 - doesn't handle the mid-round end correctly
print get_battle_outcome(test1)

print get_battle_outcome(test2)
print get_battle_outcome(test3)
print get_battle_outcome(test4)
print get_battle_outcome(test5)
print get_battle_outcome(test6)
print get_battle_outcome(inp)
# worked for part 1



# part 2
print get_elf_power_with_no_deaths(test1)
print get_elf_power_with_no_deaths(test2)
print get_elf_power_with_no_deaths(test3)
print get_elf_power_with_no_deaths(test4)
print get_elf_power_with_no_deaths(test5)
print get_elf_power_with_no_deaths(test6)
print get_elf_power_with_no_deaths(inp)

# 60550 was wrong for part 2
# 59339 was correct for part 2
# the damage calc seems ok, but my turn counting is bad - fairly consistenly off
