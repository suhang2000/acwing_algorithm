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

"""
845. 八数码
https://www.acwing.com/problem/content/847/
"""

s = input().split()


def dfs(start):
    end = "12345678x"
    q = collections.deque()
    q.append(start)
    distance = dict()
    distance[''.join(start)] = 0
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    while q:
        cur = q.popleft()
        s_cur = ''.join(cur)
        if s_cur == end:
            return distance[s_cur]
        d = distance[s_cur]
        pre = s_cur.find('x')
        pre_x, pre_y = pre // 3, pre % 3
        for i, j in zip(dx, dy):
            x, y = pre_x + i, pre_y + j
            if 0 <= x < 3 and 0 <= y < 3:
                cur[pre], cur[x * 3 + y] = cur[x * 3 + y], cur[pre]
                s_next = ''.join(cur)
                if s_next not in distance:
                    q.append(cur.copy())
                    distance[s_next] = d + 1
                cur[pre], cur[x * 3 + y] = cur[x * 3 + y], cur[pre]
    return -1


print(dfs(s))
