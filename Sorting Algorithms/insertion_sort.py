"""
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
