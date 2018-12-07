# https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard

# for some reason this reminds me of cantor diagonalization
# if you take all of the letters in one word, you only have to find one that's different
# it's O(N**2 L) I think which is not bad
# a lot better than N**L

from sys import stdin

def find_candidate(words, l):
    '''Returns None if no alternative could be found'''
    # index -> possibilities
    letters = {}
    for i in xrange(l):
        letters[i] = set(word[i] for word in words)
    for word in words:
        for i in xrange(l):
            for sub in letters[i]:
                cand = word[:i] + sub + word[i+1:]
                if cand not in words:
                    return cand

cases = int(next(stdin))
for c in xrange(cases):
    n, l = (int(d) for d in next(stdin).split())
    words = set()
    for _ in xrange(n):
        words.add(next(stdin).strip())
    result = find_candidate(words, l)
    if result is None:
        result = '-'
    print 'Case #{}: {}'.format(c+1, result)

