"""
prefix sum
"""
"""
795. 前缀和
https://www.acwing.com/problem/content/797/
"""

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = [0] * (n + 1)
for i, x in enumerate(arr):
    s[i+1] = s[i] + x
for _ in range(m):
    l, r = map(int, input().split())
    print(s[r] - s[l-1])

"""
796. 子矩阵的和
https://www.acwing.com/problem/content/798/
"""

n, m, q = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
s = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + matrix[i-1][j-1]
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    print(s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1])
