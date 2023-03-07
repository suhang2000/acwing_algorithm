"""
Linear DP
"""
from math import inf

import cachetools

"""
898. 数字三角形
https://www.acwing.com/problem/content/900/
"""

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
dp = [[-inf] * n for _ in range(n)]
dp[0][0] = a[0][0]
for i in range(1, n):
    dp[i][0] = a[i][0] + dp[i - 1][0]
    for j in range(1, i + 1):
        dp[i][j] = a[i][j] + max(dp[i - 1][j], dp[i - 1][j - 1])
print(max(dp[-1]))

"""
895. 最长上升子序列
https://www.acwing.com/problem/content/897/
"""

n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n
for j in range(1, n):
    for i in range(j):
        if nums[i] < nums[j]:
            dp[j] = max(dp[j], dp[i] + 1)
print(max(dp))

"""
896. 最长上升子序列 II
https://www.acwing.com/problem/content/898/
"""

n = int(input())
nums = list(map(int, input().split()))
f = []
for x in nums:
    # binary search f
    l, r = 0, len(f) - 1
    while l <= r:
        mid = (l + r) >> 1
        if f[mid] >= x:
            r = mid - 1
        else:
            l = mid + 1
    if l == len(f):
        f.append(x)
    else:
        f[l] = x
print(len(f))

"""
897. 最长公共子序列
https://www.acwing.com/problem/content/899/
"""

n, m = map(int, input().split())
a = input()
b = input()
f = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        f[i][j] = f[i - 1][j - 1] + 1 if a[i - 1] == b[j - 1] else max(f[i - 1][j], f[i][j - 1])
print(f[-1][-1])
