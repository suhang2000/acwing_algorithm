"""
Prim algorithm: MST(minimum spanning tree)
"""
from math import inf

"""
858. Prim算法求最小生成树
https://www.acwing.com/problem/content/860/
"""

n, m = map(int, input().split())
# adjacent matrix
g = [[inf] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    g[u][v] = g[v][u] = min(g[u][v], w)  # remove duplicate edges
for i in range(1, n + 1):
    g[i][i] = 0  # remove self cycles


def prim():
    global n
    dist = [inf] * (n + 1)  # distance between node and connected block
    state = [False] * (n + 1)  # if node in connected block
    res = 0

    for i in range(n):
        t = -1
        # find the nearest node to the connected block
        for j in range(1, n + 1):
            if not state[j] and (t == -1 or dist[t] > dist[j]):
                t = j
        if i and dist[t] == inf:
            # can't connect
            return inf
        if i:
            res += dist[t]
        # update other node from t
        for j in range(1, n + 1):
            dist[j] = min(dist[j], g[t][j])
        state[t] = True

    return res


res = prim()
print(res if res != inf else "impossible")


# template
def prim_template():
    global n
    dist = [inf] * (n + 1)  # distance between node and connected block
    state = [False] * (n + 1)  # if node in connected block
    dist[1] = 0
    res = 0

    for i in range(n):
        t = -1
        # find the nearest node to the connected block
        for j in range(1, n + 1):
            if not state[j] and (t == -1 or dist[t] > dist[j]):
                t = j
        if dist[t] == inf:
            return inf
        res += dist[t]
        state[t] = True
        # update other nodes
        for j in range(1, n + 1):
            dist[j] = min(dist[j], g[t][j])

    return res
