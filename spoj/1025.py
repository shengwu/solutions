for i in range(input()):
    n = input()
    men = sorted([int(x) for x in raw_input().split()])
    women = sorted([int(x) for x in raw_input().split()])
    print sum(map(lambda x: men[x] * women[x], range(n)))
