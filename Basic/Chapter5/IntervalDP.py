"""
Interval DP
"""
"""
282. 石子合并
https://www.acwing.com/problem/content/284/
"""

n = int(input())
nums = list(map(int, input().split()))
f = [[1e9] * n for _ in range(n)]
for i in range(n):
    f[i][i] = 0
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + nums[i - 1]

for interval in range(2, n + 1):
    # left: i, right: i + interval - 1
    # enumerate left start
    for i in range(n - interval + 1):
        l, r = i, i + interval - 1
        for k in range(l, r):
            f[l][r] = min(f[l][r], f[l][k] + f[k + 1][r] + s[r + 1] - s[l])
print(f[0][n - 1])
