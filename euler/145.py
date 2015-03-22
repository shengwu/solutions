odds = set([1, 3, 5, 7, 9])

def is_reversible(n):
    # Leading zeroes not allowed
    if n / 10 * 10 == n:
        return False

    total = n + int(str(n)[::-1])
    while total > 0:
        if not total % 10 in odds:
            return False
        total /= 10
    return True

count = 0
for n in range(10**9):
    if is_reversible(n):
        count += 1
print count
