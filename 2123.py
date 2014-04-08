n = input()
eps = 0.0000000001
while n != -1:
    candies = []
    for i in range(n):
        candies.append(input())
    mean = float(sum(candies))/len(candies)
    if abs(mean - round(mean)) < eps:
        print int(sum(filter(lambda x: x > 0, [mean - x for x in candies])))
    else:
        print -1
    n = input()
