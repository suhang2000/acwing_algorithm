"""
Knapsack Problem
"""
"""
2. 01背包问题
https://www.acwing.com/problem/content/2/
"""

n, volume = map(int, input().split())
dp = [0] * (volume + 1)
for i in range(n):
    v, w = map(int, input().split())
    for j in range(volume, v - 1, -1):
        dp[j] = max(dp[j], dp[j - v] + w)
print(dp[-1])
