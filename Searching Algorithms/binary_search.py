'''
Binary Search: These algorithms are specifically designed for searching in sorted data-structures.
    These type of searching algorithms are much more efficient than Linear Search as they repeatedly
    target the center of the search structure and divide the search space in half
'''


def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    index = -1
    while first <= last and index == -1:
        mid = (first + last) // 2
        if item_list[mid] == item:
            index = mid
        elif item < item_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return index


def binary_recursive(arr, lower_index, upper_index, search_value):
    if lower_index <= upper_index:
        mid_index = (lower_index + upper_index) // 2
        if arr[mid_index] == search_value:
            return mid_index
        elif search_value < arr[mid_index]:
            return binary_recursive(arr, lower_index, mid_index - 1, search_value)
        else:
            return binary_recursive(arr, mid_index + 1, upper_index, search_value)
    else:
        return -1


array = [1, 2, 3, 5, 8]
print(binary_search(array, 7))
print(binary_search(array, 5))

print(binary_recursive(array, 0, len(array) - 1, 7))
print(binary_recursive(array, 0, len(array) - 1, 2))
