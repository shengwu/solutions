from collections import Counter, defaultdict

inp = '''
#ip 4
addi 4 16 4
seti 1 9 3
seti 1 6 2
mulr 3 2 5
eqrr 5 1 5
addr 5 4 4
addi 4 1 4
addr 3 0 0
addi 2 1 2
gtrr 2 1 5
addr 4 5 4
seti 2 9 4
addi 3 1 3
gtrr 3 1 5
addr 5 4 4
seti 1 0 4
mulr 4 4 4
addi 1 2 1
mulr 1 1 1
mulr 4 1 1
muli 1 11 1
addi 5 1 5
mulr 5 4 5
addi 5 2 5
addr 1 5 1
addr 4 0 4
seti 0 1 4
setr 4 3 5
mulr 5 4 5
addr 4 5 5
mulr 4 5 5
muli 5 14 5
mulr 5 4 5
addr 1 5 1
seti 0 6 0
seti 0 7 4
'''

#inp = '''
#seti 5 0 1
#seti 6 0 2
#addi 0 1 0
#addr 1 2 3
#setr 1 0 0
#seti 8 0 4
#seti 9 0 5
#'''

ip_reg = 4
#ip_reg = 0
def exec_cmd(cmd, regs, ip):
    #print cmd
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

for row in rows[1:]:
    parts = row.split()
    inst = parts[0]
    a, b, c = [int(p) for p in parts[1:]]
    cmd = [inst, a, b, c]
    insts.append(cmd)
    #print cmd

'''
regs = [0] * 6
regs[0] = 1
#regs[5] = 10551260 - 1
ip = 0
while ip < len(insts):
    regs, ip = exec_cmd(insts[ip], regs, ip)
    #regs[5] = 10551260 - 1
    print regs, ip
    raw_input()
    ip += 1
print regs[0]
'''


# 0 is not correct
# 527563 is not correct
# 527572 is not correct
# 11078861 is not correct!!


# part 2 test code

'''
regs = [0, 10551260, 527562*5, 4, 2, 0]
#regs = [527563, 10551260, 10551259, 10551260, 11, 0]
ip = 3
while ip < len(insts):
    regs, ip = exec_cmd(insts[ip], regs, ip)
    #regs[5] = 10551260 - 1
    print regs, ip
    raw_input()
    ip += 1
print regs[0]
'''


# Analysis
# ========
# 
# 0 ['addi', 4, 16, 4]
# 1 ['seti', 1, 9, 3]
# 2 ['seti', 1, 6, 2]
# 3 ['mulr', 3, 2, 5]
# 4 ['eqrr', 5, 1, 5]
# 5 ['addr', 5, 4, 4]
# 6 ['addi', 4, 1, 4]
# 7 ['addr', 3, 0, 0]
# 8 ['addi', 2, 1, 2]
# 9 ['gtrr', 2, 1, 5]
# 10 ['addr', 4, 5, 4]
# 11 ['seti', 2, 9, 4]
# 12 ['addi', 3, 1, 3]
# 13 ['gtrr', 3, 1, 5]
# 14 ['addr', 5, 4, 4]
# 15 ['seti', 1, 0, 4]
# 16 ['mulr', 4, 4, 4]
# 17 ['addi', 1, 2, 1]
# 18 ['mulr', 1, 1, 1]
# 19 ['mulr', 4, 1, 1]
# 20 ['muli', 1, 11, 1]
# 21 ['addi', 5, 1, 5]
# 22 ['mulr', 5, 4, 5]
# 23 ['addi', 5, 2, 5]
# 24 ['addr', 1, 5, 1]
# 25 ['addr', 4, 0, 4]
# 26 ['seti', 0, 1, 4]
# 27 ['setr', 4, 3, 5]
# 28 ['mulr', 5, 4, 5]
# 29 ['addr', 4, 5, 5]
# 30 ['mulr', 4, 5, 5]
# 31 ['muli', 5, 14, 5]
# 32 ['mulr', 5, 4, 5]
# 33 ['addr', 1, 5, 1]
# 34 ['seti', 0, 6, 0]
# 35 ['seti', 0, 7, 4]
# 
# 
# -- 0 -> add 16 to register 4
# put 1 in reg 3
# put 1 in reg 2
# reg 5 = reg 3 x reg 2
# reg 5 = 1 if reg 5 == reg 1 else 0
# -- 5-> reg 4 = reg 4 + reg 5
# reg 4 = reg 4 + (1)
# reg 0 = reg 3 + reg 0
# reg 2 = reg 2 + (1)
# reg 5 = 1 if reg 2 > reg 1 else 0
# -- 10 -> reg 4 = reg 5 + reg 4
# reg 4 = 2
# reg 3 = (1) + reg 3
# reg 5 = 1 if reg 3 > reg 1 else 0
# reg 4 = reg 5 + reg 4
# -- 15 -> reg 4 = 1
# reg 4 = reg 4 * reg 4
# reg 1 = reg 1 + (2)
# reg 1 = reg 1 * reg 1
# reg 1 = reg 4 * reg 1
# -- 20 -> reg 1 = reg 1 * 11
# reg 5 = reg 5 + (1)
# reg 5 = reg 5 * reg 4
# reg 5 = reg 5 + (2)
# reg 1 = reg 1 + reg 5
# -- 25 -> reg 4 = reg 4 + reg 0
# reg 4 = 0
# reg 5 = reg 4
# reg 5 = reg 5 * reg 4
# reg 5 = reg 4 + reg 5
# -- 30 -> reg 5 = reg 4 * reg 5
# reg 5 = reg 5 * (14)
# reg 5 = reg 5 * reg 4
# reg 1 = reg 1 + reg 5
# reg 0 = 0
# -- 35 -> reg 4 = 0
# 
# 
# - instructions 34 and 35, i wonder if they ever get executed
# reg 0 only gets set  in instruction 7 and 34
# inst 7 adds reg 3 to it
# reg 3?
# inst 5 skips the next instruction if reg 5 == reg 1
# 
# 
# this is the beginning of the execution!!
 # 
# [1, 0, 0, 0, 16, 0] 16
# [1, 2, 0, 0, 17, 0] 17
# [1, 4, 0, 0, 18, 0] 18
# [1, 76, 0, 0, 19, 0] 19
# [1, 836, 0, 0, 20, 0] 20
# [1, 836, 0, 0, 21, 1] 21
# [1, 836, 0, 0, 22, 22] 22
# [1, 836, 0, 0, 23, 24] 23
# [1, 860, 0, 0, 24, 24] 24
# [1, 860, 0, 0, 26, 24] 26
# [1, 860, 0, 0, 27, 27] 27
# [1, 860, 0, 0, 28, 756] 28
# [1, 860, 0, 0, 29, 785] 29
# [1, 860, 0, 0, 30, 23550] 30
# [1, 860, 0, 0, 31, 329700] 31
# [1, 860, 0, 0, 32, 10550400] 32
# [1, 10551260, 0, 0, 33, 10550400] 33
# [0, 10551260, 0, 0, 34, 10550400] 34
# [0, 10551260, 0, 0, 0, 10550400] 0
# 
# 
# kind of interesting when it breaks the 2-10 loop
# (read: registers after executing instruction 12, instruction 12)
# 
# [0, 10551260, 10551261, 2, 12, 0] 12
# [0, 10551260, 10551261, 2, 13, 0] 13
# [0, 10551260, 10551261, 2, 14, 0] 14
# [0, 10551260, 10551261, 2, 1, 0] 1
# [0, 10551260, 1, 2, 2, 0] 2
# [0, 10551260, 1, 2, 3, 2] 3
# [0, 10551260, 1, 2, 4, 0] 4
# [0, 10551260, 1, 2, 5, 0] 5
# 
# prime factorization of 
# 10551260
# 2 × 2 × 5 × 527563
# 
# the value of reg 0 when reg e becomes 10551261 is what it will be when it exits
# the only times things get copied into reg 0 are when 
# reg 5 == reg 1
# or
# 
# if reg 2 x reg 3 == reg 1
# reg 0 += reg 3
# 
# 
# reg 2 is an incrementing counter that doesn't stop until it reaches reg 1
# the only time reg 2 x reg 3 == reg 1
# reg 3 == reg 1 / reg 2 evenly
# or reg 3 == reg 1 % reg 2 == 0 evenly
# 
# 
# reg 3 is fixed for an entire "run"
# so it's run for 
# 
# then 
# 10551260 and 1
# reg 0 += 1
# 
# let's start reg 2 at 527562*5*2 and reg 3 is 2
# then reg 0 += 2
# 
# reg 0 += 4 (FORGOT)
# 
# starting reg 2 at 527562*4, and reg 3 is 5
# reg 0 gets 5 added to it
# 
# starting reg 2 at 527562*2, and reg 3 is 10
# reg 0 gets 10 added to it
# 
# starting reg 2 at 527562, and reg 3 is 20
# reg 0 gets 20 added to it
# 
# startig reg 2 at 20 and reg 3 is 527563
# reg 0 gets 527563 added to it
# 
# reg 0 += 10551260
# 
# 2 x 2 x 5 x ...
# 
# 1 + 2 + 4 + 5 + 10 + 20
# 10551260 + ...
# =
# 22157688 is my guess now
# CORRECT!
# 
# but 
# 1 + 2 + 5+ 10 + 20 + 527563 + 10551260
# 11078861
# is not correct!
# 
# maybe we're missing some border conditions
