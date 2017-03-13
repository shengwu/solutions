from collections import defaultdict

def groupingDishes(dishes):
    ing_map = defaultdict(list)
    for dish in dishes:
        for ing in dish[1:]:
            ing_map[ing].append(dish[0])
    result = []
    for k, v in ing_map.iteritems():
        if len(v) > 1:
            result.append([k] + sorted(v))
    return sorted(result)
