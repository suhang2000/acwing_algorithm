"""
Bipartite Graph
"""
"""
860. 染色法判定二分图
https://www.acwing.com/problem/content/862/
"""

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
color = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)


def dfs(x, c):
    global n
    if color[x] != 0:
        return color[x] == c
    color[x] = c
    for v in g[x]:
        if not dfs(v, 3 - c):
            return False
    return True


flag = True
for i in range(1, n + 1):
    if color[i] == 0 and dfs(i, 1) is False:
        flag = False
        break
print("Yes" if flag else "No")
