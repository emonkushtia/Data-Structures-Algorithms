from collections import defaultdict


def sherlockAndAnagrams(s):
    check = {}
    l = len(s)
    for i in range(l):
        for j in range(i + 1, l + 1):
            sub = list(s[i:j])
            sub.sort()
            sub = "".join(sub)
            if sub in check:
                check[sub] += 1
            else:
                check[sub] = 1
    sum = 0
    for i in check:
        n = check[i]
        sum += (n * (n - 1)) // 2
    return sum


print(sherlockAndAnagrams('abba'))
