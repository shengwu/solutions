from collections import Counter, defaultdict

def expand(s):
    if s == '': return ''
    count = 1
    curr = s[0]
    result = []
    for digit in s[1:]:
        if digit != curr:
            result.append(count)
            result.append(curr)
            count = 1
            curr = digit
        else:
            count += 1
    result.append(count)
    result.append(curr)
    return ''.join(str(r) for r in result)

assert expand('1') == '11'
assert expand('11') == '21'
assert expand('21') == '1211'
assert expand('1211') == '111221'
assert expand('111221') == '312211'

inp = '3113322113'
for _ in xrange(40):
    inp = expand(inp)

print len(inp)

# ran this with pypy - still took a few seconds
inp = '3113322113'
for _ in xrange(50):
    inp = expand(inp)

print len(inp)
