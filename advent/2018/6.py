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

points = []

for row in rows:
    points.append([int(r) for r in row.split(', ')])

def dist((a, b), (x, y)):
    return abs(a-x) + abs(b-y)

def total_dist((i, j)):
    total = 0
    for x, y in points:
        total += dist((i, j), (x, y))
    return total

# this is still wrong
def min_pt((i, j)):
    lowest = float('inf')
    pt = None
    for x, y in points:
        if x in [minx, maxx] or y in [miny, maxy]:
            continue
        d = dist((i, j), (x, y))
        if d < lowest:
            lowest = d
            pt = (x, y)
        elif d == lowest and pt != (x, y):
            pt = None
    return pt

minx = min(p[0] for p in points)
maxx = max(p[0] for p in points)
miny = min(p[1] for p in points)
maxy = max(p[1] for p in points)

scores = Counter()
count = 0
grid = ((i, j) for i in xrange(minx, maxx+1) for j in xrange(miny, maxy+1))

for i, j in grid:
    # part 1
    pt = min_pt((i, j))
    if pt is not None:
        scores[pt] += 1
    # part 2
    if total_dist((i, j)) < 10000:
        count += 1

print scores.most_common(1)[0][1]
print scores
print count
