ints = set()
for base in range(1, 10):
    for power in range(1, 30):
        power_len = len(str(base**power))
        if power_len == power:
            ints.add(base**power)
print len(ints)
