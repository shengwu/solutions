import json

with open('12.txt') as f:
    d = json.load(f)

def add_all_numbers(root):
    if type(root) is int:
        return root
    if type(root) is unicode or type(root) is str:
        return 0
    if type(root) is list:
        return sum(add_all_numbers(elem) for elem in root)
    assert type(root) is dict
    s = 0
    for k, v in root.iteritems():
        s += add_all_numbers(k)
        s += add_all_numbers(v)
    return s

print add_all_numbers(d)


def add_all_numbers_ignoring_red(root):
    if type(root) is int:
        return root
    if type(root) is unicode or type(root) is str:
        return 0
    if type(root) is list:
        return sum(add_all_numbers_ignoring_red(elem) for elem in root)
    assert type(root) is dict
    if any(v == 'red' for v in root.itervalues()):
        return 0
    s = 0
    for k, v in root.iteritems():
        s += add_all_numbers_ignoring_red(k)
        s += add_all_numbers_ignoring_red(v)
    return s

assert add_all_numbers_ignoring_red([1,{"c":"red","b":2},3]) == 4
assert add_all_numbers_ignoring_red({"d":"red","e":[1,2,3,4],"f":5}) == 0
assert add_all_numbers_ignoring_red([1,"red",5]) == 6
# wrong answer 122688, too high
print add_all_numbers_ignoring_red(d)


# started 7:27
# ended 7:35
# wasted a few mins since i forgot to change the recursive references
