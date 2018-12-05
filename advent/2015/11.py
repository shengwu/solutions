import string

def chunks_of_three(s):
    return set(s[i:i+3] for i in range(len(s)-2))

runs = chunks_of_three(string.ascii_lowercase)
invalid = set('iol')

pairs = set(''.join(pair) for pair in zip(string.ascii_lowercase, string.ascii_lowercase))
def has_two_pairs(s):
    for pair in pairs:
        if pair in s:
            for p2 in (pairs - set([pair])):
                if p2 in s:
                    return True
            return False
    return False

def is_valid(password):
    return (len(chunks_of_three(password) & runs) > 0 and
            len(set(password) & invalid) == 0 and
            has_two_pairs(password))

def to_letters(nums):
    return ''.join(chr(c + ord('a')) for c in nums)

def inc(password):
    nums = [ord(c) - ord('a') for c in password]
    i = len(nums)-1
    while i >= 0:
        added = nums[i] + 1
        if added < 26:
            nums[i] = added
            return to_letters(nums)
        nums[i] = 0
        i -= 1

assert inc('xx') == 'xy'
assert inc('xy') == 'xz'
assert inc('xz') == 'ya'
assert inc('ya') == 'yb'

def next_valid_password(password):
    curr = inc(password)
    while not is_valid(curr):
        curr = inc(curr)
    return curr

assert next_valid_password('abcdefgh') == 'abcdffaa'
assert next_valid_password('ghijklmn') == 'ghjaabcc'

# part 1
first = next_valid_password('vzbxkghb')
print first

# part 2
print next_valid_password(first)
