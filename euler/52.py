def has_same_digits(n):
    digits = sorted(str(n))
    if digits != sorted(str(n*2)):
        return False
    if digits != sorted(str(n*3)):
        return False
    if digits != sorted(str(n*4)):
        return False
    if digits != sorted(str(n*5)):
        return False
    if digits != sorted(str(n*6)):
        return False
    return True

n = 100000
while True:
    if has_same_digits(n):
        print n
        break
    n += 1
