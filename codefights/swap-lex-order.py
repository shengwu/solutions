# https://codefights.com/interview/vG6SManzGDZsoqsh7
#
# Given a string str and array of pairs that indicates which indices in the
# string can be swapped, return the lexicographically largest string that
# results from doing the allowed swaps. You can swap indices any number of
# times.
#
# Example
#
# For str = "abdc" and pairs = [[1, 4], [3, 4]], the output should be
# swapLexOrder(str, pairs) = "dbca".
#
# By swapping the given indices, you get the strings: "cdba", "cbad", "dbac",
# "dbca". The lexicographically largest string in this list is "dbca".

def lettersAtIndices(orig, indices):
    return sorted((orig[i-1] for i in indices), reverse=True)

def swapLexOrder(orig, pairs):
    # First, merge all of the pairs into sets of indices
    # If two indices are in a set, it means that the
    # letters at those positions can be interchanged
    groups = []
    for a, b in pairs:
        oldGroups = []
        for i, group in enumerate(groups):
            if a in group or b in group:
                group.add(a)
                group.add(b)
                oldGroups.append(i)
        if len(oldGroups) == 0:
            groups.append(set([a, b]))
        elif len(oldGroups) > 1:
            total = set()
            for groupId in oldGroups[::-1][:-1]:
                total |= groups.pop(groupId)
            groups[oldGroups[0]] |= total

    # letterMap is a map from index -> the lexicographically
    # largest letter we can put at that index
    letterMap = {}
    for group in groups:
        letterMap.update(dict(zip(
            sorted(i-1 for i in group),
            lettersAtIndices(orig, group)
        )))

    result = []
    for i in xrange(len(orig)):
        if i in letterMap:
            result.append(letterMap[i])
        else:
            result.append(orig[i])
    return ''.join(result)
