instructions = '''
cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 14 c
cpy 14 d
inc a
dec d
jnz d -2
dec c
jnz c -5
'''.strip().split('\n')

regs = 'abcd'

def run_program(reg_vals):
    pt = 0
    while pt < len(instructions):
        parts = instructions[pt].split()
        if parts[0] == 'cpy':
            if parts[1] in regs:
                reg_vals[parts[2]] = reg_vals[parts[1]]
            else:
                reg_vals[parts[2]] = int(parts[1])
            pt += 1
        elif parts[0] == 'inc':
            reg_vals[parts[1]] += 1
            pt += 1
        elif parts[0] == 'dec':
            reg_vals[parts[1]] -= 1
            pt += 1
        elif parts[0] == 'jnz':
            if parts[1] in regs:
                val = reg_vals.get(parts[1], 0)
            else:
                val = int(parts[1])
            if val != 0:
                pt += int(parts[2])
            else:
                pt += 1

# part 1 - answer was 318007
reg_vals = {r: 0 for r in regs}
run_program(reg_vals)
print reg_vals['a']

# part 2 - answer was 9227661
reg_vals = {r: 0 for r in regs}
reg_vals['c'] = 1
run_program(reg_vals)
print reg_vals['a']
