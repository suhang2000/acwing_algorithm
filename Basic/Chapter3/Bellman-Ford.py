"""
Bellman-Ford
"""
from math import inf

"""
853. 有边数限制的最短路
https://www.acwing.com/problem/content/855/
"""

n, m, k = map(int, input().split())
g = []
for _ in range(m):
    x, y, z = map(int, input().split())
    g.append((x, y, z))
dist = [inf] * (n + 1)


def bellman_ford():
    global n, k
    dist[1] = 0
    # 循环k次
    for _ in range(k):
        backup = dist.copy()
        # 每次循环遍历所有的边
        for x, y, z in g:
            dist[y] = min(dist[y], backup[x] + z)
    return dist[n]


res = bellman_ford()
print("impossible" if res == inf else res)
