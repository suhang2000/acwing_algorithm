"""
DFS
"""
"""
842. 排列数字
https://www.acwing.com/problem/content/844/
"""
# version 1 状态数组
n = int(input())
path = [0] * n
used = [False] * (n + 1)


def dfs(idx):
    global n
    if idx == n:
        print(*path)
        return
    for i in range(1, n + 1):
        if not used[i]:
            path[idx] = i
            used[i] = True
            dfs(idx + 1)
            used[i] = False


dfs(0)

# version 2 状态压缩
n = int(input())
path = [0] * n


def dfs(idx, state):
    global n
    if idx == n:
        print(*path)
        return
    for i in range(1, n + 1):
        if state >> i & 1 == 0:
            path[idx] = i
            dfs(idx + 1, state + (1 << i))


dfs(0, 0)
