"""
Hungarian Algorithm
"""
"""
861. 二分图的最大匹配
https://www.acwing.com/problem/content/863/
"""

n1, n2, m = map(int, input().split())
g = [[] for _ in range(n1 + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
matched = [0] * (n2 + 1)    # n2 -> n1


def find(x, state):
    for y in g[x]:
        if not state[y]:
            state[y] = True
            if matched[y] == 0 or find(matched[y], state):
                matched[y] = x
                return True
    return False


res = 0
for i in range(1, n1 + 1):
    if find(i, [False] * (n2 + 1)):
        res += 1
print(res)
