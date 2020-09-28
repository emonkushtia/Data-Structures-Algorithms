# https://www.hackerrank.com/challenges/minimum-swaps-2/problem

def minimumSwaps(arr):
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i + 1:
            swaps += 1
            t = arr[i]
            arr[i] = i + 1
            arr[temp[i + 1]] = t
            temp[t] = temp[i + 1]
    return swaps


array = [1, 3, 5, 2, 4, 6, 7]
print(minimumSwaps(array))
