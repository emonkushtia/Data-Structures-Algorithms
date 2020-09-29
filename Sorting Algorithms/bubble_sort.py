"""
Bubble Sort Algorithm:
    Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

Time Complexities:
    Worst Case Complexity:O(n2)
        If we want to sort in ascending order and the array is in descending order then, the worst case occurs.
    Best Case Complexity:O(n)
        If the array is already sorted, then there is no need for sorting.
    Average Case Complexity:O(n2)
        It occurs when the elements of the array are in jumbled order (neither ascending nor descending).

Space Complexity:
    Space complexity is O(1) because an extra variable temp is used for swapping.
    In the optimized algorithm, the variable swapped adds to the space complexity thus, making it O(2).

Bubble Sort Applications
    Bubble sort is used in the following cases where
        the complexity of the code does not matter.
        a short code is preferred.
"""


def bubble_sort(arr, n):
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def optimized_bubble_sort(arr, n):
    for i in range(n):
        swapped = True
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = False
        if swapped:
            break
    return arr


arr = [24, 67, 11, 6, 89, 24]
arr_val = bubble_sort(arr, len(arr))
arr_val = optimized_bubble_sort([6, 11, 10, 24, 67, 89], len(arr))
print(arr_val)
