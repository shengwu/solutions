# part 1
# answer was 120765

inp = ''
with open('9.txt') as f:
    inp = f.read().strip()

i = 0
compl = 0
while i < len(inp):
    c = inp[i]
    if c == '(':
        j = i+1
        while inp[j] != 'x': j += 1
        first = int(inp[i+1:j])
        i = j+1
        j = j+1
        while inp[j] != ')': j += 1
        second = int(inp[i:j])
        # now i is pointing to the char after the closed parens
        i = j+1
        compl += first * second
        i += first
    else:
        compl += 1
        i += 1

print(compl)


# part 2
# answer was 11658395076

def decom_len(s):
    i = 0
    compl = 0
    while i < len(s):
        c = s[i]
        if c == '(':
            j = i+1
            while s[j] != 'x': j += 1
            first = int(s[i+1:j])
            i = j+1
            j = j+1
            while s[j] != ')': j += 1
            second = int(s[i:j])
            # now i is pointing to the char after the closed parens
            i = j+1
            sublen = decom_len(s[i:i+first])
            compl += sublen * second
            i += first
        else:
            compl += 1
            i += 1
    return compl

print(decom_len(inp))
