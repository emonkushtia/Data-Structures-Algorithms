# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays
# https://www.martinkysel.com/hackerrank-new-year-chaos-solution/

# def minimumBribes(q):
#     moves = 0
#     for pos, val in enumerate(q):
#         if (val - 1) - pos > 2:
#             print("Too chaotic")
#             return
#         for j in range(max(0, val - 2), pos):
#             if q[j] > val:
#                 moves += 1
#     print(moves)


def minimumBribes(q):
    moves = 0
    for pos, val in enumerate(q):
        if val > pos+3:
            print("Too chaotic")
            return
        for j in range(max(0, val - 2), pos):
            if q[j] > val:
                moves += 1
    print(moves)



arr = [1, 2, 5, 3, 7, 8, 6, 4]

minimumBribes(arr)
#
# arr = [2, 5, 1, 3, 4]
# minimumBribes(arr)
