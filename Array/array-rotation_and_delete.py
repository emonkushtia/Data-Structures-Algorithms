# https://practice.geeksforgeeks.org/problems/rotate-and-delete/0

N = int(input())
A = list(map(int, input().split()))
if N == 1:
    print(A[0])
elif N % 2:
    new = N - 3
    new = new // 4
    new = new + 3
    print(A[new - 1])
else:
    new = N - 2
    new = new // 4
    new = new + 2
    print(A[new - 1])