"""
Selection Sort Algorithm:
    Selection sort is an algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.

Time Complexities:
    Worst Case Complexity:O(n2)
        If we want to sort in ascending order and the array is in descending order then, the worst case occurs.
    Best Case Complexity:O(n2)
        It occurs when the array is already sorted
    Average Case Complexity:O(n2)
        It occurs when the elements of the array are in jumbled order (neither ascending nor descending).

Space Complexity:
    Space complexity is O(1) because an extra variable temp is used.

Bubble Sort Applications
    The selection sort is used when:
        a small list is to be sorted
        cost of swapping does not matter
        checking of all the elements is compulsory
        cost of writing to a memory matters like in flash memory (number of writes/swaps is O(n) as compared to O(n2) of bubble sort)
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
