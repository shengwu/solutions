import md5

# part 1
# answer was d4cd2ee1

inp = 'ugkcyxxp'

def get_char(n):
    s = md5.new(inp + str(n)).hexdigest()
    if s.startswith('00000'):
        return s[5]

n = 0
result = []
while len(result) < 8:
    char = get_char(n)
    if char:
        result.append(char)
    n += 1
print(''.join(result))


# part 2
# answer was f2c730e5

def get_char_and_pos(n):
    s = md5.new(inp + str(n)).hexdigest()
    if s.startswith('00000'):
        if s[5] in '01234567':
            return s[6], s[5]
    return None, None

n = 0
result = [None] * 8

while not all(result):
    char, pos = get_char_and_pos(n)
    if char:
        if result[int(pos)] is None:
            result[int(pos)] = char
    n += 1

print(''.join(result))
