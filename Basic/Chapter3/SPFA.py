"""
SPFA
queue optimization of Bellman-Ford algorithm
"""
import collections
from math import inf

"""
851. spfa求最短路
https://www.acwing.com/problem/content/853/
用队列存储变短了的点，用这些点去更新后续点
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

"""
852. spfa判断负环
https://www.acwing.com/problem/content/854/
把所有点放入队列，判断循环过程中是否有点的路径大于n-1(一共n个点，路径最长不超过n-1)
"""
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
dist = [0] * (n + 1)  # 不需要初始化为inf，不是用来保存最短路径的，只需要记录距离更新信息即可
state = [True] * (n + 1)
cnt = [0] * (n + 1)
for _ in range(m):
    x, y, z = map(int, input().split())
    g[x].append((y, z))


def spfa_negative_cycles():
    global n
    # add all points
    dq = collections.deque(range(1, n + 1))
    # for i in range(1, n + 1):
    #     dq.append(i)

    while dq:
        x = dq.popleft()
        state[x] = False
        for y, z in g[x]:
            if dist[y] > dist[x] + z:
                dist[y] = dist[x] + z
                cnt[y] = cnt[x] + 1
                if cnt[y] > n - 1:
                    return True
                if not state[y]:
                    dq.append(y)
                    state[y] = True

    return False


print("Yes" if spfa_negative_cycles() else "No")
