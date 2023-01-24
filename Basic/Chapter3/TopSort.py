"""
Top Sort
"""
import collections

"""
848. 有向图的拓扑序列
https://www.acwing.com/problem/content/850/
"""
n, m = map(int, input().split())
res = []
# init adjacency list
g = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)  # in degree
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    degree[b] += 1


def top_sort():
    global n
    # BFS
    dq = collections.deque()
    for i in range(1, n + 1):
        if degree[i] == 0:
            dq.append(i)
    while dq:
        x = dq.popleft()
        res.append(x)
        for y in g[x]:
            degree[y] -= 1
            if degree[y] == 0:
                dq.append(y)


top_sort()
if len(res) == n:
    print(*res)
else:
    print(-1)
