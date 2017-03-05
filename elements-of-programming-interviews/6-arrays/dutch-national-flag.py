def partition_into_three(arr, pivot):
    smaller = 0
    for i in xrange(len(arr)):
        if arr[i] < pivot:
            arr[i], arr[smaller] = arr[smaller], arr[i]
            smaller += 1
    larger = len(arr) - 1
    for i in xrange(len(arr)-1, smaller-1, -1):
        if arr[i] > pivot:
            arr[i], arr[larger] = arr[larger], arr[i]
            larger -= 1
    return arr

example = [1, 10, 3, 7, 2, 4, 5, 3]
print partition_into_three(example, 1)
print partition_into_three(example, 2)
print partition_into_three(example, 3)
print partition_into_three(example, 4)
print partition_into_three(example, 5)
print partition_into_three(example, 7)
print partition_into_three(example, 10)
