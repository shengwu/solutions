def sortedSquaredArray(array):
    squared = [a**2 for a in array]
    split_pt = 0
    while split_pt < len(array) and array[split_pt] < 0:
        split_pt += 1
    other_arr = squared[:split_pt][::-1]
    result = []
    i = split_pt
    j = 0
    while i < len(array) and j < len(other_arr):
        if squared[i] < other_arr[j]:
            result.append(squared[i])
            i += 1
        else:
            result.append(other_arr[j])
            j += 1
    if i >= len(array):
        result += other_arr[j:]
    elif j >= len(other_arr):
        result += squared[i:]
    return result
