def reverse_if_odd(msg, n):
    def f(pair):
        if pair[0] % 2 == 1:
            # Odd-numbered segment; reverse the pair
            return msg[pair[1]+n-1:pair[1]-1:-1]
        else:
            # Even-numbered segment; return part untouched
            return msg[pair[1]:pair[1]+n]
    return f

n = input()
while n != 0:
    raw_msg = raw_input()
    msg_fn = reverse_if_odd(raw_msg, n)
    starts = range(0, len(raw_msg), n)
    fixed_msg = ''.join(map(msg_fn, enumerate(starts)))
    print ''.join(map(lambda x: fixed_msg[x::n], range(n)))
    n = input()
