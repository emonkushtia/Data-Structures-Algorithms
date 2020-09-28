# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def rotLeft(a, d):
    return a[d:] + a[:d]


arr = [3, 6, 1, 20]
arr = rotLeft(arr, 2)
print(arr)
