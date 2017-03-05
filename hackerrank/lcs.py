n, m = map(int, raw_input().split())
a = map(int, raw_input().split())
b = map(int, raw_input().split())

c = []
for _ in xrange(len(a)+1):
    c.append([0] * (len(b)+1))

for i in xrange(1, len(a)+1):
    for j in xrange(1, len(b) + 1):
        if a[i-1] == b[j-1]:
            c[i][j] = c[i-1][j-1] + 1
        else:
            c[i][j] = max(c[i][j-1], c[i-1][j])

i = len(a)
j = len(b)
result = []
#print '\n'.join('\t'.join(map(str, row)) for row in c)
while c[i][j] > 0:
    if c[i-1][j-1] == c[i][j]:
        i -= 1
        j -= 1
    elif c[i-1][j] == c[i][j]:
        i -= 1
    elif c[i][j-1] == c[i][j]:
        j -= 1
    else:
        result.append(b[j-1])
        i -= 1
        j -= 1
    #print i, j
print ' '.join(map(str, result[::-1]))
