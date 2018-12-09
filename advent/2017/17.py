from collections import deque

rotation = 386
d = deque([0])
for i in xrange(1, 2018):
    d.rotate(-rotation-1)
    d.appendleft(i)

print d[1]

# took several minutes with pypy
d = deque([0])
for i in xrange(1, 50000001):
    d.rotate(-rotation-1)
    d.appendleft(i)

while d[0] != 0:
    d.rotate(1)
print d[1]
