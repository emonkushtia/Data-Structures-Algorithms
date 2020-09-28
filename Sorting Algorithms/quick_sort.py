"""
QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.
There are many different versions of quickSort that pick pivot in different ways.
    - Always pick first element as pivot.(implemented below)
    - Always pick last element as pivot
    - Pick a random element as pivot.
    - Pick median as pivot.

This function takes first element as pivot, places the pivot element at its correct position in sorted array,
and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot
"""


def quick_sort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quick_sort(less) + equal + quick_sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array


arr = [10, 7, 8, 9, 1, 5]
arr = quick_sort(arr)
print("Sorted array is: ", arr)
