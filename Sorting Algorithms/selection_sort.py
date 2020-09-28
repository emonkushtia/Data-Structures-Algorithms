"""
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
from unsorted part and putting it at the beginning
"""


def selection_sort(arr, n):
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


arr = [24, 67, 11, 6, 89, 24]
arr_val = selection_sort(arr, len(arr))
print(arr_val)
