"""
Content 89
"""
"""
4803. 满足的数
https://www.acwing.com/problem/content/4806/
"""

n = int(input())
nums = map(int, input().split())
s = sum(nums)
res = 0
for i in range(1, 6):
    if (s + i) % (n + 1) != 1:
        res += 1
print(res)

"""
4804. 构造矩阵
https://www.acwing.com/problem/content/4807/
"""

m, n = map(int, input().split())
b = []
for _ in range(m):
    b.append(list(map(int, input().split())))
a = [[1] * n for _ in range(m)]
for i, row in enumerate(b):
    for j, val in enumerate(row):
        if val == 0:
            for x in range(n):
                a[i][x] = 0
            for x in range(m):
                a[x][j] = 0
flag = True
for i, row in enumerate(b):
    for j, val in enumerate(row):
        if val == 1:
            s = sum(a[i])
            for x in range(m):
                s += a[x][j]
            if s == 0:
                flag = False
                break
if flag:
    print("YES")
    for i in range(m):
        print(*a[i])
else:
    print("NO")

"""
4805. 加减乘
https://www.acwing.com/problem/content/4808/
"""

n, x, y = map(int, input().split())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    if i & 1:
        dp[i] = min(dp[i-1] + x, dp[i//2+1]+x+y)
    else:
        dp[i] = min(dp[i-1] + x, dp[i//2] + y)
print(dp[-1])
