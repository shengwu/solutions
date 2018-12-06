from collections import Counter, defaultdict

inp = '''
124, 262
182, 343
79, 341
44, 244
212, 64
42, 240
225, 195
192, 325
192, 318
42, 235
276, 196
181, 262
199, 151
166, 214
49, 81
202, 239
130, 167
166, 87
197, 53
341, 346
235, 241
99, 278
163, 184
85, 152
349, 334
175, 308
147, 51
251, 93
163, 123
151, 219
162, 107
71, 58
249, 293
223, 119
46, 176
214, 140
80, 156
265, 153
92, 359
103, 186
242, 104
272, 202
292, 93
304, 55
115, 357
43, 182
184, 282
352, 228
267, 147
248, 271
'''

rows = inp.strip().split('\n')
points = [(int(pair.split(',')[0]), int(pair.split(',')[1])) for pair in rows]

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def closest(pt):
    min_pt = None
    min_dist = float('inf')
    dists = []
    for b in points:
        dists.append((b, manhattan(pt, b)))
    dists.sort(key=lambda d: d[1])
    if dists[0][1] == dists[1][1]:
        return None
    return dists[0][0]

def biggest_area():
    min_x = min(pt[0] for pt in points)
    min_y = min(pt[1] for pt in points)
    max_x = max(pt[0] for pt in points)
    max_y = max(pt[1] for pt in points)
    first_pass = Counter()
    for x in xrange(min_x-10, max_x+20):
        for y in xrange(min_y-10, max_y+20):
            cand = closest((x, y))
            if cand is not None:
                first_pass[cand] += 1
    second_pass = Counter()
    for x in xrange(min_x-100, max_x+200):
        for y in xrange(min_y-100, max_y+200):
            cand = closest((x, y))
            if cand is not None:
                second_pass[cand] += 1
    areas = []
    for pt in points:
        if first_pass[pt] == second_pass[pt]:
            areas.append(first_pass[pt])
    return max(areas)

print biggest_area()
# wrong: 3304 is too high
# wrong: 3153 is too low
# turned out my min dist tiebreaker was wrong
# slow even with pypy


# unoptimized part 2

# i think you can easily optimize this
# e.g. if you know the manhattan sum for x-1, y
# and you are x, y
# you count the number of points <= x-1 and add that count
# and you count the number of points > x-1 and subtract that count

def manhattan_sum(pt):
    total = 0
    for b in points:
        total += manhattan(pt, b)
    return total

sum_limit = 10000

count = 0
for x in xrange(-1000, 1500):
    for y in xrange(-1000, 1500):
        if manhattan_sum((x, y)) < sum_limit:
            count += 1
print count
