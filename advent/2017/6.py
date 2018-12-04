from collections import Counter, defaultdict

inp = ''' 14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4 '''

curr = [int(elem) for elem in inp.strip().split()]
seen = set([tuple(curr)])
l = len(curr)
tries = 0
first_repeat = None

while True:
    max_c = -1
    max_i = -1
    for i, c in enumerate(curr):
        if c > max_c:
            max_c = c
            max_i = i

    curr[max_i] = 0
    i = max_i
    while max_c > 0:
        i = (i + 1) % l
        curr[i] += 1
        max_c -= 1

    tries += 1
    if tuple(curr) in seen:
        print tries
        first_repeat = tuple(curr)
        break
    seen.add(tuple(curr))

tries = 0

while True:
    max_c = -1
    max_i = -1
    for i, c in enumerate(curr):
        if c > max_c:
            max_c = c
            max_i = i

    curr[max_i] = 0
    i = max_i
    while max_c > 0:
        i = (i + 1) % l
        curr[i] += 1
        max_c -= 1

    tries += 1
    if tuple(curr) == first_repeat:
        print tries
        break
