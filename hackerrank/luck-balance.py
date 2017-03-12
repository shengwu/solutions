# https://www.hackerrank.com/challenges/luck-balance

n, k = map(int, raw_input().split())
important_contests = []
luck = 0
for _ in xrange(n):
    l, i = map(int, raw_input().split())
    if i == 0:
        luck += l
    else:
        important_contests.append((l, i))
important_contests.sort(key=lambda c: c[0], reverse=True)
luck += sum(c[0] for c in important_contests[:k]) - sum(c[0] for c in important_contests[k:])
print luck
