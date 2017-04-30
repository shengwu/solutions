# https://codefights.com/arcade/graphs-arcade/kingdom-roads/pmmMeP4JkqgKbzyTy

from collections import defaultdict
from copy import deepcopy

def removeFromNeighbors(neighbors, city):
    for v in neighbors.itervalues():
        if city in v:
            v.remove(city)

def citiesConquering(n, roads):
    neighbors = defaultdict(list)
    for a, b in roads:
        neighbors[a].append(b)
        neighbors[b].append(a)
        
    result = [-1] * n
    conqueredCity = True
    day = 1
    while conqueredCity:
        conqueredCity = False
        nextDayNeighbors = deepcopy(neighbors)
        for i in xrange(n):
            if result[i] == -1 and len(neighbors[i]) <= 1:
                result[i] = day
                conqueredCity = True
                removeFromNeighbors(nextDayNeighbors, i)
        neighbors = nextDayNeighbors
        day += 1
    return result
        

roads = [[1, 0], [1, 2], [8, 5], [9, 7],
         [5, 6], [5, 4], [4, 6], [6, 7]]
print citiesConquering(10, roads)
