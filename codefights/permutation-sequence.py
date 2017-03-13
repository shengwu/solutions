# https://codefights.com/interview/Ruzueihek5i5cHJRD/description

import itertools

def permutationSequence(n, k):
    p = itertools.permutations(range(1, n+1))
    while k > 0:
        try:
            n = p.next()
        except StopIteration:
            return ''
        k -= 1
    return ''.join(map(str, n))
