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

"""
3. 完全背包问题
https://www.acwing.com/problem/content/3/
"""

n, volume = map(int, input().split())
dp = [0] * (volume + 1)
for i in range(n):
    v, w = map(int, input().split())
    for j in range(v, volume + 1):
        dp[j] = max(dp[j], dp[j - v] + w)
print(dp[-1])

"""
4. 多重背包问题 I
https://www.acwing.com/problem/content/4/
"""

# version 1
n, volume = map(int, input().split())
dp = [[0] * (volume + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    v, w, s = map(int, input().split())
    for j in range(volume + 1):
        for k in range(s + 1):
            if k * v > j:
                break
            dp[i][j] = max(dp[i][j], dp[i - 1][j - k * v] + k * w)
print(dp[-1][-1])

# version 2
n, volume = map(int, input().split())
dp = [0] * (volume + 1)
for i in range(n):
    v, w, s = map(int, input().split())
    for j in range(volume, v - 1, -1):
        for k in range(s + 1):
            if k * v > j:
                break
            dp[j] = max(dp[j], dp[j - k * v] + k * w)
print(dp[-1])

"""
5. 多重背包问题 II
https://www.acwing.com/problem/content/5/
二进制优化，转化为01背包
"""

n, volume = map(int, input().split())
v, w = [], []
for i in range(n):
    a, b, s = map(int, input().split())
    k = 1
    # 二进制优化
    while k <= s:
        v.append(k * a)
        w.append(k * b)
        s -= k
        k *= 2
    if s:
        # 注意这里是s乘，不是k
        v.append(s * a)
        w.append(s * b)
# 01 knapsack
m = len(v)
dp = [0] * (volume + 1)
for i in range(m):
    for j in range(volume, v[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - v[i]] + w[i])
print(dp[-1])
