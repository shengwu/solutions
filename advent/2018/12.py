import copy

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

def to_binary(s):
    return int('0b' + s.replace('#', '1').replace('.', '0'), 2)

def bin_to_nums(curr, offset):
    num = -offset
    i = 0
    nums = []
    while (1 << i) <= curr:
        if curr & (1 << i):
            nums.append(num + i)
        i += 1
    return nums

cache = {}
def gnext(curr, bin_d):
    result = 0
    # don't forget that the original shifts by 2 each time!
    curr <<= 4
    offset = 0
    while (1 << offset) <= curr:
        ckey = (curr & (0xffffffffffffffffffffffffffffffff << offset)) >> offset
        if ckey in cache:
            result |= (cache[ckey] << offset)
        else:
            res = 0
            for i in range(124):
                k = ((0x1f << i) & ckey) >> i
                res |= (bin_d.get(k, 0) << i)
            cache[ckey] = res
            result |= res << offset
        offset += 124
    return result

bin_d = {to_binary(k[::-1]): to_binary(v) for k, v in d.iteritems()}

# part 1
curr = to_binary(state[::-1])
offset = 0
for i in range(20):
    curr = gnext(curr, bin_d)
    offset += 2
print sum(bin_to_nums(curr, offset))

# part 2
curr = to_binary(state[::-1])
offset = 0
prev_sum = 0
prev_diff = 0
stable_i = 0
for i in range(100000):
    curr = gnext(curr, bin_d)
    offset += 2
    curr_sum = sum(bin_to_nums(curr, offset))
    curr_diff = curr_sum - prev_sum
    if curr_diff == prev_diff:
        stable_i = i
        break
    prev_diff = curr_diff
    prev_sum = curr_sum

n = 50000000000
print prev_sum + prev_diff * (n - stable_i)

# you just had to spot the pattern
# this is the worst.
# answer was 2300000000006 for part 2
# my input stabilized after 101-102 generations, then it was 46 times each addl generation after that
