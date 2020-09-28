'''
Linear Search:  In this, the list or array is traversed sequentially and every element is checked
'''


def linear_search(item_list, item):
    for i in range(len(item_list)):
        if item_list[i] == item:
            return i
    return -1


array = [1, 2, 3, 5, 8]
print(linear_search(array, 7))
print(linear_search(array, 5))
