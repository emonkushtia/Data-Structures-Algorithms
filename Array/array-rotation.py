"""
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
Input Array  = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
Output Array = [3, 4, 5, 6, 7, 1, 2]
"""


def left_rotate_by_one(arr, d, n):
    for i in range(d):
        temp = arr[0]
        for j in range(n - 1):
            arr[j] = arr[j + 1]
        arr[n - 1] = temp


arr = [1, 2, 3, 4, 5, 6, 7]
# left_rotate_by_one(arr, 2, len(arr))
print(arr)


def temp_array(arr, d, n):
    temp = arr[:d]
    arr = arr[d:]
    for t in temp:
        arr.append(t)
    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
arr = temp_array(arr, 2, len(arr))
print(arr)