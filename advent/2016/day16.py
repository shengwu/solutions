


def swap(s):
    return ''.join('1' if c == '0' else '0' for c in s)

def process(a):
    return a + '0' + swap(a)[::-1]

def checksum(s):
    result = []
    for i in range(0, len(s), 2):
        if s[i] == s[i+1]:
            result.append('1')
        else:
            result.append('0')
    if len(result) % 2 == 0:
        return checksum(''.join(result))
    return ''.join(result)

# part 1
# answer was 11100110111101110

target_len = 272
curr_state = '10111100110001111'
while len(curr_state) < target_len:
    curr_state = process(curr_state)
print checksum(curr_state[:target_len])

# part 2
# answer was 10001101010000101
# it's probably not necessary to brute force this, but it didn't really take
# that long

target_len = 35651584
curr_state = '10111100110001111'
while len(curr_state) < target_len:
    curr_state = process(curr_state)
print checksum(curr_state[:target_len])

