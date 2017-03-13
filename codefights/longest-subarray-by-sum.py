# https://codefights.com/interview/rm8sj82SYiJYApvKw

def findLongestSubarrayBySum(goal, arr):
    sums = [0]
    s = 0
    for elem in arr:
        s += elem
        sums.append(s)
    curr = [-1]
    i = 0
    j = 0
    while j < len(arr):
        cs = sums[j+1] - sums[i]
        if cs == goal:
            if curr == [-1] or j - i > curr[1] - curr[0]:
                curr = [i, j]
            j += 1
        elif cs < goal:
            j += 1
        else:
            i += 1
    if len(curr) == 1:
        return curr
    return [curr[0]+1, curr[1]+1]
