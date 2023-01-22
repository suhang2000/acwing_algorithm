"""
DFS of Tree
"""
"""
846. 树的重心
https://www.acwing.com/problem/content/848/
"""

# version 1

n = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

visited = [False] * (n + 1)
res = n


def dfs(x: int) -> int:
    global visited, res, g, n
    visited[x] = True
    cur_max, cur_sum = 0, 1
    for y in g[x]:
        if not visited[y]:
            sub = dfs(y)
            cur_max = max(cur_max, sub)
            cur_sum += sub
    cur_max = max(cur_max, n - cur_sum)
    res = min(res, cur_max)
    return cur_sum


dfs(1)
print(res)

# version 2

n = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)
res = n


def dfs(x: int, fa: int) -> int:
    global res, n
    size, max_block = 1, 0
    for y in g[x]:
        if y != fa:
            sub = dfs(y, x)
            size += sub
            max_block = max(max_block, sub)
    max_block = max(max_block, n - size)
    res = min(res, max_block)
    return size


dfs(1, 0)
print(res)
