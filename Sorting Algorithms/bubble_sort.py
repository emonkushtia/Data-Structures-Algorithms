"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
"""


def bubble_sort(arr, n):
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [24, 67, 11, 6, 89, 24]
arr_val = bubble_sort(arr, len(arr))
print(arr_val)
