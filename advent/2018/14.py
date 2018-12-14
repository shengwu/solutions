def tick(recipes, elves):
    digits = str(sum(recipes[e] for e in elves))
    recipes += map(int, digits)
    for i in xrange(len(elves)):
        elves[i] = (elves[i] + recipes[elves[i]] + 1) % len(recipes)

def matches(recipes, searched, target_arr):
    for i in xrange(searched, len(recipes)):
        if recipes[i:i+6] == target_arr:
            print i
            return True

target = 190221
target_arr = map(int, str(190221))
recipes = [3, 7]
elves = [0, 1]

while len(recipes) < target + 10:
    tick(recipes, elves)

print ''.join(str(d) for d in recipes[target:target+10])

searched = 0
while not matches(recipes, searched, target_arr):
    searched = len(recipes) - 6
    tick(recipes, elves)
