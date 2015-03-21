# A naive solution for problem 26
from decimal import Decimal, getcontext

# Use 1000 decimal digits
getcontext().prec = 10000

def get_recurring_cycle_len_for_denominator(d):
    digits = str(Decimal(1) / Decimal(d))[2:]
    # Ignore all cycles below length 6 (returns incorrect results but it's okay)
    for i in xrange(6, len(digits)/2):
        for j in xrange(0, len(digits)-i*2):
            if digits[j:j+i] == digits[j+i:j+i*2]:
                return i
    return 0

max_cycle = 0
max_n = 0
for n in xrange(2, 1000):
    cycle_len = get_recurring_cycle_len_for_denominator(n)
    if cycle_len > max_cycle:
        max_cycle = cycle_len
        max_n = n
print max_n
