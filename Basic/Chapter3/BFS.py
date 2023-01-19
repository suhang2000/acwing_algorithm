"""
BFS
"""
import collections

"""
844. 走迷宫
https://www.acwing.com/problem/content/846/
"""

n, m = map(int, input().split())
g = []
for _ in range(n):
    g.append(list(map(int, input().split())))
d = [[-1] * m for _ in range(n)]
d[0][0] = 0


def bfs():
    global n, m
    q = collections.deque()
    q.append([0, 0])
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    while q:
        pre_x, pre_y = q.popleft()
        for i, j in zip(dx, dy):
            x, y = pre_x + i, pre_y + j
            if 0 <= x < n and 0 <= y < m and g[x][y] == 0 and d[x][y] == -1:
                d[x][y] = d[pre_x][pre_y] + 1
                q.append([x, y])
    return d[-1][-1]


print(bfs())
