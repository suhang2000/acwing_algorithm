"""
Floyd
"""
from math import inf

"""
854. Floyd求最短路
https://www.acwing.com/problem/content/856/
"""

n, m, k = map(int, input().split())
# adjacent matrix
g = [[inf] * (n + 1) for i in range(n + 1)]
# 多源，去除所有点的自环
for i in range(1, n + 1):
    g[i][i] = 0
for _ in range(m):
    x, y, z = map(int, input().split())
    g[x][y] = min(g[x][y], z)   # 去除重边


def floyd():
    global n
    for node in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                g[i][j] = min(g[i][j], g[i][node] + g[node][j])


floyd()
for _ in range(k):
    x, y = map(int, input().split())
    print(g[x][y] if g[x][y] != inf else "impossible")
