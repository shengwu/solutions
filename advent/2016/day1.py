import sys

# part 1
# 236 was the correct answer for me

inp = '''
R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5, L4, L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1, R1, L1, L5, L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3, R5, L4, L4, R2, R5, L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2, R3, L1, L1, R4, R3, L4, R2, R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2, R4, R4, L3, R2, R1, L4, R3, L3, L4, L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5, L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, L4, R5, R3, R2, R2, L3, R3, L2, L5
'''
commands = inp.strip().split(', ')

coords = [0, 0]
direction = 0

for command in commands:
    turn, steps = command[0], int(command[1:])
    if turn == 'L': direction = (direction - 90) % 360
    if turn == 'R': direction = (direction + 90) % 360
    if direction == 0: coords[0] += steps
    if direction == 90: coords[1] += steps
    if direction == 180: coords[0] -= steps
    if direction == 270: coords[1] -= steps

print(sum(abs(coord) for coord in coords))


# part 2
# 182 was the correct answer

coords = [0, 0]
direction = 0
visited = set()

for command in commands:
    turn, steps = command[0], int(command[1:])
    if turn == 'L': direction = (direction - 90) % 360
    if turn == 'R': direction = (direction + 90) % 360
    oldcoords = [coords[0], coords[1]]
    if direction == 0: coords[0] += steps
    if direction == 90: coords[1] += steps
    if direction == 180: coords[0] -= steps
    if direction == 270: coords[1] -= steps
    if oldcoords[0] == coords[0]:
        if oldcoords[1] > coords[1]:
            inc = -1
        else:
            inc = 1
        for i in range(oldcoords[1], coords[1], inc):
            candidate = (coords[0], i)
            if candidate in visited:
                print(sum(abs(coord) for coord in candidate))
                sys.exit(0)
            visited.add(candidate)
    elif oldcoords[1] == coords[1]:
        if oldcoords[0] > coords[0]:
            inc = -1
        else:
            inc = 1
        for i in range(oldcoords[0], coords[0], inc):
            candidate = (i, coords[1])
            if candidate in visited:
                print(sum(abs(coord) for coord in candidate))
                sys.exit(0)
            visited.add(candidate)
