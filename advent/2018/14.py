from collections import deque

target = 190221
recipes = [3, 7]
elves = [0, 1]

def tick():
    global recipes, elves
    digits = str(sum(recipes[e] for e in elves))
    recipes += map(int, digits)
    for i in xrange(len(elves)):
        elves[i] = (elves[i] + recipes[elves[i]] + 1) % len(recipes)

searched = 0
def search():
    global recipes, searched
    for i in xrange(searched, len(recipes)):
        if recipes[i:i+6] == [1, 9, 0, 2, 2, 1]:
            print i
            return True
    searched = len(recipes) - 6

while len(recipes) < target + 10:
    tick()

print ''.join(str(d) for d in  recipes[target:target+10])

while not search():
    tick()
