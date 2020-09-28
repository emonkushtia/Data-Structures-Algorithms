
def min_heapify(arr):
    i = len(arr)
    left = 2*i +1
    right = left + 1
    parent = (i+1)//2
    if parent<0:
        return
    if arr[left]> arr[parent]:
        pass







array = [4,6,2,8,50]
min_heapify(array)
