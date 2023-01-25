"""
Dijkstra
"""
from math import inf

"""
849. Dijkstra求最短路 I
https://www.acwing.com/problem/content/851/
"""

n, m = map(int, input().split())
g = [[inf] * (n + 1) for i in range(n + 1)]
for i in range(m):
    x, y, z = map(int, input().split())
    # g[x][y] = z
    # 因为有重边，需要额外判断一下，记录最小的边
    # 自环不用管，因为后面更新距离时g[x][y]始终是正数，不会影响 dist[j] = min(dist[j], dist[j] + g[j][j]) 的值
    g[x][y] = min(g[x][y], z)
determined = [False] * (n + 1)
dist = [inf] * (n + 1)


def dijkstra():
    global n
    dist[1] = 0
    for i in range(1, n + 1):
        mn = -1
        # 从没确定最短距离的点中，取出最短路径的点
        for j in range(1, n + 1):
            if not determined[j] and (mn == -1 or dist[mn] > dist[j]):
                mn = j
        determined[mn] = True
        # 更新距离
        for j in range(1, n + 1):
            dist[j] = min(dist[j], dist[mn] + g[mn][j])
    if dist[n] == inf:
        return -1
    return dist[n]


print(dijkstra())
