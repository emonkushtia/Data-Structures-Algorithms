"""
Insertion Sort Algorithm:
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


Algorithm
1.	Consider the first element to be sorted and the rest to be unsorted
2.	Compare with the second element:
	1.	If the second element< the first element, insert the element in the correct position of the sorted portion
	2.	Else, leave it as it is
3.	Repeat 1 and 2 until all elements are sorted
"""


# Insertion Sort In Python
#
# Performance Complexity = O(n^2)
# Space Complexity = O(n)


def insertion_sort(my_list):
    for index in range(1, len(my_list)):
        current = my_list[index]
        position = index

        while position > 0 and my_list[position - 1] > current:
            print("Swapped {} for {}".format(my_list[position], my_list[position - 1]))
            my_list[position] = my_list[position - 1]
            print(my_list)
            position -= 1

        my_list[position] = current

    return my_list


my_list = [8, 5, 1, 3, 5, 4]

print(insertion_sort(my_list))
