# Algorithm taken from http://rosettacode.org/wiki/Pi#Python
 
import sys
import time

def calc_pi():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4*q+r-t < n*t:
            yield n
            nr = 10*(r-n*t)
            n = ((10*(3*q+r))//t)-10*n
            q *= 10
            r = nr
        else:
            nr = (2*q+r)*l
            nn = (q*(7*k)+2+(r*l))//(t*l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr

pi_digits = calc_pi()
dot = True
start = time.time()
for d in pi_digits:
    sys.stdout.write(str(d))
    if dot:
        sys.stdout.write('.')
        dot = False
    if time.time() - start > 24.5:
        break
