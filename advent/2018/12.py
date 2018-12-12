import copy
from collections import Counter, defaultdict

state = '..#..####.##.####...#....#######..#.#..#..#.#.#####.######..#.#.#.#..##.###.#....####.#.#....#.#####'

d = {
    '#.##.': '.',
    '#.#..': '.',
    '###.#': '.',
    '..#.#': '.',
    '....#': '.',
    '.####': '.',
    '##.##': '#',
    '###..': '#',
    '.###.': '#',
    '...#.': '.',
    '.....': '.',
    '##..#': '.',
    '.#.#.': '#',
    '.#.##': '#',
    '##.#.': '.',
    '##...': '.',
    '#####': '#',
    '#...#': '.',
    '..##.': '.',
    '..###': '.',
    '.#...': '#',
    '.##.#': '.',
    '#....': '.',
    '.#..#': '.',
    '.##..': '#',
    '...##': '#',
    '#.###': '.',
    '#..#.': '.',
    '..#..': '#',
    '#.#.#': '#',
    '####.': '#',
    '#..##': '.',
}

'''
state = '#..#.#..##......###...###'
d = {
'...##': '#',
'..#..': '#',
'.#...': '#',
'.#.#.': '#',
'.#.##': '#',
'.##..': '#',
'.####': '#',
'#.#.#': '#',
'#.###': '#',
'##.#.': '#',
'##.##': '#',
'###..': '#',
'###.#': '#',
'####.': '#',
}
'''



def getNext(curr, d):
    res = set()
    def addIf(i):
        if i in curr:
            return '#'
        else:
            return '.'
    start = min(curr) - 4
    end = max(curr) + 4
    for i in xrange(start, end+1):
        pat = addIf(i-2) + addIf(i-1) + addIf(i) + addIf(i+1) + addIf(i+2)
        if pat in d and d[pat] == '#':
            res.add(i)
    return res

'''
#current = state
current = set(p[0] for p in enumerate(state) if p[1] == '#')
for _ in range(50000000000):
    #print current
    current = getNext(current, d)
#print current
print sum(current)
'''

# 8989 is wrong
# 13029 is wrong

# we have to use hashlife to make it through this...
# one idea: cache the middle 28 bits
# k -> v
# convert the initial string
# on a 64 bit system, maybe we can cache the middle 60 bits


def bin_to_nums(curr, offset):
    num = -offset
    i = 0
    #s = 0
    nums = []
    while (1 << i) <= curr:
        if curr & (1 << i):
            nums.append(num)
        i += 1
        num += 1
    return nums

def to_binary(s):
    return int('0b' + s.replace('#', '1').replace('.', '0'), 2)

cache = {}
def gnext(curr, bin_d):
    result = 0

    # don't forget that the original shifts by 2 each time!
    curr <<= 4

    offset = 0
    while (1 << offset) <= curr:
        ckey = (curr & (0xffffffffffffffffffffffffffffffff << offset)) >> offset
        #print ckey
        if ckey in cache:
            result |= (cache[ckey] << offset)
        else:
            #print 'finding key for', ckey, bin_to_nums(ckey, 0)
            res = 0
            for i in range(124):
                k = ((0x1f << i) & ckey) >> i
                res |= (bin_d.get(k, 0) << i)
            #print res, bin_to_nums(res, 0)
            cache[ckey] = res
            result |= res << offset
        offset += 124

    #print 'result', result, bin_to_nums(result, 0)
    return result

curr = to_binary(state[::-1])
#print bin_to_nums(curr, 0)
bin_d = {to_binary(k[::-1]): to_binary(v) for k, v in d.iteritems()}
offset = 0
#for _ in range(20):
prev = 0
for i in range(102):
    #print curr
    curr = gnext(curr, bin_d)
    offset += 2
    print i, sum(bin_to_nums(curr, offset)) - prev
    prev = sum(bin_to_nums(curr, offset)) 
    #print sum(bin_to_nums(curr, offset)) 
#print curr
print sum(bin_to_nums(curr, offset))
#print sum(bin_to_nums(curr, 0))
#print bin_d

# you just had to spot the pattern
# this is the worst.
# answer was 2300000000006 for part 2
# my input stabilized after 101-102 generations, then it was 46 times each addl generation after that
