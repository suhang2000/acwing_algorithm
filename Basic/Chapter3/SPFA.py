"""
SPFA
queue optimization of Bellman-Ford algorithm
"""
import collections
from math import inf

"""
851. spfa求最短路
https://www.acwing.com/problem/content/853/
"""

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
dist = [inf] * (n + 1)
state = [False] * (n + 1)
for _ in range(m):
    x, y, z = map(int, input().split())
    g[x].append((y, z))


def spfa_shortest_path():
    global n
    dq = collections.deque()

    dq.append(1)
    dist[1] = 0
    state[1] = True

    while dq:
        x = dq.pop()
        state[x] = False
        for y, z in g[x]:
            if dist[y] > dist[x] + z:
                dist[y] = dist[x] + z
                if not state[y]:
                    # don't repeat add
                    state[y] = True
                    dq.append(y)

    return dist[n]


res = spfa_shortest_path()
print(res if res != inf else "impossible")
