"""
BFS of Tree
"""
import collections

"""
847. 图中点的层次
https://www.acwing.com/problem/content/849/
"""
n, m = map(int, input().split())
# init adjacency list
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)


def bfs():
    global n
    dq = collections.deque()
    dq.append(1)
    d = [-1] * (n + 1)
    d[1] = 0
    while dq:
        x = dq.popleft()
        for y in g[x]:
            if d[y] == -1:
                d[y] = d[x] + 1
                dq.append(y)
            if y == n:
                return d[y]
    return -1


print(bfs())
