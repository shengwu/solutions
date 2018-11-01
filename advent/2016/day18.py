inp = '^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^.'

def is_trap(rows, i, j):
    left = False
    right = False
    center = rows[i-1][j] == '^'
    if j > 0:
        left = rows[i-1][j-1] == '^'
    if j < len(inp)-1:
        right = rows[i-1][j+1] == '^'
    return ((left and center and not right) or
            (center and right and not left) or
            (left and not center and not right) or
            (right and not center and not left))


def count_rows(num_rows):
    rows = [inp]
    safe_count = 0
    for i in range(1, num_rows):
        row = []
        for j in range(len(inp)):
            if is_trap(rows, i, j):
                row.append('^')
            else:
                row.append('.')
        rows.append(''.join(row))
    return sum(sum(1 if c == '.' else 0 for c in row) for row in rows)


# part 1 - answer was 1926
print(count_rows(40))

# part 2 - answer was 19986699
# (ran this with pypy)
print(count_rows(400000))
