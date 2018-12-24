import copy
import re

inp = '''
Immune System:
3020 units each with 3290 hit points with an attack that does 10 radiation damage at initiative 16
528 units each with 6169 hit points with an attack that does 113 fire damage at initiative 9
4017 units each with 2793 hit points (weak to radiation) with an attack that does 6 slashing damage at initiative 1
2915 units each with 7735 hit points with an attack that does 26 cold damage at initiative 4
3194 units each with 1773 hit points (immune to radiation; weak to fire) with an attack that does 5 cold damage at initiative 13
1098 units each with 4711 hit points with an attack that does 36 radiation damage at initiative 7
2530 units each with 3347 hit points (immune to slashing) with an attack that does 12 bludgeoning damage at initiative 5
216 units each with 7514 hit points (immune to cold, slashing; weak to bludgeoning) with an attack that does 335 slashing damage at initiative 15
8513 units each with 9917 hit points (immune to slashing; weak to cold) with an attack that does 10 fire damage at initiative 14
1616 units each with 3771 hit points with an attack that does 19 bludgeoning damage at initiative 10

Infection:
1906 units each with 37289 hit points (immune to radiation; weak to fire) with an attack that does 28 radiation damage at initiative 3
6486 units each with 32981 hit points with an attack that does 9 bludgeoning damage at initiative 18
489 units each with 28313 hit points (immune to radiation, bludgeoning) with an attack that does 110 bludgeoning damage at initiative 6
1573 units each with 44967 hit points (weak to bludgeoning, cold) with an attack that does 42 slashing damage at initiative 12
2814 units each with 11032 hit points (immune to fire, slashing; weak to radiation) with an attack that does 7 slashing damage at initiative 2
1588 units each with 18229 hit points (weak to slashing; immune to radiation, cold) with an attack that does 20 radiation damage at initiative 19
608 units each with 39576 hit points (immune to bludgeoning) with an attack that does 116 slashing damage at initiative 20
675 units each with 48183 hit points (immune to cold, slashing, bludgeoning) with an attack that does 138 slashing damage at initiative 8
685 units each with 11702 hit points with an attack that does 32 fire damage at initiative 17
1949 units each with 32177 hit points with an attack that does 32 radiation damage at initiative 11
'''

#inp = '''
#Immune System:
#17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
#989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3
#
#Infection:
#801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
#4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4
#'''

immune_raw, infection_raw = inp.split('\n\n')
immune_rows = immune_raw.strip().split('\n')[1:]
infection_rows = infection_raw.strip().split('\n')[1:]

class Unit(object):
    def __init__(self, side, units, hp, dmg, initiative, dmg_type, weak_to, immune_to):
        self.side = side
        self.units = units
        self.hp = hp
        self.dmg = dmg
        self.initiative = initiative
        self.dmg_type = dmg_type
        self.weak_to = weak_to
        self.immune_to = immune_to

    def power(self):
        return self.units * self.dmg

    def take_damage(self, amount):
        while amount >= self.hp:
            self.units -= 1
            amount -= self.hp

    def take_damage_from(self, other):
        self.take_damage(self.would_take_damage_from(other))

    def boost(self, amt):
        self.dmg += amt

    def would_take_damage_from(self, other):
        if other.dmg_type in self.immune_to:
            return 0
        if other.dmg_type in self.weak_to:
            return other.power() * 2
        return other.power()

    def __repr__(self):
        return '<{}, {}, {}, {}, {}, {}, {}, {}>'.format(self.side, self.units, self.hp, self.dmg, self.initiative, self.dmg_type, self.weak_to, self.immune_to)

def parse_row(row, side):
    unitcount, hp, dmg, initiative = map(int, re.findall(r'\d+', row))
    dmg_type = re.search(r'(\w+) damage', row).group(1)
    weak_to = []
    immune_to = []
    weak_to_s = re.search(r'weak to ([^\);]+)', row)
    if weak_to_s:
        weak_to = weak_to_s.group(1).split(', ')
    immune_to_s = re.search(r'immune to ([^\);]+)', row)
    if immune_to_s:
        immune_to = immune_to_s.group(1).split(', ')
    return Unit(side, unitcount, hp, dmg, initiative, dmg_type, weak_to, immune_to)

immune_orig = [parse_row(row, 'immune') for row in immune_rows]
infection_orig = [parse_row(row, 'infection') for row in infection_rows]

def select(immune, infection):
    order = sorted(immune + infection, key=lambda g: (g.power(), g.initiative), reverse=True)
    targets = {}
    for g in order:
        choose(immune, infection, g, targets)
    return targets

def choose(immune, infection, source, targets):
    options = set(immune) if source.side == 'infection' else set(infection)
    filtered_options = options - set(targets.values())
    if len(filtered_options) == 0:
        return
    chosen = max(filtered_options,
                 key=lambda t: (t.would_take_damage_from(source), t.power(), t.initiative))
    if chosen.would_take_damage_from(source) == 0:
        return
    targets[source] = chosen

def attack(immune, infection, targets):
    order = sorted(immune + infection, key=lambda g: g.initiative, reverse=True)
    for g in order:
        if g in targets:
            target = targets[g]
            target.take_damage_from(g)
            if target.units <= 0:
                if target in immune:
                    immune.remove(target)
                else:
                    infection.remove(target)


# part 1
immune = copy.deepcopy(immune_orig)
infection = copy.deepcopy(infection_orig)
while len(immune) > 0 and len(infection) > 0:
    targets = select(immune, infection)
    attack(immune, infection, targets)
if len(immune) == 0:
    print sum(g.units for g in infection)
else:
    print sum(g.units for g in immune)


# part 2
boost = 0
found_answer = False
while len(immune) == 0 or not found_answer:
    boost += 1
    immune = copy.deepcopy(immune_orig)
    infection = copy.deepcopy(infection_orig)
    [g.boost(boost) for g in immune]

    found_answer = True
    prev_scores = None
    while len(immune) > 0 and len(infection) > 0:
        targets = select(immune, infection)
        attack(immune, infection, targets)
        # prevent infinite loops
        scores = (sum(g.units for g in immune), sum(g.units for g in infection))
        if scores == prev_scores:
            found_answer = False
            break
        prev_scores = scores

print sum(g.units for g in immune)
