"""
Linear DP
"""
from math import inf

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
