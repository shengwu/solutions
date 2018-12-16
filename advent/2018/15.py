import copy
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

def around(player):
    return set(
        (player.x+dx, player.y+dy)
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))
    )

def attackable(player, elves, goblins):
    neighboring_spots = around(player)
    if player.type == 'goblin':
        enemies = elves
    else:
        enemies = goblins
    result = []
    for enemy in enemies:
        if loc(enemy) in neighboring_spots:
            result.append(enemy)
    return result

def attack(attackable, power=3):
    assert len(attackable) > 0
    # find enemies with the lowest hp
    lowest = []
    min_hp = min(a.hp for a in attackable)
    for enemy in attackable:
        if enemy.hp == min_hp:
            lowest.append(enemy)
    # sort by location
    lowest.sort(key=loc)
    # attack!
    lowest[0].hp -= power

def bfs_dist(grid, players_locs, start, end):
    q = deque([(0,) + start])
    visited = set()
    while q:
        dist, x, y = q.popleft()
        if (x, y) == end:
            #print 'bfs', players_locs, start, end, dist
            return dist
        for i, j in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
            if grid[i][j] != '#' and (i, j) not in visited and (i, j) not in players_locs:
                visited.add((i, j))
                q.append((dist+1, i, j))
    #print 'bfs', players_locs, start, end, dist, 'inf'
    return float('inf')

def move(player, goblins, elves, grid):
    # run bfs to find closest enemy
    # goal: collect squares adjacent to enemies
    q = deque([(0,) + loc(player)])
    visited = set()
    possibilities = set()
    if player.type == 'goblin':
        enemy_locs = set(map(loc, elves))
        friendly_locs = set(map(loc, goblins))
    else:
        enemy_locs = set(map(loc, goblins))
        friendly_locs = set(map(loc, elves))
    players_locs = enemy_locs | friendly_locs
    min_dist = float('inf')
    while q:
        dist, x, y = q.popleft()
        if dist > min_dist:
            break
        for i, j in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
            if (i, j) in enemy_locs and grid[i][j] != '#' and (i, j) not in visited and (i, j) not in friendly_locs:
                #print (i, j), 'in enemy locs', (dist, x, y)
                possibilities.add((dist, x, y))
                min_dist = min(min_dist, dist)
                continue
            if grid[i][j] != '#' and (i, j) not in visited and (i, j) not in players_locs:
                visited.add((i, j))
                q.append((dist+1, i, j))
    if len(possibilities) == 0:
        return 'no_targets'
    #print 'whittlig', min_dist, possibilities
    final = filter(lambda p: p[0] == min_dist, possibilities)
    chosen = sorted((p[1], p[2]) for p in possibilities)[0]

    possible_next_steps = [l for l in around(player) if grid[l[0]][l[1]] != '#' and l not in players_locs]
    next_step_dists = [bfs_dist(grid, players_locs, (s[0], s[1]), chosen) for s in possible_next_steps]
    min_next_step_dist = min(next_step_dists)
    tossup_next_steps = [p[1] for p in filter(lambda p: next_step_dists[p[0]] == min_next_step_dist, enumerate(possible_next_steps))]
    chosen_next_step = sorted(tossup_next_steps)[0]
    #print player, enemy_locs, min_next_step_dist, possible_next_steps, chosen_next_step
    player.x = chosen_next_step[0]
    player.y = chosen_next_step[1]

def turn(player, goblins, elves, grid, elf_power):
    if player.hp <= 0:
        return
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
    if not try_attack():
        move(player, goblins, elves, grid)
        try_attack()

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
    for player in order:
        if turn(player, goblins, elves, grid, elf_power=elf_power) == 'no_targets':
            return 'no_targets'
        remove_dead(goblins)
        remove_dead(elves)

def outcome(turns, goblins, elves):
    assert len(goblins) == 0 or len(elves) == 0
    if len(goblins) == 0:
        print turns, sum(e.hp for e in elves)
        return turns * sum(e.hp for e in elves)
    print turns, sum(g.hp for g in goblins)
    return turns * sum(g.hp for g in goblins)

def get_battle_outcome(inp, elf_power=3):
    elves = []
    goblins = []
    grid = inp.strip().split('\n')
    for i, row in enumerate(grid):
        for j, elem in enumerate(row):
            if elem == 'G':
                goblins.append(Player(200, 'goblin', i, j))
            elif elem == 'E':
                elves.append(Player(200, 'elf', i, j))
    turns = 0
    #while len(goblins) > 0 and len(elves) > 0:
    while True:
        tick(goblins, elves, grid, elf_power=elf_power)
        if len(goblins) == 0 or len(elves) == 0:
            break
        turns += 1
    return outcome(turns, goblins, elves)

def get_elf_power_with_no_deaths(inp):
    orig_elves = []
    orig_goblins = []
    grid = inp.strip().split('\n')
    for i, row in enumerate(grid):
        for j, elem in enumerate(row):
            if elem == 'G':
                orig_goblins.append(Player(200, 'goblin', i, j))
            elif elem == 'E':
                orig_elves.append(Player(200, 'elf', i, j))

    elf_power = 3
    def run():
        elves = copy.deepcopy(orig_elves)
        goblins = copy.deepcopy(orig_goblins)
        turns = 0
        #while len(goblins) > 0 and len(elves) > 0:
        while True:
            tick(goblins, elves, grid, elf_power=elf_power)
            if len(goblins) == 0 or len(elves) == 0:
                break
            turns += 1
        if len(elves) != len(orig_elves):
            return None
        return outcome(turns, goblins, elves)

    result = run()
    while result is None:
        elf_power += 1
        result = run()
    print elf_power
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
