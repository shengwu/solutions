inp = '''
#ip 5
seti 123 0 3
bani 3 456 3
eqri 3 72 3
addr 3 5 5
seti 0 0 5
seti 0 0 3
bori 3 65536 2
seti 14070682 0 3
bani 2 255 1
addr 3 1 3
bani 3 16777215 3
muli 3 65899 3
bani 3 16777215 3
gtir 256 2 1
addr 1 5 5
addi 5 1 5
seti 27 8 5
seti 0 3 1
addi 1 1 4
muli 4 256 4
gtrr 4 2 4
addr 4 5 5
addi 5 1 5
seti 25 8 5
addi 1 1 1
seti 17 9 5
setr 1 4 2
seti 7 5 5
eqrr 3 0 1
addr 1 5 5
seti 5 4 5
'''

def exec_cmd(cmd, regs, ip, ip_reg):
    proccmd = cmd[0]
    a, b, c = cmd[1:]
    # make a copy
    result = list(regs)
    result[ip_reg] = ip
    if proccmd == 'addr':
        result[c] = result[a] + result[b]
    elif proccmd == 'addi':
        result[c] = result[a] + b
    elif proccmd == 'mulr':
        result[c] = result[a] * result[b]
    elif proccmd == 'muli':
        result[c] = result[a] * b
    elif proccmd == 'banr':
        result[c] = result[a] & result[b]
    elif proccmd == 'bani':
        result[c] = result[a] & b
    elif proccmd == 'borr':
        result[c] = result[a] | result[b]
    elif proccmd == 'bori':
        result[c] = result[a] | b
    elif proccmd == 'setr':
        result[c] = result[a]
    elif proccmd == 'seti':
        result[c] = a
    elif proccmd == 'gtir':
        if a > result[b]:
            result[c] = 1
        else:
            result[c] = 0
    elif proccmd == 'gtri':
        if result[a] > b:
            result[c] = 1
        else:
            result[c] = 0
    elif proccmd == 'gtrr':
        if result[a] > result[b]:
            result[c] = 1
        else:
            result[c] = 0
    elif proccmd == 'eqir':
        if a == result[b]:
            result[c] = 1
        else:
            result[c] = 0
    elif proccmd == 'eqri':
        if result[a] == b:
            result[c] = 1
        else:
            result[c] = 0
    elif proccmd == 'eqrr':
        if result[a] == result[b]:
            result[c] = 1
        else:
            result[c] = 0
    return result, result[ip_reg]

rows = inp.strip().split('\n')
insts = []
ip_reg = int(rows[0].split()[1])
for row in rows[1:]:
    parts = row.split()
    inst = parts[0]
    a, b, c = [int(p) for p in parts[1:]]
    insts.append((inst, a, b, c))


regs = [0] * 6
ip = 0
while True:
    regs, ip = exec_cmd(insts[ip], regs, ip, ip_reg)
    if ip == 27:
        print regs[3]
        break
    ip += 1

regs = [0] * 6
ip = 0
seen = {}
count = 0
while True:
    regs, ip = exec_cmd(insts[ip], regs, ip, ip_reg)
    if ip == 27 and regs[3] in seen:
        break
    elif ip == 27:
        seen[regs[3]] = count
    count += 1
    ip += 1

# part 2
print max(seen.items(), key=lambda i: i[1])[0]
