import collections
import math

# Generate all right triangles with a + b + c <= 1000
triangles = set()
for a in range(1, 1000):
    for b in range(1, 1000 - a):
        c = math.sqrt(a**2 + b**2)
        if c.is_integer() and a + b + c <= 1000:
            triangles.add(tuple(sorted([a, b, int(c)])))
print collections.Counter(map(sum, triangles)).most_common(1)[0][0]
