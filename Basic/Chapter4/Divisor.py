"""
Divisor
"""

"""
869. 试除法求约数
https://www.acwing.com/problem/content/871/
"""

n = int(input())
for _ in range(n):
    a = int(input())
    res = []
    i = 1
    while i <= a // i:
        if a % i == 0:
            res.append(i)
            if a // i != i:
                res.append(a // i)
        i += 1
    res.sort()
    print(*res)

# Version 2
n = int(input())
for _ in range(n):
    a = int(input())
    res = []
    i = 1
    while i <= a // i:
        if a % i == 0:
            res.append(i)
        i += 1
    idx = len(res) - 1
    if a // res[-1] == res[-1]:
        idx -= 1
    while idx >= 0:
        res.append(a // res[idx])
        idx -= 1
    print(*res)
