# https://codefights.com/interview/Q8td3XApSWuobjEaJ/solutions
# python 3

from functools import lru_cache

@lru_cache()
def setsOfFactors(n):
    result = set()
    result.add((n, 1))
    for i in range(2, int(n**0.5)+1):
        if n % i != 0:
            continue
        larger = n / i
        smaller = i
        for factor_set in setsOfFactors(larger)[1:]:
            result.add(tuple(sorted(factor_set + (smaller,), reverse=True)))
        result.add((larger, smaller))
    return sorted(result, reverse=True)
